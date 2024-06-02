from rest_framework.exceptions import ValidationError


class RelatedOrRewardCheck:
    """Может быть либо связанная привычка, либо награда"""
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        if value.get(self.field1) and value.get(self.field2):
            raise ValidationError('Может быть либо связанная привычка, либо награда')


class CompletionTimeCheck:
    """Время выполнения привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get(self.field) >= 120:
            raise ValidationError('Время выполнения привычки не должно превышать 2 минуты')


class OnlyPleasantInRelatedHabits:
    """В связанных привычках могут быть только приятные привычки"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if not value.get(self.field):
            raise ValidationError('В связанных привычках могут быть только приятные привычки')


class NoRewardOrRelatedForPleasantHabit:
    """У приятной привычки не может быть вознаграждения или связанной привычки."""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        if value.get(self.field1) and value.get(self.field2):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class HabitTimeCheck:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней."""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if not 1 <= value.get(self.field) <= 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
