from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_lottery', views.save_lottery, name='save_lottery'),
    path('lottery_list', views.lottery_list, name='lottery_list'),
    path('lottery_result', views.lottery_result, name='lottery_result'),
]
