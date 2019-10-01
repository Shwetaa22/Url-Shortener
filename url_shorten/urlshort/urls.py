from django.conf.urls import url
from .views import customUrl,newshorturl


urlpatterns = [
    url(r'original-url', customUrl, name="original-url"),
    url(r'short-url', newshorturl, name="short-url"),
]
