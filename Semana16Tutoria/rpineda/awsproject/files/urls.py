from rest_framework.routers import SimpleRouter
from .views import ClienteViewset
router = SimpleRouter()
router.register('cliente', ClienteViewset)
urlpatterns = router.urls