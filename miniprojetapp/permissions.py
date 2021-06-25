from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Les permissions de lecture seule sont autorisées pour toute demande.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
