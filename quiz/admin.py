from django.contrib import admin
from .models import Quiz


# Register your models here.
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['pr_id', 'subject', 'title']
    search_fields = ('pr_id', 'subject',)
