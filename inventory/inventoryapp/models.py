from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=50, verbose_name='Найменування')
    unit = models.CharField(max_length=10, verbose_name='Одиниця виміру')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Ціна')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class DeliveryNotes(models.Model):
    date = models.DateField(verbose_name='Дата')
    type = models.CharField(
        max_length=3, choices=(('IN', 'IN'), ('OUT', 'OUT')), verbose_name='Тип')
    note = models.CharField(max_length=50, verbose_name='Примітка')

    class Meta:
        verbose_name = 'Накладна на поставку'
        verbose_name_plural = 'Накладні на поставку'


class DeliveryNoteDetails(models.Model):
    delivery_note = models.ForeignKey(
        DeliveryNotes, on_delete=models.CASCADE, verbose_name='Накладна на поставку')
    goods = models.ForeignKey(
        Goods, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Кількість')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Ціна')

    class Meta:
        verbose_name = 'Деталі накладної на поставку'
        verbose_name_plural = 'Деталі накладних на поставку'


class AdditionalServices(models.Model):
    name = models.CharField(max_length=50, verbose_name='Найменування')
    unit = models.CharField(max_length=10, verbose_name='Одиниця виміру')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Ціна')

    class Meta:
        verbose_name = 'Додаткова послуга'
        verbose_name_plural = 'Додаткові послуги'


class ServiceDetails(models.Model):
    delivery_note = models.ForeignKey(
        DeliveryNotes, on_delete=models.CASCADE, verbose_name='Накладна на поставку')
    service = models.ForeignKey(
        AdditionalServices, on_delete=models.CASCADE, verbose_name='Додаткова послуга')
    quantity = models.IntegerField(verbose_name='Кількість')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Ціна')

    class Meta:
        verbose_name = 'Деталі додаткової послуги'
        verbose_name_plural = 'Деталі додаткових послуг'


class Cost(models.Model):
    delivery_note = models.ForeignKey(
        DeliveryNotes, on_delete=models.CASCADE, verbose_name='Накладна на поставку')
    goods = models.ForeignKey(
        Goods, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Кількість')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Ціна')

    class Meta:
        verbose_name = 'Витрати'
        verbose_name_plural = 'Витрати'
