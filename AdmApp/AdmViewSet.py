from rest_framework.viewsets import ModelViewSet

from .AdmSerializer import *
from .models import *


# ============ Item ViewSet ============
class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# ============ Group ViewSet ============
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# ============ Status ViewSet ===========
class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# ============ DeliveryMan ViewSet ==========
class DeliveryManViewSet(ModelViewSet):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManSerializer