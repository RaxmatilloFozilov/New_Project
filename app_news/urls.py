from django.urls import path

from app_news.views import AddNewsView, ListNewsView, DetailNewsView, DeleteNewsView, UpdateNewsView , MessageFormView , CustomView

urlpatterns = [
    path('add/', AddNewsView.as_view(), name='add_news'),
    path('<int:pk>/', DetailNewsView.as_view(), name='show_news'),
    path('', ListNewsView.as_view(), name='list_news'),
    path('update/<int:pk>/', UpdateNewsView.as_view(), name='update_news'),
    path('delete/<int:pk>/', DeleteNewsView.as_view(), name='delete_news'),

    path('message/', MessageFormView.as_view(), name='message_form'),
    path('custom/', CustomView.as_view(), name='custom_view'),
]
