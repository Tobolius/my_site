from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name='Название публикации')
    photo = models.ImageField(upload_to='post_images', blank=True, null=True, verbose_name='Фото публикации')
    text = RichTextUploadingField(verbose_name='Содержимое')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания публикации')

    def __str__(self):
        return self.title


class PostStatistic(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField('Дата', default=timezone.now)
    views = models.IntegerField("Просмотры", default=0)

    def __str__(self):
       return self.article.title

    

class Info(models.Model):
    description = models.CharField(max_length=500, verbose_name="Короткое описание")
    email = models.CharField(max_length=100, verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=150, verbose_name="Адрес")

    def __str__(self):
        return "Информация"

    class Meta:
        verbose_name_plural = 'Info'
        verbose_name = 'Info'
