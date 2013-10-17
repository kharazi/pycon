from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class Conference(models.Model):
    """Conference info model"""
    
    name = models.CharField(_('Conference Name'), max_length=20)
    start_date = models.DateTimeField(_('Start date'))
    end_date = models.DateTimeField(_('End date'))
    reg_start = models.DateTimeField(_('Start Registration'))
    reg_close = models.DateTimeField(_('Close Registration'))
    reg_quota = models.IntegerField(_('Registration quota'))
    address = models.TextField(_('Address'))

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'conference'

class Category(models.Model):
  name = models.CharField(max_length=30, unique=True)

  class Meta:
    verbose_name_plural = 'categories'

  def __unicode__(self):
    return self.name

class Talk(models.Model):
    """Submited talk model"""
    
    STATUS_PENDING = 'p'
    STATUS_DENIED = 'd'
    STATUS_CANCELLED = 'c'
    STATUS_ALTERNATE = 'al'
    STATUS_APPROVED = 'ap'
    
    AUDIENCE_CHOICES = (
        ('e', 'Everyone'),
        ('b', 'Beginner'),
        ('i', 'Intermediate'),
        ('a', 'Advanced'),
    )    
        
    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_DENIED, 'Denied'),
        (STATUS_CANCELLED, 'Speaker Cancelled'),
        (STATUS_ALTERNATE, 'Alternate'),
        (STATUS_APPROVED, 'Approved'),
    )    
    # Talk data
    title = models.CharField(_('Title'), max_length=150, unique=True)
    description = models.CharField(_('Description'), max_length=255)
    short_abstract = models.TextField(_('Short Abstract'), max_length=1000)
    long_abstract = models.TextField(_('Long Abstract'), max_length=10000, blank=True)
    msg = models.TextField(_('Msg'), max_length=1000, blank=True)
        
    # private data
    submit_date = models.DateField(_('Submit Date'), auto_now_add=True)
    status = models.CharField(_('Status'), max_length=2, choices=STATUS_CHOICES, default=STATUS_CHOICES[0])
    notes = models.TextField(_('Notes'), max_length=1000, blank=True, default=_("under dissection"))    
        
        
    # categories
    categories = models.ManyToManyField(Category, verbose_name='Categories')
    audiences = models.CharField(_('Audiences'), max_length=2, choices=AUDIENCE_CHOICES)
        
    # presenter 
    user =  models.ForeignKey(User, verbose_name=_('User'))

        # conference
    conference = models.ForeignKey(Conference, verbose_name=_('Conference'))
    
    def __unicode__(self):
        return self.title[:20] + ('...' if len(self.title) > 20 else '')

class TalkAttachment(models.Model):
    name = models.CharField(_('Name'), max_length=128)
    attachment = models.FileField(upload_to="/")
    about = models.CharField(_('About'), max_length=150)
    talk = models.ForeignKey(Talk, verbose_name=_('Talk'))
    accepted = models.BooleanField(_('Accepted'), default=False)

        
class Score(models.Model):
    score = models.IntegerField(_('Score'), default=0)
    talk = models.ForeignKey(Talk, verbose_name=_('Talk'))