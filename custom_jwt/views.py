from django.shortcuts import render

# Create your views here.

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenRefreshView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        # data["refresh"] = str(refresh)
        # data["access"] = str(refresh.access_token)

        # add new key for following the rules
        data["refresh_token"] = str(refresh)
        data["access_token"] = str(refresh.access_token)

        # delete original key
        del data["refresh"]
        del data["access"]

        # Add extra responses here
        data["username"] = self.user.username
        data["groups"] = self.user.groups.values_list("name", flat=True)

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):

        data = super().validate(attrs)
        # add `access_token`
        data["access_token"] = data.get("access")

        # delete original key
        del data["access"]
        return data


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer
