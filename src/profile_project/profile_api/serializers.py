from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
	"""se a name field for testion API"""

	name = serializers.CharField(max_length=10)

