from dacite import from_dict
from drf_spectacular.utils import extend_schema
from rest_framework import parsers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from account.models import Profile
from account.api.profile.serializers import ProfileSerializer, UpdateAvatarSerializer
from account.services.profile import ProfileService, UpdateProfileDTO


class ProfileApi(APIView):
    queryset = None
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get_or_create(user=self.request.user)[0]

    @extend_schema(tags=["profile"], responses={HTTP_200_OK: ProfileSerializer()})
    def get(self, *args, **kwargs):
        print(self.get_object())
        return Response(self.serializer_class(self.get_object()).data)

    @extend_schema(tags=["profile"], responses={HTTP_200_OK: ProfileSerializer()})
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        dto = from_dict(data_class=UpdateProfileDTO, data=serializer.validated_data)
        profile = ProfileService().update_profile(request.user, dto)
        return Response(self.serializer_class(profile).data)


class AvatarApi(GenericAPIView):
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = UpdateAvatarSerializer
    output_serializer = ProfileSerializer

    @extend_schema(tags=["profile"], request=UpdateAvatarSerializer, responses={HTTP_200_OK: ProfileSerializer()})
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.data)
        serializer.is_valid(raise_exception=True)

        profile = ProfileService().update_avatar(request.user, request.FILES.get("avatar"))
        return Response(self.output_serializer(data=profile).data)
