from django.contrib import admin
from .models import User, Wrong,Bookmark


# Register your models here.

@admin.register(Bookmark)
@admin.register(User)
@admin.register(Wrong)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email']


class WrongAdmin(admin.ModelAdmin):
    list_display = ['pr_id', 'email']


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['pr_id', 'email']
