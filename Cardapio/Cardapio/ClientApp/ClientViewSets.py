from rest_framework.viewsets import  ModelViewSet
from .ClientSerializers import *
from .models import Client


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

