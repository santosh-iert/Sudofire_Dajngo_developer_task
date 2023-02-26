from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, CustomerSerializer
from .models import User


class CustomerCreateAPIView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data.get("user"))
        customer_data = {
            "user": request.data.get("user"),
            "profile_number": request.data.get("profile_number")
        }
        if User.objects.filter(email=request.data.get("user").get('email')).exists():
            return Response({'error': 'Email already exists ! Please Use another email'},
                            status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(mobile=request.data.get("user").get('mobile')).exists():
            return Response({'error': 'Mobile number already exists ! Please Use another '},
                            status=status.HTTP_400_BAD_REQUEST)
        customer_serializer = CustomerSerializer(data=customer_data)
        if user_serializer.is_valid() and customer_serializer.is_valid():
            user = user_serializer.save()
            customer = customer_serializer.save(user=user)
            return Response(CustomerSerializer(customer).data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid data. '}, status=status.HTTP_400_BAD_REQUEST)
