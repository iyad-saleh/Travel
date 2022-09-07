from django.db import models
from PIL import Image
from django.conf import settings
from company.models import Company
from django.core.validators import RegexValidator
from ked.models import Journal
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from account.models  import Account

class Category(models.Model):
    name = models.CharField(max_length=255)
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

# Create your models here.
class Customer(models.Model):
    company     = models.ForeignKey(Company, on_delete=models.CASCADE )
    account = models.ForeignKey(Account, on_delete=models.CASCADE )
    category    = models.ManyToManyField(Category,  related_name='category')
    logo = models.ImageField(default='default.jpg', upload_to='Customer_pics', blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    # phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{7,15}$")
    phoneNumber1 = models.CharField( max_length = 25, unique = True, blank=True, null=True)
    phoneNumber2 = models.CharField( max_length = 25, unique = True, blank=True, null=True)
    phoneNumber3 = models.CharField( max_length = 25, unique = True, blank=True, null=True)
    phoneNumber4= models.CharField( max_length = 25, unique = True, blank=True, null=True)
    tradeRecord = models.CharField(max_length=500, blank=True, null=True)
    email       = models.EmailField( blank=True, null=True)
    webSite     =  models.URLField(max_length = 200, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name='author_customer')
    journal     = GenericRelation(Journal)
    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = 'الشركات'


    def __str__(self):
        return self.account.name

        img = Image.open(self.logo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.logo.path)