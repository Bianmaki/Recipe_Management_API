from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only recipe owners to edit/delete them.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions: allow GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions: only the owner can edit/delete
        return obj.user == request.user
