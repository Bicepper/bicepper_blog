from django import forms
from .models import BlogPost


class BlogPostSearch(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'placeholder': '検索',
            'class': 'side-bar-form-input',
        }))

# class BlogPostSearch(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = {
#             'title',
#         }