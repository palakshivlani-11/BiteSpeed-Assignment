from rest_framework import serializers

class getDataSerializer(serializers.Serializer):
    email = serializers.CharField()
    phonenumber = serializers.CharField()