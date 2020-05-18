from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст сообщения')
    published = models.DateTimeField(auto_now_add=True, db_index = True, verbose_name='Опубликованно')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-published']