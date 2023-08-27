from celery import shared_task
from rooms.models import Book


@shared_task(name="delete_book_room")
def delete_book_room(*args, **kwargs):
    book_id = kwargs['book_id']
    book = Book.objects.get(id=book_id)

    print("Освобождаю комнату")
    book.room.is_booked = False
    book.room.save()

    print("удаляю запись о бронировании")
    book.delete()