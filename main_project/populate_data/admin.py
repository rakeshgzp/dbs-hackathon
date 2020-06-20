from django.contrib import admin

from .models import customer_list,customer_values,rules,decision
# Register your models here.
admin.site.register(customer_list)
admin.site.register(customer_values)
admin.site.register(rules)
admin.site.register(decision)
