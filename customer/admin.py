from django.contrib import admin

from .models import Customer,Category

# admin.site.register(Company)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ( 'id',
                'account',
                'logo',
                'get_address',
                'phoneNumber1',
                'phoneNumber2',
                'get_tradeRecord',
                'email',
                'get_category',
                'webSite',
                'create_at',
                'update_at',
                'author',
                )
    list_filter = (
                'category',
                'create_at',
                'update_at',
                'author',
                )
    def get_category(self, obj):
        return "\n".join([p.name for p in obj.category.all()])
    def get_tradeRecord(self, obj):
        if obj.tradeRecord:
            return obj.tradeRecord[:10]+'...'
    def get_address(self, obj):
        if obj.address:
            return obj.address[:10]+'...'
# admin.site.register(CompanyType)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (    'id',
                        'name',
                        'author',
                        'create_at',
                        'update_at',
                )
    list_filter = (

                'author',
                'create_at',
                'update_at',
)











