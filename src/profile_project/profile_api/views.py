from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class HelloApiView(APIView):
	"""test api"""

	def get(self,request, format = None):
		"""resturn a list of api features. """
		an_apiview = [
			'use Htp (get, post, patch, put, delet',
			'it is similar to a traditional Django view',
			'give you the most control over your logic',
			'is mapped manually to urls'

		]

		return Response({'message ': 'Hello', 'an_apiview': an_apiview})