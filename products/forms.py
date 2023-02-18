from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', ]
        labels = {
            'body': 'ایمیل'
        }
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'ایمیل شما'})
        }