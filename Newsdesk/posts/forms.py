from django.forms import ModelForm, ClearableFileInput, Textarea, Select, SelectMultiple, CheckboxSelectMultiple
from .models import Post, Category, Comment, Message, PostPhoto
from django import forms
class PostForm(ModelForm):
    #video_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    class Meta:
        model = Post

        fields = ['headline', 'text', 'categories', 'images']
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст...'
            }),
            'categories': CheckboxSelectMultiple(attrs={
                'class': 'form-check-label',
                'size': '100',
            }),
        }
class PhotoForm(ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    class Meta:
        model = PostPhoto

        fields = ['headline', 'text', 'categories', 'image']
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст...'
            }),
            'categories': CheckboxSelectMultiple(attrs={
                'class': 'form-check-label',
                'size': '100',
            }),
        }
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = []
class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['com_text']
        widgets = {
            'com_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст...',
                'rows': "3",
            }),}
class AddMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст...',
                'rows': "3",
            }),}