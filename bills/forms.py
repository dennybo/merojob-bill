from django import forms

from .models import Bill


class BillForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = ['client', 'item', 'quantity', 'rate']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Quantity can't be less than 1", code='invalid')
        return quantity

    def clean_rate(self):
        rate = self.cleaned_data.get('rate')
        if rate <= 0.0:
            raise forms.ValidationError("Rate should be more than zero.", code='invalid')
        return rate
