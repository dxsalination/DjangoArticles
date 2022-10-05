from tabnanny import verbose
from django.db import models


class Articles(models.Model):

    title = models.CharField('Название статьи', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Новость: {self.title}'


    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta():
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'