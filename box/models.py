from django.db import models
from django.conf import settings
from company.models import Company
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from account.models  import Account


class Box(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE )
    company     = models.ForeignKey(Company, on_delete=models.CASCADE )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.name