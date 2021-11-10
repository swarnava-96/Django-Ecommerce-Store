from rest_framework import serializers
from . models import Users, profile

class UsersSerializer(serializers.ModelSerializer):
    # For put meathod
    employee_id = serializers.CharField(required = False)
    name = serializers.CharField(required = False)
    ranking = serializers.FloatField(required = False)

    class Meta:
        model = Users
        #fields = ('name', 'employee_id')
        fields = '__all__'

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        #fields = ('name', 'employee_id')
        fields = '__all__'
