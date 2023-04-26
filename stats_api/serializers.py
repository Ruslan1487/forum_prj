from rest_framework import serializers

from .models import (UserStatBlock, DetailedStatBlock, GeneralStatBlock)

class UserStatBlockSerializer(serializers.ModelSerializer):
    """
        UserStatBlock Serializer
    """
    class Meta:
        model = UserStatBlock
        fields = '__all__'

class DetailedStatBlockSerializer(serializers.ModelSerializer):
    """
        DetailedStatBlock Serializer
    """
    class Meta:
        model = DetailedStatBlock
        fields = '__all__'

class GeneralStatBlockSerializer(serializers.ModelSerializer):
    """
        GeneralStatBlock Serializer
    """
    class Meta:
        model = GeneralStatBlock
        fields = '__all__'