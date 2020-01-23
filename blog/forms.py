from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse


class BlogPostSearch(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'placeholder': '検索',
            'class': 'side-bar-form-input',
        }))


SUBJECT_CHOICES = (
    ('', '選択してください'),
    ('ブログの内容について', 'ブログの内容について'),
    ('個人情報について', '個人情報について'),
    ('著作権について', '著作権について'),
    ('その他', 'その他'),
)


class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control-input',
            'placeholder': 'お名前',
        }),
        required=True
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control-input',
            'placeholder': 'メールアドレス',
        }),
        required=True
    )
    subject = forms.ChoiceField(
        label='',
        widget=forms.Select(attrs={
            'class': 'form-control-select',
            'placeholder': '種別',
        }),
        choices=SUBJECT_CHOICES,
        required=True)
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control-field',
            'placeholder': 'お問い合わせ内容',
        }),
        required=True
    )

    def send_email(self, request):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        context = {
            'message': message,
            'name': name,
            'email': email,
            'user_ip': request.META['REMOTE_ADDR'],
            'user_agent': request.META['HTTP_USER_AGENT'],
            'http_host': request.META['HTTP_HOST'],
        }
        message_format = render_to_string('mail/mail.txt', context, request)
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]
        try:
            send_mail(subject, message_format, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダーが検出されました")

