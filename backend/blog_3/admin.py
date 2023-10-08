from django.contrib.admin import ModelAdmin, register
from django.contrib.admin import AdminSite

from .models import Blog3


@register(Blog3)
class BlogAdmin(ModelAdmin):
    order = 1
