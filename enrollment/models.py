from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from conference.models import Conference

class Enroll(models.Model):
    """Enroll info model"""
    
    WILL_COME_CHOICES = (
        ('m', _('Maybe I will come (50%)')),
        ('y', _('I will come (80%)')),
        ('s', _('I will not lose it! (100%)'))
    )
        
    # reg_code must be generate by system and it will be used to validate each user enrollment on conf day .
    reg_code = models.CharField(_('Enroll Code'), max_length=8)
    will_come = models.CharField(_('Will be come'), max_length=2, choices=WILL_COME_CHOICES)
    add_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Add Date'))
    conference = models.ForeignKey(Conference, verbose_name=_('Conference'))

    user =  models.ForeignKey(User, verbose_name=_('User'))
    
    def __unicode__(self):
        return unicode(self.reg_code)

    class Meta:
        verbose_name = _('Enroll')
        verbose_name_plural = _('Enrolls')    
        unique_together = (('user', 'conference'),)        