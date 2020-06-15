from django.urls import path
from . import views

urlpatterns = [
    path('', views.default),
    path('shows/new', views.new_show),
    path('shows', views.shows),
    path('shows/create', views.create_show),
    path('shows/<int:id>', views.show_details),
    path('shows/<int:id>/destroy', views.destroy),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/update', views.update_show)
]
