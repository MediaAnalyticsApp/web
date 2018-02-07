import mainapp.views as mainapp
from django.urls import path

urlpatterns = [
    path('', mainapp.index, name='index'),
]
