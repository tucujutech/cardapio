from django.db import models

# Create your models here.


class Group(models.Model):
    name_group = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = 'Group'

    def __str__(self):
        return self.name_group

# =================================================================================


class Item(models.Model):
    name_item = models.CharField(max_length=30, null=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=100, null=False)
    price = models.FloatField(null=False)
    availability = models.BooleanField(null=False, default=1)

    class Meta:
        db_table = 'Item'

    def __str__(self):
        return self.name_item

# ===================================================================================


class Status(models.Model):
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'Status'

    def __str__(self):
        self.status

# ===================================================================================


class DeliveryMan(models.Model):
    name = models.CharField(max_length=30, null=False)
    dt_birthday = models.DateField(null=False)
    cnh = models.CharField(max_length=12, null=False)
    active = models.BooleanField(null=False, default=1)

    class Meta:
        db_table = 'DeliveryMan'

    def __str__(self):
        return self.name

# ===================================================================================

#  >>>>>>>>>>>>  It is missing the Order model <<<<<<<<<<<<<<