from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from account.api.account.serializers import RegisterSerializer
from account.services.account import AccountService


@extend_schema(tags=["account"], responses={status.HTTP_201_CREATED: None})
class RegisterApi(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService().register_new_user(serializer.validated_data["email"], serializer.validated_data["password"])
        return Response(status=status.HTTP_201_CREATED)


@extend_schema(tags=["account"], responses={status.HTTP_204_NO_CONTENT: None})
class DeleteAccountApi(APIView):
    def delete(self, request, *args, **kwargs):
        AccountService().delete_user(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)

