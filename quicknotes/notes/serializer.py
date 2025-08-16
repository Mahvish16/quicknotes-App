from .models import RegisterUser,Notes
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
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 100)
    password = serializers.CharField(max_length=200, write_only=True)

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('id','user','title', 'description')


