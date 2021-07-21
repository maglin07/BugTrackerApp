from django import forms
from homepage.models import TicketModel


class TicketForm(forms.ModelForm):
    class Meta:
        model = TicketModel
        fields = ['title', 'description']
