from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import http.client
from .utils import *
# Create your views here.
# auth0authorization/views.py

from functools import wraps
import jwt
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests
from random import randint
import os
import tweepy
from dotenv import load_dotenv

from sillyHacks.settings import ACCESS_SECRET_TOKEN,API_SECRET_KEY, ACCESS_TOKEN ,API_KEY
def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]
    return token

def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope

def get_auth0_user_data(token):
    url = 'https://' + "dev-wbn8u07y.us.auth0.com" + '/userinfo'
    params = {'access_token': token}
    resp = requests.get(url, params)
    data = resp.json()
    return data

# auth0authorization/views.py

@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    token = get_token_auth_header(args[0])
    print(token)
    return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})


@api_view(['GET'])
def private(request):
    token = get_token_auth_header(request)
    payload=jwt_decode_token(token)
    print(get_auth0_user_data(token))
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})

# auth0authorization/views.py

@api_view(['GET'])
@requires_scope('read:messages')
def private_scoped(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})

@permission_classes([AllowAny])
class Register(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        twitterId=request.data.get('twitterId')
        data={
            "email":email,
            "password":password,
            "twitterId":twitterId
        }
        serializer=CustomUserSerializer(data=data)
        if serializer.is_valid():
            conn = http.client.HTTPSConnection("dev-wbn8u07y.us.auth0.com")

            payload = "{\"client_id\":\"Emzfbw5VmOG4ZJCXqmmlpxxRHsyf0clD\",\"audience\":\"https://sillyHacks/api\",\"connection\":\"Username-Password-Authentication\",\"email\":\""+email+"\",\"password\":\""+password+"\"}"

            headers = { 'content-type': "application/json" }

            conn.request("POST", "/dbconnections/signup", payload, headers)

            res = conn.getresponse()
            data = res.read()

            print(data.decode("utf-8"))
            result=data.decode("utf-8").replace("'",'"')
            # print(type(result))
            data = json.loads(result)
            try:
                if(data['statusCode']==400):
                    return Response(data={
                    "Type": "Error",
                    "Message": "Registration Failed",
                    "Data": None
                }, status=status.HTTP_400_BAD_REQUEST)
            except:
                serializer.save()
                dic = {
                    "Type": "Success",
                    "Message": "Registered Successfully"
                }
                return Response(data=dic, status=status.HTTP_201_CREATED)

@permission_classes([AllowAny])
class Login(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        conn = http.client.HTTPSConnection("dev-wbn8u07y.us.auth0.com")

        payload = "{\"grant_type\":\"password\",\"client_id\":\"Emzfbw5VmOG4ZJCXqmmlpxxRHsyf0clD\",\"client_secret\":\"6qYhEG569aBbVpgzbC4d4FGMJv8yNkcPcYa0mKgG9sghV3nmEYRfCYCxnERj-aVn\",\"audience\":\"https://sillyHacks/api\",\"scope\":\"openid profile email address phone\",\"username\":\""+email+"\",\"password\":\""+password+"\"}"
        # print(payload)
        headers = { 'content-type': "application/json"}

        conn.request("POST", "/oauth/token", payload, headers)

        res = conn.getresponse()
        # print(res)
        data = res.read()
        # print(data)
        # print(type(data))
        result=data.decode("utf-8").replace("'",'"')
        # print(type(result))
        data = json.loads(result)
        # s = json.dumps(data, indent=4, sort_keys=True)
        # print(type(s))
        try:
            if data["access_token"]:
                dic = {
                    "Type": "Success",
                    "Message": "Login Successfully",
                    "Data":data
                }
                return Response(data=dic, status=status.HTTP_200_OK)
        except:
            return Response(data={
                    "Type": "Error",
                    "Message": "Login Failed",
                    "Data": None
                }, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
class getThought(APIView):
    def get(self,request):
        count= Thought.objects.all().count()
        randomNum=randint(1,count)
        thoughtObj=Thought.objects.get(id=randomNum)
        if thoughtObj.thought!="":
                dic = {
                    "Type": "Success",
                    "Message": "Thought obtained",
                    "Data": thoughtObj.thought
                }
                return Response(data=dic, status=status.HTTP_200_OK)
        else:
            return Response(data={
                    "Type": "Error",
                    "Message": "Not valid request",
                    "Data": None
                }, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
class getImage(APIView):
    def get(self,request):
        count= Image.objects.all().count()
        randomNum=randint(1,count)
        ImageObj=Image.objects.get(id=randomNum)
        if ImageObj.image!="":
                dic = {
                    "Type": "Success",
                    "Message": "Image obtained",
                    "Data": ImageObj.image
                }
                return Response(data=dic, status=status.HTTP_200_OK)
        else:
            return Response(data={
                    "Type": "Error",
                    "Message": "Not valid request",
                    "Data": None
                }, status=status.HTTP_400_BAD_REQUEST)              


@permission_classes([AllowAny])
class Twitterbot(APIView):
    def post(self,request):
        # twitterId=request.data.get('twitterId')
        load_dotenv(verbose=True)

        auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET_TOKEN)


        #api = tweepy.API(auth)
        api = tweepy.API(auth, wait_on_rate_limit=True,
            wait_on_rate_limit_notify=True)
        num=0
        allAccounts=CustomUser.objects.all()
        print(len(allAccounts))
        for account in allAccounts:
            twitterId=account.twitterId
            print("l",twitterId)
            if twitterId!=None:
                user = api.get_user(twitterId)
                print("User details:")
                print(user.id)
                print(user.name)
                print(user.description)
                print(user.location)

                count=Thought.objects.all().count()
                randomNum=randint(1,count)
                thoughtObj=Thought.objects.get(id=randomNum)
                direct_mssg = api.send_direct_message(user.id,thoughtObj.thought)
                num+=1
                print(direct_mssg.message_create['message_data']['text'])
            else:
                continue
        try:
            api.verify_credentials()
            #api.update_status("Test tweet from my twitter bot")
            print("Authentication OK")
            dic = {
                    "Type": "Success",
                    "Message": "Authentication OK",
                    "Data": num
                }
            return Response(data=dic, status=status.HTTP_200_OK)
        except:
            print("Error during authentication")
            return Response(data={
                    "Type": "Error",
                    "Message": "Error during Authentication",
                    "Data": None
                }, status=status.HTTP_400_BAD_REQUEST)


        


