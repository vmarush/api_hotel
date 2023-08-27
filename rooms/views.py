import json

from django.shortcuts import render
from rest_framework.response import Response

from .models import Hotel, Room, Book
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import HotelSerializer, RoomSerializer
from rest_framework.decorators import action
from datetime import datetime

from django_celery_beat.models import PeriodicTask, IntervalSchedule


# Просмотр отелей и номеров
# Поиск отелей
# Бронирование номеров


class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated, ]


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request, *args, **kwargs):

        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['POST'])
    def book(self, request, pk=None):
        room = self.get_object()
        date_finish = request.POST['date_finish']
        date_finish = datetime.strptime(date_finish, "%d/%m/%Y %H:%M")

        book = Book.objects.create(
            owner = request.user,
            room = room,
            date_finish = date_finish
        )

        schedule = IntervalSchedule.objects.create(
            every=50, period=IntervalSchedule.SECONDS
        )

        task = PeriodicTask.objects.filter(name="Моя первая таска").last()

        if task is not None:
            print("Такая таска уже есть, удаляю и создаю новую")
            task.delete()

        task_body = {
            "book_id": book.id
        }

        PeriodicTask.objects.create(
            name=f"Моя первая таска",
            task="delete_book_room",
            interval=schedule,
            one_off=True,
            kwargs=json.dumps(task_body)
        )
        return Response(data={"Бронь": "Успешно забронирована!"})