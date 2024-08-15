from django.urls import path
from . import views

app_name = 'book-urls'
urlpatterns = [
    path('book/<str:isbn>', views.book_detail, name='book-detail' ),
    path('book/post/', views.book_post, name='book-post')
]