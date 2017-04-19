from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from django_multiple_forms import forms


class IndexView(TemplateView):
    template_name = 'index.html'


class TwoFormsBothMustPassView(TemplateView):
    template_name = 'two_forms.html'

    def get_context_data(self, **kwargs):
        data = super(TwoFormsBothMustPassView, self).get_context_data(**kwargs)
        data.setdefault('contact_form', forms.ContactForm())
        data.setdefault('subscription_form', forms.SubscriptionForm())
        return data

    def post(self, request):
        contact_form = forms.ContactForm(request.POST)
        subscription_form = forms.SubscriptionForm(request.POST)
        if contact_form.is_valid() and subscription_form.is_valid():
            contact = contact_form.cleaned_data
            subs = subscription_form.cleaned_data

            # ... do something with the data
            print(contact, subs)

            # redirect back to view, to prevent accidentally submitting form second time
            return redirect('two_both')

        # something is wrong, display errors
        context = self.get_context_data(contact_form=contact_form, subscription_form=subscription_form)
        return TemplateResponse(request, self.template_name, context)
