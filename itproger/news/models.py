from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50, null=True)
    anons = models.CharField('Анонс',  max_length=250, null=True)
    full_text = models.TextField('Статья', null=True)
    date = models.DateTimeField('Дата публикации', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'