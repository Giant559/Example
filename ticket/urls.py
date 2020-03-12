from django.urls import path
from .views import (
    TicketListView,
    TicketDetailView,
    TicketCreateView,
#    TicketUpdateView,
#    TicketDeleteView,
#    ticket_view,
)
app_name='ticket'

urlpatterns = [
    path('',TicketListView.as_view(),name='ticket-list'),
    path('<int:id>/',TicketDetailView.as_view(),name='ticket-detail'),
    path('create/',TicketCreateView.as_view(),name='ticket-create'),
#    path('<int:id>/update/',ProjectUpdateView.as_view(),name='project-update'),
#    path('<int:id>/delete/',ProjectDeleteView.as_view(),name='project-delete'),
#    path('ticket/',ticket_view,name='ticket-view')
]
