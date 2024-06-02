from rest_framework import serializers

from habits.models import Habit
from habits.validators import RelatedOrRewardCheck, CompletionTimeCheck, HabitTimeCheck, \
    NoRewardOrRelatedForPleasantHabit, OnlyPleasantInRelatedHabits


class HabitSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedOrRewardCheck(field1='related_habit', field2='reward'),
            CompletionTimeCheck(field='expected_completion_time'),
            OnlyPleasantInRelatedHabits(field='is_pleasant'),
            NoRewardOrRelatedForPleasantHabit(field1='is_pleasant', field2='reward'),
            HabitTimeCheck(field='periodicity')
        ]
