from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from ads.models import Selections
from ads.serializer import AdSerializer
from authentications.models import User


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selections
        fields = ['id', 'name']


class SelectionDetailSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    items = AdSerializer(many=True)

    class Meta:
        model = Selections
        fields = '__all__'


class SelectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selections
        fields = '__all__'


class SelectionsCreateSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Selections
        fields = '__all__'
