from django.conf.urls import url
from appname.views import home

urlpatterns = [
     url(r"^$", home, name="home"),
]
