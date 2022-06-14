from django import forms
from . models import Newsletter, Comment, Post, Contact
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'