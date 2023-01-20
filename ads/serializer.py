from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from ads.models import *
from authentications.serializer import UserSerializer


class AdSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    category = SlugRelatedField(slug_field='name', allow_null=True,  queryset=Categories.objects.all())
    locations = serializers.SerializerMethodField()
    name = serializers.CharField(max_length=200, min_length=10)
    # TODO: Поле name объявления не может быть пустым и должно содержать не менее 10 символов. Да!
    slug = serializers.SlugField(max_length=10, min_length=5)

    def get_locations(self, ad):
        return [loc.name for loc in ad.author.locations.all()]

    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer
    category = SlugRelatedField(slug_field='name', queryset=Categories.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'
