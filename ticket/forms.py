from django import forms
from .models import Ticket

class TicketModelForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'project',
            'description',
        ]
