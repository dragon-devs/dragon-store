from django.contrib import admin

from playground import models

# Register your models here.


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    #autocomplete_fields = ['name']
    list_display = ['name', 'age', 'gender', 'salary', 'position']
    list_editable = ['position']
    list_per_page = 10
    #list_select_related = ['user']
    #ordering = ['user__first_name', 'user__last_name']
    #search_fields = ['first_name__istartswith', 'last_name__istartswith']

    # @admin.display(ordering='orders_count')
    # def orders(self, customer):
    #     url = (
    #             reverse('admin:store_order_changelist')
    #             + '?'
    #             + urlencode({
    #                 'customer__id': str(customer.id)
    #             }))
    #     return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)
        
    
    # def get_queryset(self, request):
    #     return super().get_queryset(request).annotate(
    #         orders_count=Count('order')
    #     )