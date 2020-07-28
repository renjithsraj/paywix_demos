from django.contrib import admin
from checkout.models import Transaction
# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'


admin.site.register(Transaction, TransactionAdmin)
