import email
import imp
from .models import user
from rest_framework.decorators import api_view, permission_classes,APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.auth import AuthToken, TokenAuthentication
from .serializers import RegisterSerializer

#

#

def serialize_user(user1):
    return {
        "name": user1.name,
        "email": user1.email,
        "number": user1.number,
        "company_or_indvidual":user1.company_or_indvidual,
        #"standard_or_custom":user1.standard_or_custom,
        # "is_verified":user1.is_verified,
        # "last_name": user.last_name
    }

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def login(request):  
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user_instance = serializer.validated_data['user']
    # print(email.__dict__)
    token = Token.objects.get(user=user_instance)
    return Response({
        'user_data': serialize_user(user_instance),
        'token': token.key
    })
        

@api_view(['POST'])
def register(request):
    print("This is data")
    data=request.data
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # print("before")
        # print(user)
        # print("After")
        token = Token.objects.create(user=user)
        # print(token.__dict__)
        
        return Response({
            "user_info": serialize_user(user),
            "token": token.key
        })


@api_view(['GET'])
def get_user(request):
    var_token=request.META.get("HTTP_AUTHORIZATION")
    if not var_token:
        return Response({"Response":"Provide Auth Token"})
    auth_token_list=var_token.split(" ")
    print(auth_token_list)   
    if len(auth_token_list)<3:
        return Response({"Response":"Provide Auth Token in ,Bearer token format with key word \"Token\""})
    #print(x[2])
    print(var_token)
    user_id=Token.objects.filter(key=auth_token_list[2]).values_list("user",flat=True)
    # user_id=int(user_id[0])
    print(user_id)
    print("Print One im here")
    if not user_id:
        return Response({"Response":"User Not authenticate"})
    user_id=int(user_id[0])
    if user.objects.filter(id=user_id).exists():
        print("Print two")
        user_instance=user.objects.get(id=user_id)
        # print(request.headers)
        # user = request.user
        # if user.is_authenticated:
        return Response({
                'user_data': serialize_user(user_instance)
            })
    else:
        return Response({"Response":"User Not authenticate"})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)     
    def get(self, request):
        content = {'message': 'Hello, World! Get'}
        return Response(content)

    def post(self, request):
        content = {'message': 'Hello, World! Post'}
        return Response(content)