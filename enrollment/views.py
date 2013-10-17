import hashlib
from time import time

from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from enrollment.forms import EnrollForm

@login_required 
def enroll(request):
    if request.method == 'POST':
        form = EnrollForm(request.user,data=request.POST)
        if form.is_valid():
            enroll = form.save(commit=False)
            m = hashlib.md5()
            m.update(str(time()))
            enroll.reg_code = m.hexdigest()[:5]
            enroll.user = request.user
            enroll.save()
            return render_to_response('enrollment/enroll.html',
                                  {'enroll_submitted': _('Enroll submitted .')},
                                  context_instance=RequestContext(request))
    else:
        form = EnrollForm(request.user)
    return render_to_response('enrollment/enroll.html', {'form': form},
                              context_instance=RequestContext(request))