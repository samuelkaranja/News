from django import forms
from . models import Newsletter, PostReply, Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'

class PostReplyForm(forms.ModelForm):
    class Meta:
        model = PostReply
        fields = '__all__'