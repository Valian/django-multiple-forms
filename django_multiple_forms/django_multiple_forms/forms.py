from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=60)
    message = forms.CharField(max_length=200, widget=forms.TextInput)


class SubscriptionForm(forms.Form):
    need_spam = forms.BooleanField(required=False)
