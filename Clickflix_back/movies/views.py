# Python 
import random
from functools import cmp_to_key

# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer, MovieSearschList, ActorAll
from .models import Movie, LikeGenre, LikeKeyword, LikeActor
from django.contrib.auth import get_user_model
import datetime

# Create your views here.

# algorithm
def year_recommend():  
    tmp = [0, 0, 0, 0, 0]
    tmp_cnt1 = 0
    tmp_cnt2 = 0
    tmp_cnt3 = 0
    tmp_cnt4 = 0
    tmp_cnt5 = 0
    tmp1 = []
    tmp2 = []
    tmp3 = []
    tmp4 = []
    tmp5 = []
    movies = get_list_or_404(Movie.objects.order_by('-vote_average', '-vote_count', '-popularity'))
    for i in movies:  
        if int(str(i.release_date)[:4]) < 2000:  
            if tmp_cnt1 < 10:  
                tmp1.append(i)
                tmp_cnt1 += 1
        elif int(str(i.release_date)[:4]) < 2010:  
            if tmp_cnt2 < 10:  
                tmp2.append(i)
                tmp_cnt2 += 1
        elif int(str(i.release_date)[:4]) < 2015:  
            if tmp_cnt3 < 10:  
                tmp3.append(i)
                tmp_cnt3 += 1
        elif int(str(i.release_date)[:4]) < 2020:  
            if tmp_cnt4 < 10:  
                tmp4.append(i)
                tmp_cnt4 += 1
        elif 2020 <= int(str(i.release_date)[:4]):  
            if tmp_cnt5 < 10:  
                tmp5.append(i)
                tmp_cnt5 += 1

    idx = random.choice(range(0, len(tmp1)))
    tmp[0] = tmp1[idx]
    idx = random.choice(range(0, len(tmp2)))
    tmp[1] = tmp2[idx]
    idx = random.choice(range(0, len(tmp3)))
    tmp[2] = tmp3[idx]
    idx = random.choice(range(0, len(tmp4)))
    tmp[3] = tmp4[idx]
    idx = random.choice(range(0, len(tmp5)))
    tmp[4] = tmp5[idx]
    return tmp

