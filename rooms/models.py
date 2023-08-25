from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    number = models.IntegerField(verbose_name="Номер комнаты",)
    count_places = models.IntegerField(verbose_name="Количество мест", default = 1)
    price = models.DecimalField(verbose_name="Цена", max_digits=6, decimal_places=2)
    hotel = models.ForeignKey("Hotel", related_name="rooms", on_delete=models.CASCADE, verbose_name="Отель",)
    is_booked = models.BooleanField(default=False, verbose_name="Есть бронь",)

    def __str__(self):
        return f"Комната {self.number}, Отель: {self.hotel.title}"

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"


class Hotel(models.Model):
    title = models.CharField(verbose_name="Название отеля", max_length=150)
    description = models.TextField(verbose_name="Описание отеля")
    stars = models.IntegerField(verbose_name="Количество звезд",default=3)

    def __str__(self):
        return f"Отель: {self.title} Кол-во звезд: {self.stars}"

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books", verbose_name="Постоялец",)
    date_start = models.DateTimeField(auto_now_add=True, verbose_name="Начало бронирования",)
    date_finish = models.DateTimeField(verbose_name="Конец бронирования",)
    room = models.OneToOneField(Room,on_delete=models.CASCADE,verbose_name='Бронируемая комната')

    def __str__(self):
        return f"Бронь: {self.owner.username} {self.date_start} - {self.date_finish}"

    class Meta:
        verbose_name = "Запись бронирования"
        verbose_name_plural = "Записи бронирования"