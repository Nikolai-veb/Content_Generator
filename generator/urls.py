from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListSitesView.as_view(), name='list_sites'),
    path("<int:pk>/", views.ListSitesView.as_view(), name='site_under_category'),
    path("<slug:slug_category>/", views.ListSitesView.as_view(), name='site_category'),

]