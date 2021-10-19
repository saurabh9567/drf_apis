from django.urls import include, path
from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]