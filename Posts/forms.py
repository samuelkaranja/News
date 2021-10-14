from django import forms
from . models import Newsletter, PostReply

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'

class PostReplyForm(forms.ModelForm):
    class Meta:
        model = PostReply
        fields = '__all__'