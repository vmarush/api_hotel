from rest_framework.routers import SimpleRouter
from .views import HotelViewSet,RoomViewSet

router = SimpleRouter()
router.register("hotels", HotelViewSet)
router.register("rooms",RoomViewSet)
urlpatterns = router.urls
