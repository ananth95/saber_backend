from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^redirect',views.redirect),
	url(r'^$',views.home),
]