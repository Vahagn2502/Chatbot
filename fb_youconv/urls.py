from django.conf.urls import include, url
from .views import YouConvView

urlpatterns = [
    url(r'^0bca8e3cb1efd4d736b674d436145dea9ac7c864b95b66ab76/?$', YouConvView.as_view())
    ]