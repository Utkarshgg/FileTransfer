from django.contrib import admin
from .models import File, TransferLog

# Register your models here.
admin.site.register(File)
admin.site.register(TransferLog)
