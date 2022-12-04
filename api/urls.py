from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:user_id>/events/',
         views.EventsViewSet.as_view(
             {'get': 'list'}), name='user_events'
         ),
]
