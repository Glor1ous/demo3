from django.db import models

class CourseModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название курса'
        verbose_name_plural = 'Название курса'

class ApplicationModel(models.Model):
    cousre = models.ForeignKey(CourseModel, on_delete=models.CASCADE, verbose_name='Название курса')
    preferred_start_date = models.DateField(verbose_name='Дата желаемого посещения')
    PAYMENT_CHOICES = [('1','Наличные'),
                       ('2','Перевод'),]
    payment_method = models.CharField(max_length=255, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты')
    STATUC_CHOICES = [('1','Новая'),
                      ('2','Идет обучение'),
                      ('3','Обучение завершено'),]
    status = models.CharField(max_length=1, choices=STATUC_CHOICES, verbose_name='Статус')

    def __str__(self):
        return self.cousre.name
    class Meta:
        verbose_name = 'Заявкy'
        verbose_name_plural = 'Заявки'

