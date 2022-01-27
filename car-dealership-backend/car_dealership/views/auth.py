from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from car_dealership.serializers.client import ClientSerializer


# view to register the client
class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)

        if serializer.is_valid():
            if "password" not in serializer.validated_data:
                response = {
                    "error": "Password required for creating account",
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

            # registers the client
            client = serializer.save()

            # logs the client in
            login(request, client)

            response = {
                "success": "Logged successfully",
                "client": serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)

        response = {
            "error": "Bad request: " + str(serializer.errors),
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


# view for client login
class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        email = request.data.get("email")
        password = request.data.get("password")

        client = authenticate(request, email=email, password=password)

        if client is not None:
            # logs the client in
            login(request, client)

            response = {
                "success": "Logged successfully",
                "client": ClientSerializer(client),
            }
            return Response(response, status=status.HTTP_200_OK)

        response = {
            "error": "Bad request",
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


# view to logout the client
class Logout(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # logs the client out
        logout(request)

        response = {
            "success": "Logged out successfully",
        }
        return Response(response, status=status.HTTP_200_OK)
