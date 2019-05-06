from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
	""" allow user update status"""
	def has_object_permission(self,request,view,obj):

		"""check the user want to update status"""
		if request.method in permissions.SAFE_METHODS:
			return True

        #check the user is the user
		return obj.user_profile.id == request.user.id