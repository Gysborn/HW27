from rest_framework.permissions import BasePermission


class IsAdOwnerOrStaff(BasePermission):
    message = "For access, you must be the owner or moderator"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in ["admin", "moderator"]:
            return True
        return False
