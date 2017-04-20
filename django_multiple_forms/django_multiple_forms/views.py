from django.contrib import messages

from django_multiple_forms import forms
from django_multiple_forms.multiple_forms import MultipleFormsView


class MultipleFormsDemoView(MultipleFormsView):
    template_name = 'forms.html'
    success_url = '/'
    forms_classes = [
        forms.AdminForm,
        forms.ContactForm,
        forms.SubscriptionForm,
        forms.SuggestionForm
    ]

    def get_forms_classes(self):
        user = self.request.user
        if not user.is_authenticated() or not user.is_staff:
            return list(filter(lambda form: not getattr(form, 'staff_only', False), self.forms_classes))
        return super(MultipleFormsDemoView, self).get_forms_classes()

    def form_valid(self, form):
        messages.success(self.request, "Submitted {}".format(form.__class__.__name__))
        return super(MultipleFormsDemoView, self).form_valid(form)
