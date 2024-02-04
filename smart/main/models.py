from django.db import models

class Course(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    anons = models.TextField('Анонс')
    text = models.TextField('Текст')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class PreSchool(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    anons = models.TextField('Анонс')
    text = models.TextField('Текст')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'До-школьное'
        verbose_name_plural = 'До-школьные'

class ExtraClass(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    anons = models.TextField('Анонс')
    text = models.TextField('Текст')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Дополнительный'
        verbose_name_plural = 'Дополнительные'