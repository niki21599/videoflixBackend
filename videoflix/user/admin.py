from django.contrib import admin

from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm 
    fieldsets= (
        *UserAdmin.fieldsets, (
            "Individuelle Daten", {
                "fields": (
                    "custom", 
                    "phone", 
                    "adress"
                )
            }
        )
    )
    pass
admin.site.register(CustomUser, CustomUserAdmin)

