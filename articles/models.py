import datetime
from django.db import models

from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField("название статьи", max_length=250)
    article_text = models.TextField("текст статьи")
    pub_date = models.DateTimeField("дата публикации")

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def was_publish_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("имя автора", max_length=250)
    comment_text = models.CharField("коментарий", max_length=250)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
