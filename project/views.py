from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Project
from .forms import ProjectModelForm
from django.contrib.auth.mixins import LoginRequiredMixin#,PermissionRequriedMixin

from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from ticket.models import Ticket
# Create your views here.
@permission_required('project.can_add_ticket')
def ticket_view(request):
    return HttpResponse('Ticket')

'''
class MyView(PermissionRequiredMixin, View):
    #single permission_required=('app.permission','app.permission')
    #multiple permission_requried= ('app.permission', 'app.permission')
'''
class ProjectListView(LoginRequiredMixin,ListView):
    template_name='project/project_list.html'
    queryset = Project.objects.all()


class ProjectDetailView(DetailView):
    template_name='project/project_detail.html'
    queryset = Project.objects.all()

    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Project,id=id_)

class ProjectCreateView(CreateView):
    template_name='project/project_create.html'
    form_class = ProjectModelForm
    queryset = Project.objects.all()

class ProjectUpdateView(UpdateView):
    template_name='project/project_create.html'
    form_class = ProjectModelForm
    queryset = Project.objects.all()

    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Project,id=id_)

class ProjectDeleteView(DeleteView):
    template_name='project/project_delete.html'
    queryset = Project.objects.all()

    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Project,id=id_)

    def get_success_url(self):
        return reverse('project:project-list')
