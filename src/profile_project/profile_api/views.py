from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response


#Serializers 
from . import serializers
from rest_framework import status


#profile
from . import models

# VIEWSET
from rest_framework import viewsets

# Create your views here.


class HelloApiView(APIView):
	"""test api"""

	serializer_class = serializers.HelloSerializer	

	def get(self,request, format = None):
		"""resturn a list of api features. """
		an_apiview = [
			'use Htp (get, post, patch, put, delet',
			'it is similar to a traditional Django view',
			'give you the most control over your logic',
			'is mapped manually to urls'

		]

		return Response({'message ': 'Hello', 'an_apiview': an_apiview})

	def post(self,request):
		"""create a hello message with our name """

		serializer = serializers.HelloSerializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'hello {0}'.format(name)
			return Response({'message':message})
		else :
			return Response(
				serializer.errors, status = status.HTTP_400_BAD_REQUEST)


	def put(self,request, pk = None):

		"""handeling updating

		pk is primary key this is for hadneling data	"""
		return Response({'method':'put'})


	def patch(self,request, pk=None):
		""" for updating data"""
		return Response({'method':'patch'})

	def delete(self, response, pk=None):

		"""delet an object"""

		return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
	"""Test ViewsSet"""
	

	serializer_class = serializers.HelloSerializer

	def list(self,request):
		""" Return a hello message """

		a_viewset = [
			'use parial',
			'automaticly user urls',
			'provides more fucnationaly with less code',
		]

		return Response({'message':'Hello','a_viewset':a_viewset})


	def create(self,request):

		"""Create a new hello messgae"""

		serializer = serializers.HelloSerializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'hello {0}'.format(name)
			return Response({'message':message})

		else: 
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )


	def retrieve(self,request,pk =None):

		"""handeles getting an object"""

		return Response({'http_method':'GET'})


	def update(self, request, pk=None):
		"""pk none because we want to know wich objecting is updating"""
		return Response({'http_method':'PUT'})	

	def partial_update(self,request,pk=None):

		"""Handles updating part of an object"""

		return  Response({'http_method':'PATCH'})

	def destroy(self, request, pk=None):

		"""handels removing"""

		return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
	""" Handels creating and updating profiles"""
	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.object.all()
























