from django import forms
from django.forms import ModelForm
from .models import Invoice, InvoiceItem, Payments

class NewInvoice(ModelForm):
    class Meta:
        model = Invoice
        exclude = ["date_added", "total", "invoice_id", "balance_due", "cgst_net", "sgst_net", "igst_net"]


class InvoiceItemForm(ModelForm):
    class Meta:
        model = InvoiceItem
        exclude = ["invoice", "serial_number", "cgst", "sgst", "igst", "sub_total", "tax"]
        widgets = {
            "total": forms.TextInput(attrs={"disabled":True})
        }

class NewInvoiceItemForm(ModelForm):
    class Meta:
        model = InvoiceItem
        exclude = ["invoice", "serial_number", "cgst", "sgst", "igst", "sub_total", "tax"]
        widgets = {
            "total": forms.TextInput(attrs={"disabled":True})
         
        }

class InvoiceItemUpdateForm(ModelForm):
    class Meta:
        model = InvoiceItem
        exclude = ["invoice", "serial_number"]
        widgets = {
            "total": forms.TextInput(attrs={"disabled":True})
        }

class InvoicePaymentForm(ModelForm):
    class Meta:
        model = Payments
        exclude = ["invoice"]
        widgets = {
            "date_added": forms.TextInput(attrs={"disabled":True})
        }

class NewInvoicePaymentForm(ModelForm):
    class Meta:
        model = Payments
        exclude = ["invoice"]
        widgets = {
            "date_added": forms.TextInput(attrs={"disabled":True})
        }