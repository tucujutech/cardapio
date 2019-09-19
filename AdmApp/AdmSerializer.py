from rest_framework.serializers import ModelSerializer

from .models import *


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','name_item', 'group', 'description', 'price', 'availability')


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name_group')


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'status')


class DeliveryManSerializer(ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = ('id', 'name', 'dt_birthday', 'cnh', 'active')