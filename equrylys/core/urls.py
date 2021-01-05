from django.urls import path
from core import views
from rest_framework import routers
from core.views import SdachaViewSet, TalonViewSet, ZakazchikViewSet, GeneralnyiViewSet, SubpodryadnyeViewSet, GeneralViewSet, OrgViewSet, GotovnostViewSet, \
calendarViewSet, sostoyanieViewSet, soderzhanieViewSet, ITRViewSet, izmenenieViewSet, vydannieViewSet, expertViewSet, primichanieViewSet

router = routers.DefaultRouter()
router.register("Sdacha", SdachaViewSet, basename='SdachaViewSet')
router.register("Talon", TalonViewSet, basename='Talon')
router.register("Zakazchik", ZakazchikViewSet, basename='Zakazchik')
router.register("Generalnyi", GeneralnyiViewSet, basename='Generalnyi')
router.register("Subpodryadnye", SubpodryadnyeViewSet, basename='Subpodryadnye')
router.register("General", GeneralViewSet, basename='General')
router.register("Org", OrgViewSet, basename='Org')
router.register("Gotovnost", GotovnostViewSet, basename='Gotovnost')
router.register("CalendarV", calendarViewSet, basename='CalendarV')
router.register("Sostoyanie", sostoyanieViewSet, basename='Sostoyanie')
router.register("Soderzhanie", soderzhanieViewSet, basename='Soderzhanie')
router.register("ITR", ITRViewSet, basename='ITR')
router.register("Izmenenie", izmenenieViewSet, basename='Izmenenie')
router.register("Vydannie", vydannieViewSet, basename='Vydannie')
router.register("Primichanie", primichanieViewSet, basename='Primichanie')


urlpatterns = router.urls
