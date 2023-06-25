from django.urls import path
from . import views
from django.urls.resolvers import URLPattern

urlpatterns=[
    path('',views.home),
    path('logout',views.logout_view),
]