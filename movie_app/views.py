from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from movie_app.models import Director
from .serializers import (DirectorListSerializer, DirectorSerializer,
                          MovieListSerializer, MovieSerializer,
                          ReviewListSerializer, ReviewSerializer)

@api_view(['GET', 'POST'])
def director_list_view(request):
    directors = Director.objects.all()
    list_ = DirectorListSerializer(directors, many=True).data
    return Response(data=list_)

@api_view(['GET', 'POST'])
def director_view(request, id):
    directors = Director.objects.get(id=id)
    list_ = DirectorSerializer(directors, many=False).data
    return Response(data=list_)

@api_view(['GET', 'POST'])
def movie_list_view(request):
    movies = Movie.objects.all()
    list_ = MovieListSerializer(movies, many=True).data
    return Response(data=list_)

@api_view(['GET', 'POST'])
def movie_view(request, id):
    movie = Movie.objects.get(id=id)
    list_ = MovieSerializer(movie, many=False).data
    return Response(data=list_)

@api_view(['GET', 'POST'])
def review_list_view(request):
    reviews = Review.objects.all()
    list_ = ReviewListSerializer(reviews, many=True).data
    return Response(data=list_)

@api_view(['GET', 'POST'])
def review_view(request, id):
    review = Review.objects.get(id=id)
    list_ = ReviewSerializer(review, many=False).data
    return Response(data=list_)