from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=60)
    message = forms.CharField(max_length=200, widget=forms.TextInput)


class SubscriptionForm(forms.Form):
    email = forms.EmailField()
    want_spam = forms.BooleanField(required=False)


class SuggestionForm(forms.Form):
    text = forms.CharField(max_length=200, widget=forms.TextInput)
    type = forms.ChoiceField(choices=[('bug', 'Bug'), ('feature', 'Feature')])


class AdminForm(forms.Form):
    staff_only = True
    global_message = forms.CharField(max_length=200, widget=forms.TextInput)