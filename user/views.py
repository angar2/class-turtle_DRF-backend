from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from user.serializers import UserSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers_jwt import TokenObtainPairSerializer

# Create your views here.
class UserView(APIView):

    # 회원정보 조회
    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

    # 회원가입
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"massege": "회원가입이 완료되었습니다", "response": serializer.data}, status=status.HTTP_200_OK)
        return Response({"massege": "회원가입 오류", "response": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# 로그인
class login(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


