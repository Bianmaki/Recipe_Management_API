from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow admins to edit objects, others can only read.
    """
    def has_permission(self, request, view):
        # SAFE_METHODS are GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only admins can POST, PUT, DELETE
        return request.user and request.user.is_staff


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only the owner of an object can edit/delete it.
    Others can only read.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE methods = GET, HEAD, OPTIONS → allow for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise, only the owner can modify
        return obj.user == request.user
