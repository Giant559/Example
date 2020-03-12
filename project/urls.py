from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    ticket_view,
)
app_name='project'

urlpatterns = [
    path('',ProjectListView.as_view(),name='project-list'),
    path('<int:id>/',ProjectDetailView.as_view(),name='project-detail'),
    path('create/',ProjectCreateView.as_view(),name='project-create'),
    path('<int:id>/update/',ProjectUpdateView.as_view(),name='project-update'),
    path('<int:id>/delete/',ProjectDeleteView.as_view(),name='project-delete'),
#    path('ticket/',ticket_view,name='ticket-view')
]
