from django.contrib import admin
from .models import CustomeUser,transaction

# Register your models here.


admin.site.register(CustomeUser)
admin.site.register(transaction)
