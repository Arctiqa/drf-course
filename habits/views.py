from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """Вывод списка привычек"""
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner, )
    pagination_class = HabitsPaginator

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            queryset = Habit.objects.filter(user=user)
        else:
            queryset = Habit.objects.all()
        return queryset


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, )

    # def perform_create(self, serializer):
    #     new_habit = serializer.save()
    #     new_habit.user = self.request.user
    #     new_habit.save()



class HabitRetrieveAPIVIew(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner, )


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner, )


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner, )
