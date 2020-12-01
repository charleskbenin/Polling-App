from django.forms import ModelForm

from .models import Question

class PollForm(ModelForm):
    class  Meta:
        model=Question
        fields=['category','question','opt_1','opt_2','opt_3']
        
    