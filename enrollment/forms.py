from django import forms

from enrollment.models import Enroll
                
class EnrollForm(forms.ModelForm):
    'Main form to enroll a conference'
    def __init__(self, user, *args, **kwargs):
        super(EnrollForm, self).__init__(*args, **kwargs)
        self.user = user
    def clean_conference(self):
        conference = self.cleaned_data['conference']
        if self.user.enroll_set.filter(conference=conference) :
            raise forms.ValidationError("Your enrollment for this conference submitted  .")
        else :
            return conference
                        
    class Meta:
        model = Enroll
        exclude = ('reg_code', 'user')