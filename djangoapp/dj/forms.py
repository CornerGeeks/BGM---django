from django import forms
from dj.models import Meetup
import datetime


class MeetupForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the meetup group name.")
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Meetup

