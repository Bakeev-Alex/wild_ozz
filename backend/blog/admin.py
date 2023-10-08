from django.contrib.admin import ModelAdmin, register

from .models import Blog


@register(Blog)
class BlogAdmin(ModelAdmin):
    order = 3
