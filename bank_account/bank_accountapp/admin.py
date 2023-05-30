from django.contrib import admin
from .models import BankAccountMember,BankAccountAdmin
admin.site.register(BankAccountMember,BankAccountAdmin)