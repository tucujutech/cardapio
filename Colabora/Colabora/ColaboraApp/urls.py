from django.urls import path
from .views import *
urlpatterns = [
   path('userReg/', RegUser.as_view(), name='userReg/'),
   path('colaboradorNew/',ColaboradorCreate.as_view(), name='colaboradorNew/'),
   path('colabList/', ColabList.as_view(), name='colabList/'),
   path('colabDetail/<int:pk>/', ColabDetail.as_view(), name='colabDetail/'),
   path('ColabDelete/<int:pk>/',ColabDelete.as_view(), name='colabDelete/'),
   path('formaRegister/',FormacaoCreate.as_view(), name='formaRegister/'),
   path('formaList/', FormacaoList.as_view(), name='formaList/'),
   path('formaDelete/<int:pk>',FormacaoDelete.as_view(), name='formaDelete/'),
   path('departamento/', DerpartmentView.as_view(), name='departamento/'),
   path('departamentoDelete/<int:pk>',DepartmentDelete.as_view(),name='departamentoDelete/'),
   path('funcao/', FuncaoRegister.as_view(), name='funcao/'),
   path('funcaoDelete/<int:pk>',FuncaoDelete.as_view(), name='funcaoDelete/'),
]