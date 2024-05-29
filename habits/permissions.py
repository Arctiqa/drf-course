from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Вы не владелец привычки"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
