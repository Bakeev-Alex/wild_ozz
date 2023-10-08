from django.db import models


class Blog(models.Model):
    title: str = models.CharField("Заголовок", max_length=255)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        db_table = "blog_blog"
