from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from community.serializers import ReviewSerializer
from movies.models import Movie
from community.models import Review

class CustomRegisterSerializer(RegisterSerializer):  
    birthday = serializers.DateField(required=True, write_only=True)
    nickname = serializers.CharField(write_only=True, required=True, max_length=100)
 
    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()
        cleaned_data['nickname'] = self.validated_data.get('nickname', '')
        cleaned_data['birthday'] = self.validated_data.get('birthday', '')
        return cleaned_data

class CustomProfileSerializer(serializers.ModelSerializer):  

    class ReviewSerializer(serializers.ModelSerializer):  

        class Meta:  
            model = Review
            fields = '__all__'

    review_user = ReviewSerializer(many=True, read_only=True)

    class movielike(serializers.ModelSerializer):  

        class Meta:  
            model = Movie
            fields = '__all__'
    
    like_movie = movielike(many=True, read_only=True)

    class wishmovie(serializers.ModelSerializer):  

        class Meta:  
            model = Movie
            fields = '__all__'

    wish_movie = wishmovie(many=True, read_only=True)

    class watchedmovie(serializers.ModelSerializer):  

        class Meta:  
            model = Movie
            fields = '__all__'
    
    watched_movie = watchedmovie(many=True, read_only=True)

    class followersserial(serializers.ModelSerializer):  

        class Meta:  
            model = get_user_model()
            fields = '__all__'
    
    followers = followersserial(many=True, read_only=True)

    class Meta:  
        model = get_user_model()
        fields = '__all__'