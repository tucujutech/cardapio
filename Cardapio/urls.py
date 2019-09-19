
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from AdmApp.AdmViewSet import ItemViewSet
from AdmApp.AdmViewSet import GroupViewSet
from AdmApp.AdmViewSet import StatusViewSet
from AdmApp.AdmViewSet import DeliveryManViewSet
from ClientApp.ClientViewSets import ClientViewSet

router = DefaultRouter()
router.register('AdmApp/Item', ItemViewSet)
router.register('AdmApp/secsoes_cardapio',GroupViewSet)
router.register('AdmApp/status_register', StatusViewSet)
router.register('AdmApp/deliveryman_register', DeliveryManViewSet)
router.register('ClientApp/client', ClientViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
