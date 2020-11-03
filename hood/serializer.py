from rest_framework import serializers
from .models import Business, Profile, NeighbourHood


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'location', 'user_avatar', 'neighbourhood')


class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighbourHood
        fields = ('name', 'centers')


class Business_centresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('centre_name', 'contact_info', 'emergency_service')
