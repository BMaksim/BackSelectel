from rest_framework import serializers
from retros.models import Users, Session


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'password']


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'payers', 'oneword', 'aff_pain', 'pigs']