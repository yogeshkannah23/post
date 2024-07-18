from django import forms
from posts.models import *

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name",max_length=5,error_messages={
        "required":"This field must have valules before save",
        "max_length":"Your name is less than five characters",
    })
    address = forms.CharField(label="Address",max_length=100)
    feedback = forms.CharField(label="Feedback",widget=forms.Textarea,max_length=200)
    ratings = forms.IntegerField(label="Ratings",max_value=5,min_value=0)

    