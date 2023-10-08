from django.contrib.admin import ModelAdmin, register

from .models import Blog2


@register(Blog2)
class BlogAdmin(ModelAdmin):
    order = 2
