from rest_framework.permissions import BasePermission

class AuthorPermissionsClass(BasePermission):
    def has_object_permission(self, request, view, obj):
        #print(obj.owner)          #для отладки
        if request.user == obj.author:
            return request.method in ('GET', 'PUT', 'PATH', 'DELETE')
        else:
            return False
