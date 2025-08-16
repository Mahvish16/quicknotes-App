from .models import RegisterUser
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = RegisterUser
        fields = ('name', 'email', 'password')
    def create(self, validated_data):
        user = RegisterUser.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        return user
    


