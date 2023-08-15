from rest_framework import serializers
from .models import Genre, Actor, Keyword, Provider, Movie, Actorcharacter, Actorasknown
from community.models import Review, MachineComment, FamousLine
from accounts.models import User

#----------------ManyToMany-----------------------#

class GenreSerializer(serializers.ModelSerializer):  

    class Meta:  
        model = Genre
        fields = ('name',)

class ActorSerializer(serializers.ModelSerializer):  

    class Meta:  
        model = Actor
        fields = ('name',)

class KeywordSerializer(serializers.ModelSerializer):  

    class Meta:  
        model = Keyword
        fields = ('name',)

class ProviderSerializer(serializers.ModelSerializer):  

    class Meta:  
        model = Provider
        fields = '__all__'

class characterserial(serializers.ModelSerializer):  

    class Meta:  
        model = Actorcharacter
        fields = ('character',)
        
class asknownserial(serializers.ModelSerializer):  

    class Meta:  
        model = Actorasknown
        fields = ('asknown',)

class ActorAll(serializers.ModelSerializer):  
    
    actorcharacter_set = characterserial(many=True, read_only=True)

    actorasknown_set = asknownserial(many=True, read_only=True)

    class Meta:  
        model = Actor
        fields = ('actorcharacter_set', 'actorasknown_set', 'name',)

#-------------------main/movie----------------------#
class MovieSearschList(serializers.ModelSerializer):  
    genres = GenreSerializer(many=True, read_only= True)
    
    actors = ActorAll(many=True, read_only=True)

    class Meta:  
        model = Movie
        fields = ('id', 'title', 'poster_path', 'genres', 'actors', )
    

class MovieListSerializer(serializers.ModelSerializer):  
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:  
        model = Movie
        fields = ('id', 'title', 'release_date', 'runtime', 'poster_path', 'youtube_key', 'genres', 'backdrop_path', 'actors')

class MovieSerializer(serializers.ModelSerializer):  
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    keywords = KeywordSerializer(many=True, read_only=True)
    providers = ProviderSerializer(many=True, read_only=True)

    class ReviewSerializer(serializers.ModelSerializer):  

        class Meta:  
            model = Review
            fields = ('title', 'point','user', 'content')

    review_set = ReviewSerializer(many=True, read_only=True)
    
    class FamousLineSerializer(serializers.ModelSerializer):  

        class Meta:  
            model = FamousLine
            fields = '__all__'

    famousline_set = FamousLineSerializer(many=True, read_only=True)

    class Meta:  
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users',)
    
    