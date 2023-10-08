from django.db import models


class Blog3(models.Model):
    title: str = models.CharField("Заголовок", max_length=255)

    class Meta:
        verbose_name = "Блог_3"
        verbose_name_plural = "Блоги_3"
        db_table = "blog_blog_3"
