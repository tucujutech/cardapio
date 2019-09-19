from django.urls import path

from .views import *
urlpatterns=[
   path('core/', dashboard, name='core'),
   path('colaboradorNew/',ColaboradorCreate.as_view(), name='colaboradorNew'),
]