from urllib import response
from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from article.serializers import ArticleSerializer
from article.models import Article

# Create your views here.
class ArticleView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"massege": "저장이 완료되었습니다.", "response": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"massege": "오류가 발생했습니다.", "response": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
