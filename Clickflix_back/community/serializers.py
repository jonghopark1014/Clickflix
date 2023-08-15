from rest_framework import serializers
from movies.models import Genre, Actor, Keyword, Provider, Movie
from .models import Review, Comment, MachineComment, FamousLine
from accounts.models import User
from django.contrib.auth import get_user_model

#---------------need movie serializer ----------#
class movietitle(serializers.ModelSerializer):  
    
    class Meta:  
        model = Movie
        fields = ('title', )

#---------------comment----------------#
class CommentSerializer(serializers.ModelSerializer):  
    user = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:  
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'user', 'like_users')

#---------------Review------------------#
class ReviewListSerializer(serializers.ModelSerializer):  
    movie = serializers.CharField(source='movie.title', read_only=True)
    user = serializers.CharField(source='user.nickname', read_only=True)
    
    class Meta:  
        model = Review
        fields = '__all__'
    
class ReviewSerializer(serializers.ModelSerializer):  
    comment_set = CommentSerializer(many=True, read_only=True)
    movie = serializers.CharField(source='movie.title', read_only=True)
    class userSerial(serializers.ModelSerializer):  

        class Meta:  
            model = User
            fields = '__all__'
    user = userSerial(read_only=True)

    class Meta:  
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie', 'like_users')

#---------------Machine ----------------#
class MachineSerializer(serializers.ModelSerializer):  

    movie = serializers.CharField(source='movie.title', read_only=True)

    class Meta:  
        model = MachineComment
        fields = '__all__'

#---------------Famous Line-------------#

class FamouslineSerializer(serializers.ModelSerializer):  

    movie = serializers.CharField(source='movie.title', read_only=True)

    class Meta:  
        model = FamousLine
        fields = '__all__'