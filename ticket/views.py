from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Ticket
from .forms import TicketModelForm
from django.contrib.auth.mixins import LoginRequiredMixin#,PermissionRequriedMixin

from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
# Create your views here.
'''
@permission_required('project.can_add_ticket')
def ticket_view(request):
    return HttpResponse('Ticket')


class MyView(PermissionRequiredMixin, View):
    #single permission_required=('app.permission','app.permission')
    #multiple permission_requried= ('app.permission', 'app.permission')
'''
class TicketListView(LoginRequiredMixin,ListView):
    template_name='ticket/ticket_list.html'
    queryset = Ticket.objects.all()

class TicketDetailView(DetailView):
    template_name='ticket/ticket_detail.html'
    queryset = Ticket.objects.all()

    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Ticket,id=id_)

class TicketCreateView(CreateView):
    template_name='ticket/ticket_create.html'
    form_class = TicketModelForm
    queryset = Ticket.objects.all()
'''
class TicketUpdateView(UpdateView):
    template_name='ticket/ticket_create.html'
    form_class = TicketModelForm
    queryset = Ticket.objects.all()

    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Ticket,id=id_)

class TicketDeleteView(DeleteView):
    template_name='ticket/ticket_delete.html'
    queryset = Ticket.objects.all()

    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Ticket,id=id_)

    def get_success_url(self):
        return reverse('ticket:ticket-list')
        '''
