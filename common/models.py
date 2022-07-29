from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
 

class BaseSoftDeletableModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    class Meta:
        abstract = True
        
    def soft_delete(self, user_id=None):
        self.is_deleted = True
        self.deleted_by = user_id
        self.deleted_at = timezone.now()
        self.save()


class Address(TimestampedModel, BaseSoftDeletableModel):
    state = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    pin_code = models.IntegerField()

    def __str__(self) -> str:
        return self.country


class Place(Address):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
