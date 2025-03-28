from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'telefone', 'idade', 'endereco', 'is_staff')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Pessoais', {'fields': ('nome', 'biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'animais')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Pessoais', {'fields': ('nome', 'biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'animais')}),
    )

admin.site.register(User, CustomUserAdmin)


# Register your models here.
