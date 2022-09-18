from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from common.models import BaseModel, SoftDeleteModel


class Account(BaseModel, SoftDeleteModel):
    Accountchoise=(
        ('متاجرة', (
            ('1','التأشيرات'),
            ('2','تذاكر طيران'),
            ('3','تذاكر برية'),
            ('4','تذاكر بحرية'),
            ('5','شحن'),
            ('6','حجز فندقي'),
            ('7','مستندات سفر'),
            ('8','عمولات'),
            ('9','تحويل عملة'),
            ('10','الاصول'),
            ('11','أرباح وخسائر'),
            ('12','رصيد مدور'),
            ('13','الاهتلاك'),
            ('14','مستحقات الموظفين'),
            ('15','التأمينات الاجتماعية'),
            ('16','المصروفات'),
                    )),
        ('الشركات و الزبائن', (
            ('20', 'الزبائن'),
            ('21','شركات التأشيرات'),
            ('22','شركات نقل جوي'),
            ('23','شركات نقل بري'),
            ('24','شركات نقل بحري'),
            ('25','فنادق'),
            ('26','شركات شحن'),
            ('27','شركات تأمين صحي'),
        )),
      ('حسابات الشركة',(
            ('30','المالكين'),
            ('31','الموظفين'),
            ('32','الصناديق'),
            ('33','مصاريف يومية'),
            ('34','الحافلات'),

      )

      )

    )


    name         = models.CharField(max_length=255 )
    account_type = models.CharField(choices=Accountchoise ,max_length=4, blank=True)

    class Meta:
        unique_together = [['name', 'company']]

    def __str__(self):

        return self.name
