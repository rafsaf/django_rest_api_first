from django.urls import path, include

from rest_framework.routers import DefaultRouter

import books.views as views

app_name = 'books'

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('',include(router.urls))
]


