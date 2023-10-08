from django.db import models


class Blog2(models.Model):
    title: str = models.CharField("Заголовок", max_length=255)

    class Meta:
        verbose_name = "Блог_2"
        verbose_name_plural = "Блоги_2"
        db_table = "blog_blog_2"