from django import forms
from blog.models import Author,Post
from django.core.validators import RegexValidator
import re

valid_email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

class AuthorForm(forms.ModelForm):
    email=forms.EmailField(validators=[RegexValidator(valid_email_regex)])
    class Meta:
        model=Author
        fields='__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'


        