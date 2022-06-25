from rest_framework import serializers
from musics.models import Music


class MusicSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%Y/%m/%d %I:%M:%S')

    class Meta:
        model = Music
        fields = '__all__'
