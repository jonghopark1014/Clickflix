# django
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404

# Rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permisison Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Local 
from .serializers import ReviewListSerializer, ReviewSerializer,CommentSerializer, MachineSerializer, FamouslineSerializer 
from .models import Review, Comment, MachineComment, FamousLine
from movies.models import Movie

# Create your views here.

# Review List
@api_view(['GET'])
def review_list(request):  
    if request.method == 'GET':  
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

# Review Like
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_like(request, review_pk):  
    if request.method == 'POST':  
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():  
            review.like_users.remove(user)
            is_liked = False
        else:  
            review.like_users.add(user)
            is_liked = True
        context = {
            'is_liked' : is_liked,
            'like_count' : review.like_users.count()
        }
        return JsonResponse(context)

# Review Create
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):  
    print(1)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':  
        print(2)
        serializer = ReviewSerializer(data=request.data)
        print(3)
        if serializer.is_valid(raise_exception=True):  
            print(movie)
            serializer.save(movie = movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# Review Detail
@api_view(['GET'])
def review_detail(request, review_pk):  
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':  
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

# Update, Delete
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_detail_edit(request, review_pk):  
    review = get_object_or_404(Review, pk=review_pk)

    # Review Update
    if request.method == 'PUT':  
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):  
            serializer.save()
            return Response(serializer.data)
    
    # Review Delete
    elif request.method == 'DELETE':  
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Comment Like
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_like(request, comment_pk):  
    if request.method == 'POST':  
        comment = get_object_or_404(Comment, pk=comment_pk)
        user = request.user

        if comment.like_user.filter(pk=user.pk).exists():  
            comment.like_user.remove(user)
            is_liked = False
        else:  
            comment.like_user.add(user)
            is_liked = True
        context = {
            'is_liked' : is_liked,
            'like_count' : comment.like_user.count()
        }
        return JsonResponse(context)

# Comment Create
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, review_pk):  
    if request.method == 'POST':  
        review = get_object_or_404(Review, pk=review_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):  
            serializer.save(review=review, user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# Comment Update Delete
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_edit(request, comment_pk):  
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'DELETE':  
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':  
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):  
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def comment_list(request, review_pk):  
    comment = get_list_or_404(Comment, review=review_pk)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)

# Machine Comment List
@api_view(['GET'])
def machine_comment_list(request):  
    if request.method == 'GET':  
        machinecomments = get_list_or_404(MachineComment)
        serializer = MachineSerializer(machinecomments, many=True)
        return Response(serializer.data)

# Machine Comment Create
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def machine_comment_create(request, movie_pk):  
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MachineSerializer(data=request.data)
    if serializer.is_valid():  
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Machine Comment Edit, Delete
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def machine_comment_edit(request, machinecomment_pk):  
    machinecomment = get_object_or_404(MachineComment, pk=machinecomment_pk)

    # Machine Comment Edit
    if request.method == 'PUT':  
        serializer = MachineSerializer(machinecomment, data = request.data)
        if serializer.is_valid(raise_exception = True):  
            serializer.save()
            return Response(serializer.data)
    
    # Machine Comment Delete
    elif request.method == 'DELETE':  
        machinecomment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# FamousLine List
@api_view(['GET'])
def famousline_list(request):  
    if request.method == 'GET':  
        famousline = FamousLine.objects.all()
        serializer = FamouslineSerializer(famousline, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def famousline_info(request, famousline_pk):  
    if request.method == 'POST':  
        famousline = get_object_or_404(FamousLine, pk=famousline_pk)
        serializer = FamouslineSerializer(famousline)
        return Response(serializer.data)

# FamousLine Create
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def famousline_create(request, movie_pk):  
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = FamouslineSerializer(data=request.data)
    if serializer.is_valid():  
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def famousline_edit(request, famousline_pk):  
    famousline = get_object_or_404(FamousLine, pk=famousline_pk)

    # FamousLine Edit
    if request.method == 'PUT':  
        serializer = FamouslineSerializer(famousline, data = request.data)
        if serializer.is_valid(raise_exception=True):  
            serializer.save()
            return Response(serializer.data)

    # FamousLine Delete
    elif request.method == 'DELETE': 
        famousline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)