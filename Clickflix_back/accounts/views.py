from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import CustomProfileSerializer

# Create your views here.
@api_view(['POST'])
def follow(request, user_pk):  
    User = get_user_model()
    me = request.user
    you = User.objects.get(pk=user_pk)
    if me != you:  
        if me.followings.filter(pk=you.pk).exists():  
            me.followings.remove(you)
            is_followed = False
            print(1)
        else:  
            me.followings.add(you)
            is_followed = True
            print(2)
        context = {
            'is_followed' : is_followed,
            'followers_count' : you.followers.count(),
            'follwings_count' : you.followings.count(),
        }
        return JsonResponse(context)

@api_view(['GET'])
def anotherinfo(request, user_pk):  
    if request.method == 'GET':  
        another = User.objects.get(pk=user_pk)
        serializer = CustomProfileSerializer(another)
        return Response(serializer.data)