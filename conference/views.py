from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.conf import settings

from conference.forms import TalkForm,TalkAttachmentForm
from conference.models import TalkAttachment,Talk


@login_required
def SubmitTalk(request):
    if request.method == 'POST':
        form = TalkForm(request.POST,request.FILES)     
        if form.is_valid():
            talk=form.save(commit=False)
            talk.user = request.user
            talk.status = Talk.STATUS_PENDING   
            talk.save()
            form.save_m2m()
            if form.cleaned_data['attachment'] :
                file = form.cleaned_data['attachment'] #request.FILES['attachment']     
                TalkAttachment.objects.create( attachment = form.cleaned_data['attachment'],
                                               about = form.cleaned_data['about'],
                                               talk = talk,
                                               name   = file.name  ,
                                               )                        
            return render_to_response('conference/submit_talk.html',
                                  { 'talk_submitted':'Talk submitted.'})                                                                                
    else:
        form = TalkForm()
                        
    return render_to_response('conference/submit_talk.html',
                                  { 'form':form})                                                          

                                                                  
@login_required
def UpdateTalk(request):
    if request.method == 'POST':
        form = TalkAttachmentForm(request.POST,request.FILES)   
        if form.is_valid():
            TalkAttachment.objects.create( attachment = form.cleaned_data['attachment'],
                                           about = form.cleaned_data['about'],
                                           talk = form.cleaned_data['talk'],
                                           name   = form.cleaned_data['attachment'].name  ,
                                                                                   accepted = False,
                                          )     
            return render_to_response('conference/submit_talk.html',{ 'talk_submitted':'Talk updated.'})                                                                                
    else:
        form = TalkAttachmentForm()             
    return render_to_response('conference/submit_talk.html',{ 'form':form})

@login_required
def StatusTalk(request):
    talks = Talk.objects.filter(user=request.user)
    return render_to_response('conference/status_talk.html',{'talks':talks})

def AcceptedTalk(request):
    talk_status=[]
    talks = Talk.objects.filter(status=Talk.STATUS_APPROVED)
    for  talk in talks :
        talk_status.append([talk,TalkAttachment.objects.filter(talk=talk)])
    return render_to_response('conference/accepted_talk.html',{ 'talk_status':talk_status})


        