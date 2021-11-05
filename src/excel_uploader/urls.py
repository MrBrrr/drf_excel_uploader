from django.urls import path, include
from rest_framework import routers

from excel_uploader.views import UploaderView


router = routers.DefaultRouter()
router.register(prefix="upload", viewset=UploaderView, basename="upload")

urlpatterns = [
    path('', include(router.urls))
]
