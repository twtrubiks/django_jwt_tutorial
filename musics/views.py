# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from musics.models import Music
from musics.serializers import MusicSerializer


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)
