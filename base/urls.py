from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.main, name='main'),
    path('panel/', views.panel, name='panel'),
    path('report/', views.report, name='report'),
    path('start/', views.start, name='start'),
    path('region/', views.region, name='region'),
    path('search/', SearchResultsView.as_view(), name='search'),
]

