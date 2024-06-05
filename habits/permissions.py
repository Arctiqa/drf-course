from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Вы не владелец привычки"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsModOrOwner(BasePermission):
    message = "У вас нет доступа к этой учетной записи"

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.pk or request.user.groups.filter(name='moderator').exists()
