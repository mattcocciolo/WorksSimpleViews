from . import views
from django.urls import path

urlpatterns = [
    # path('', views.main, name='name'),
    path('', views.upload_csv, name='upload_csv'),
]
