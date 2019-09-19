from django.urls import path

from .views import *

urlpatterns = [
    path('departamentos/', DerpartmentView.as_view(), name='departamentos'),
    path('departamentoDelete/<int:pk>', DerpartmentView.DepartmentDelete, name='departamentoDelete'),
    path('funcao/', FuncaoView.as_view(), name='funcaoView'),
    path('funcaoDelete/<int:pk>',FuncaoView.FuncaoDelete,name='funcaoDelete'),
]
