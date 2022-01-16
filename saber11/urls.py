from django.urls import path

from . import views

urlpatterns = [
    path('', views.ColegioListView.as_view(), name='index'),
    #path('<int:pk>/<slug:slug>', views.ColegioDetailView.as_view(), name='detalle_colegio'),
    path('<int:pk>/<slug:slug>', views.colegio_detail_view, name='detalle_colegio'),
]