# main page
@api_view(['GET'])
@permission_classes([AllowAny])
def recommend_anonymous(request):  
    if request.method == 'GET':  
        tmp = year_recommend()
        serializer = MovieListSerializer(tmp, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recommend_user(request, user_pk):  
    if request.method == 'POST':  
        user = get_object_or_404(get_user_model(), pk=user_pk)
        if user.point_genre != None and user.point_keyword != None:  
            if user.point_genre + user.point_keyword > 25:  
                genrelist = get_list_or_404(LikeGenre.objects.order_by('-point'), user=user)
                keywordlist = get_list_or_404(LikeKeyword.objects.order_by('-point'), user=user)
                actorlist = get_list_or_404(LikeActor.objects.order_by('-point'), user=user)
                tmp_genre = {}
                tmp_keyword = {}
                tmp_actor = {}
                if datetime.datetime.now().year - user.birthday.year + 1 > 19:  
                    print(datetime.datetime.now().year - user.birthday.year + 1)
                    tmp_movie_all = get_list_or_404(Movie.objects.order_by('-vote_average', '-popularity', '-vote_count'))
                else:  
                    tmp_movie_all = get_list_or_404(Movie.objects.order_by('-vote_average', '-vote_count', '-popularity'), adult=False)
                tmp_movie_point = [0] * len(tmp_movie_all)
                tmp_movie = []
                tmp_cnt = -1
                if len(genrelist) > 10:  
                    genrelist = genrelist[:10]
                for i in genrelist:  
                    tmp_genre[i.genre.name] = i.point
                for i in keywordlist:  
                    tmp_keyword[i.keyword.name] = i.point
                for i in actorlist:  
                    tmp_actor[i.actor.name] = i.point
                for i in tmp_movie_all:  
                    tmp_cnt += 1
                    for j in i.genres.all():  
                        if j.name in tmp_genre:  
                            tmp_movie_point[tmp_cnt] += tmp_genre[j.name]
                    for j in i.keywords.all():  
                        if j.name in tmp_keyword:  
                            if tmp_keyword[j.name] >= 3:  
                                tmp_movie_point[tmp_cnt] += tmp_keyword[j.name]
                    for j in i.actors.all():  
                        if j.name in tmp_actor:  
                            if tmp_actor[j.name] >= 3:  
                                tmp_movie_point[tmp_cnt] += tmp_actor[j.name]
                tmptmp_movie_all = []
                for i in range(len(tmp_movie_point)):  
                    tmptmp_movie_all.append([tmp_movie_all[i]] + [tmp_movie_point[i]])
                tmptmp_movie_all.sort(key = lambda x : x [1], reverse=True)
                print('---------------------1------------------')
                tmp_idx = random.sample(range(0, 15), 15)
                for i in range(15):  
                    tmp_movie.append(tmptmp_movie_all[tmp_idx[i]][0])
                print('---------------------2------------------')
                umm = genrelist[-1].genre 
                cnt = 0
                not_prefer = get_list_or_404(Movie.objects.order_by('-vote_average', '-popularity', '-vote_count', ), genres = umm)[:10]
                for i in not_prefer:  
                    if cnt == 10:  
                        break
                    if i not in tmp_movie:  
                        tmp_movie.append(i)
                        cnt += 1
                serializer = MovieListSerializer(tmp_movie, many=True)
                return Response(serializer.data)
            else:  
                tmp = year_recommend()
                serializer = MovieListSerializer(tmp, many=True)
                return Response(serializer.data)
        else:  
            tmp = year_recommend()
            serializer = MovieListSerializer(tmp, many=True)
            return Response(serializer.data)

# add_prefer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_prefer(request, movie_pk):  
    if request.method == 'POST':  
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        # 가중치 알고리즘
        for i in movie.genres.all():  
            print(i)
            if user.likegenre_set.filter(genre=i).count() > 0:  
                if movie not in user.likegenre_set.all().get(genre = i, user=user).check_movie.all():  
                    likegenre = user.likegenre_set.get(genre = i, user=user)
                    likegenre.point += 4
                    likegenre.check_movie.add(movie)
                    likegenre.save()
            else:  
                likegenre = LikeGenre.objects.create(
                    user = user,
                    genre = i,
                    point = 4,
                )
                likegenre.check_movie.add(movie)

        for i in movie.keywords.all():  
            print(i)
            if user.likekeyword_set.all().filter(keyword=i).count() >0:  
                if movie not in user.likekeyword_set.all().get(keyword = i, user=user).check_movie.all():  
                    likekeyword = user.likekeyword_set.all().get(keyword = i, user=user)
                    likekeyword.point += 1
                    likekeyword.check_movie.add(movie)
                    likekeyword.save()
            else:  
                likekeyword = LikeKeyword.objects.create(
                    user = user,
                    keyword = i,
                    point = 1
                )
                likekeyword.check_movie.add(movie)
        
        for i in movie.actors.all():  
            if user.likeactor_set.all().filter(actor=i.id).count > 0:  
                if movie not in user.likeactor_set.all().get(actor = i, user=user).check_movie.all():  
                    likeactor = user.likeactor_set.all().get(actor = i, user = user)
                    likeactor.point += 2
                    likeactor.check_movie.add(movie)
                    likeactor.save()
            else:  
                likeactor = LikeActor.objects.create(
                    user = user,
                    actor = i,
                    point = 2
                )
                likeactor.check_movie.add(movie)

        userpoint_genre = get_list_or_404(LikeGenre.objects.order_by('-point'), user=user)
        user.point_genre = userpoint_genre[0].point
        userpoint_keyword = get_list_or_404(LikeKeyword.objects.order_by('-point'), user=user)
        user.point_keyword = userpoint_keyword[0].point
        user.save()

# search movie page
@api_view(['GET'])
def movie_list(request):  
    if request.method =='GET':  
        movies = get_list_or_404(Movie)
        serializer = MovieSearschList(movies, many=True)
        return Response(serializer.data)

# Detail Modal page
@api_view(['GET'])
def movie_detail(request, movie_pk):  
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':  
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

# all-Random Recommend
@api_view(['GET'])
def all_random(request):  
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        idx = random.choice(range(0, len(movies)))
        randomPK = movies[idx].id
        movie = [get_object_or_404(Movie, pk=randomPK)]
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_pk):  
    if request.method == 'POST':  
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.like_users.filter(pk=user.pk).exists():  
            movie.like_users.remove(user)
            is_liked = False
        else:  
            movie.like_users.add(user)
            is_liked = True
        for i in movie.genres.all():  
            if user.likegenre_set.filter(genre=i).count() > 0:  
                if movie not in user.likegenre_set.all().get(genre = i, user=user).check_movie.all():  
                    likegenre = user.likegenre_set.get(genre = i, user=user)
                    likegenre.point += 4
                    likegenre.check_movie.add(movie)
                    likegenre.save()
            else:  
                likegenre = LikeGenre.objects.create(
                    user = user,
                    genre = i,
                    point = 4,
                )
                likegenre.check_movie.add(movie)

        # 가중치 알고리즘
        for i in movie.keywords.all():  
            if user.likekeyword_set.all().filter(keyword=i).count() >0:  
                if movie not in user.likekeyword_set.all().get(keyword = i, user=user).check_movie.all():  
                    likekeyword = user.likekeyword_set.all().get(keyword = i, user=user)
                    likekeyword.point += 1
                    likekeyword.check_movie.add(movie)
                    likekeyword.save()
            else:  
                likekeyword = LikeKeyword.objects.create(
                    user = user,
                    keyword = i,
                    point = 1
                )
                likekeyword.check_movie.add(movie)
        
        for i in movie.actors.all():  
            if user.likeactor_set.all().filter(actor = i).count() > 0:  
                print(i.id)
                if movie not in user.likeactor_set.all().get(actor = i.id, user=user).check_movie.all():  
                    likeactor = user.likeactor_set.all().get(actor = i.id, user = user)
                    likeactor.point += 2
                    likeactor.check_movie.add(movie)
                    likeactor.save()
            else:  
                likeactor = LikeActor.objects.create(
                    user = user,
                    actor = i,
                    point = 2
                )
                likeactor.check_movie.add(movie)

        userpoint_genre = get_list_or_404(LikeGenre.objects.order_by('-point'), user=user)
        user.point_genre = userpoint_genre[0].point
        userpoint_keyword = get_list_or_404(LikeKeyword.objects.order_by('-point'), user=user)
        user.point_keyword = userpoint_keyword[0].point
        user.save()
        context = {
            'is_liked':is_liked,
            'like_count': movie.like_users.count()
        }
        return JsonResponse(context)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_watchlist(request, movie_pk):  
    if request.method == 'POST':  
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        # user2 = get_object_or_404(get_user_model(), pk=request.user.pk)
        
        if movie.wish_watch.filter(pk=user.pk).exists():  
            movie.wish_watch.remove(user)
            is_wish_watch = False
        else:  
            movie.wish_watch.add(user)
            is_wish_watch = True
        for i in movie.genres.all():  
            if user.likegenre_set.filter(genre=i).count() > 0:  
                if movie not in user.likegenre_set.all().get(genre = i, user=user).check_movie.all():  
                    likegenre = user.likegenre_set.get(genre = i, user=user)
                    likegenre.point += 4
                    likegenre.check_movie.add(movie)
                    likegenre.save()
            else:  
                likegenre = LikeGenre.objects.create(
                    user = user,
                    genre = i,
                    point = 4,
                )
                likegenre.check_movie.add(movie)

        # 가중치 알고리즘
        for i in movie.keywords.all():  
            if user.likekeyword_set.all().filter(keyword=i).count() >0:  
                if movie not in user.likekeyword_set.all().get(keyword = i, user=user).check_movie.all():  
                    likekeyword = user.likekeyword_set.all().get(keyword = i, user=user)
                    likekeyword.point += 1
                    likekeyword.check_movie.add(movie)
                    likekeyword.save()
            else:  
                likekeyword = LikeKeyword.objects.create(
                    user = user,
                    keyword = i,
                    point = 1
                )
                likekeyword.check_movie.add(movie)
        
        for i in movie.actors.all():  
            if user.likeactor_set.all().filter(actor=i).count > 0:  
                if movie not in user.likeactor_set.all().get(actor = i, user=user).check_movie.all():  
                    likeactor = user.likeactor_set.all().get(actor = i, user = user)
                    likeactor.point += 2
                    likeactor.check_movie.add(movie)
                    likeactor.save()
            else:  
                likeactor = LikeActor.objects.create(
                    user = user,
                    actor = i,
                    point = 2
                )
                likeactor.check_movie.add(movie)
        context = {
            'is_wish_watch' : is_wish_watch,
            'is_watchlist_count' : movie.wish_watch.count()
        }
        return JsonResponse(context)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_watched(request, movie_pk):  
    if request.method == 'POST':  
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        
        if movie.is_watched.filter(pk=user.pk).exists():  
            movie.is_watched.remove(user)
            is_watched = False
        else:  
            movie.is_watched.add(user)
            is_watched = True
        for i in movie.genres.all():  
            if user.likegenre_set.filter(genre=i).count() > 0:  
                if movie not in user.likegenre_set.all().get(genre = i, user=user).check_movie.all():  
                    likegenre = user.likegenre_set.get(genre = i, user=user)
                    likegenre.point += 4
                    likegenre.check_movie.add(movie)
                    likegenre.save()
            else:  
                likegenre = LikeGenre.objects.create(
                    user = user,
                    genre = i,
                    point = 4,
                )
                likegenre.check_movie.add(movie)

        # 가중치 알고리즘
        for i in movie.keywords.all():  
            if user.likekeyword_set.all().filter(keyword=i).count() >0:  
                if movie not in user.likekeyword_set.all().get(keyword = i, user=user).check_movie.all():  
                    likekeyword = user.likekeyword_set.all().get(keyword = i, user=user)
                    likekeyword.point += 1
                    likekeyword.check_movie.add(movie)
                    likekeyword.save()
            else:  
                likekeyword = LikeKeyword.objects.create(
                    user = user,
                    keyword = i,
                    point = 1
                )
                likekeyword.check_movie.add(movie)
        
        for i in movie.actors.all():  
            if user.likeactor_set.all().filter(actor=i).count > 0:  
                if movie not in user.likeactor_set.all().get(actor = i, user=user).check_movie.all():  
                    likeactor = user.likeactor_set.all().get(actor = i, user = user)
                    likeactor.point += 2
                    likeactor.check_movie.add(movie)
                    likeactor.save()
            else:  
                likeactor = LikeActor.objects.create(
                    user = user,
                    actor = i,
                    point = 2
                )
                likeactor.check_movie.add(movie)
        context = {
            'is_watched' : is_watched,
        }
        return JsonResponse(context)
