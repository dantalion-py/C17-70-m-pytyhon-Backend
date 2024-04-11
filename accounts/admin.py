from django.contrib import admin
from .models import *


admin.site.register(Administrator)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(CustomUser)