from rest_framework import serializers


class HelloSerializer(serializers.Serializer): #"S"erializer is a class
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)
