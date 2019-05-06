from rest_framework import serializers


#Profile_api
from . import models

class HelloSerializer(serializers.Serializer):
	"""se a name field for testion API"""

	name = serializers.CharField(max_length=10)

#profile_api
class UserProfileSerializer(serializers.ModelSerializer):
	"""profile Object. """
	class Meta:
		#assign model
		model =  models.UserProfile
		fields =  ('id','email','name','password')
		extra_kwargs = {'password':{'write_only':True}}


	def create(self,validated_data):

		"""create and return new user."""

		user = models.UserProfile(
			email =validated_data['email'],
			name = validated_data['name']
			)

		user.set_password(validated_data['password'])
		user.save()


		return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
	""" feed Items"""
	class Meta:
		model = models.ProfileFeedItem
		fields = ('id','user_profile','status_text','create_on')
		extra_kwargs = {'user_profile':{'read_only':True}}





