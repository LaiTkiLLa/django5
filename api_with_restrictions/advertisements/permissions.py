from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):

   def has_object_permission(self, request, view, obj):
        if obj.creator == request.user:
            return True
        if request.user.is_superuser:
            return True
        return False
