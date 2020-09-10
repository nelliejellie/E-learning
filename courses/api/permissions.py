from rest_framework.permissions import BasePermission

class IsEnrolled(BasePermission):
    #function that checks if a user exists or enrolled for a course
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()