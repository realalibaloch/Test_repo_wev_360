#from django.contrib.auth.models import user
from .models import user
from django.forms import CharField
from numpy import number
from rest_framework import serializers, validators
from rest_framework import serializers
#from django.contrib.auth.models import user
#"is_verified","is_standard","is_custom","is_indvidual","is_company"
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ("name", "password", "email", "number","company_or_indvidual")
        extra_kwargs = {
            "company_or_indvidual":{ "required": True,
            },
            "number":{ "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        user.objects.all(), f"A user with that number already exists."
                    )
                ],},
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        user.objects.all(), f"A user with that Email already exists."
                    )
                ],
            },
        }

    def create(self, validated_data):
        user1 = user.objects.create_user(
            name=validated_data["name"],
            email=validated_data["email"],
            password=validated_data["password"],
            number=validated_data["number"],
            company_or_indvidual=validated_data["company_or_indvidual"]
            #is_verified=validated_data["is_verified"],
            
        )
        return user1












"""
"is_standard":{ "required": True,
                "validators": [
                    validators.UniqueValidator(
                        user.objects.all(), f"A user with that Email already exists."
                    )
                ],},
            "is_custom":{ "required": True,
                "validators": [
                    validators.UniqueValidator(
                        user.objects.all(), f"A user with that Email already exists."
                    )
                ],},
            "is_indvidual":{ "required": True,
                "validators": [
                    validators.UniqueValidator(
                        user.objects.all(), f"A user with that Email already exists."
                    )
                ],},
            "is_company":{ "required": True,
                "validators": [
                    validators.UniqueValidator(
                        user.objects.all(), f"A user with that Email already exists."
                    )
                ],},


    create
    
"""