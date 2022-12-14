from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
                    attrs={'placeholder': 'Max length 200 characters'}))

    class Meta:
        model = Post
        fields = ['title', 'text', 'image']