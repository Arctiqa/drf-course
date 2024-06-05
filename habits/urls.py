from habits.apps import HabitsConfig
from django.urls import path

from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIVIew, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habits/list/', HabitListAPIView.as_view(), name='habit_list'),

    path('habits/<int:pk>/detail/', HabitRetrieveAPIVIew.as_view(), name='habit_detail'),
    path('habits/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habits/<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]
