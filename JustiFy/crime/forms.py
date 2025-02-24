from django import forms
from .models import CrimePost, Comment

class CrimePostForm(forms.ModelForm):
    # Use a datetime-local widget for crime_time
    crime_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    class Meta:
        model = CrimePost
        fields = ['title', 'description', 'division', 'district', 'image', 'video', 'crime_time']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
