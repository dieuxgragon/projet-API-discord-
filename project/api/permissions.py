from rest_framework import permissions
from .models import Membership

class IsServerMember(permissions.BasePermission):
    """
    Permission: user must be a member of the server to perform action (e.g. post message)
    Expects 'server' in request.data or view.kwargs (depends on endpoint)
    """

    def has_permission(self, request, view):
        # For listing messages (server in URL), check kwargs
        server_id = view.kwargs.get("server_pk") or request.data.get("server")
        if not server_id:
            return True  # let other validators decide
        user = request.user
        return Membership.objects.filter(user=user, server_id=server_id).exists()

class IsServerOwnerOrRoleCanManage(permissions.BasePermission):
    """
    Only server owner or member with role.can_manage_roles can manage roles/members
    expects 'server_pk' in kwargs or server id in data
    """

    def has_permission(self, request, view):
        server_id = view.kwargs.get("server_pk") or request.data.get("server")
        if not server_id:
            return False
        user = request.user
        from .models import Server
        try:
            server = Server.objects.get(pk=server_id)
        except Server.DoesNotExist:
            return False
        if server.owner_id == user.id:
            return True
        # check member roles
        from .models import Membership
        try:
            membership = Membership.objects.get(user=user, server=server)
        except Membership.DoesNotExist:
            return False
        return membership.roles.filter(can_manage_roles=True).exists()
