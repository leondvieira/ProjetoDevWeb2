from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
        Custom permission to allow owner of an object to edit it
    """
    
    def has_object_permission(self, request, view, obj):
        return obj.usuario == request.user
