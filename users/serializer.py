from rest_framework import serializers

from users.models import *


class UserSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True

    )

    class Meta:
        model = User
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    locations = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        for loc in self._locations:
            loc_obj, _ = Location.objects.get_or_create(name=loc)
            user.locations.add(loc_obj)

        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.get('locations', None)
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()
        if self._locations:
            for loc in self._locations:
                loc_obj, _ = Location.objects.get_or_create(name=loc)
                user.locations.add(loc_obj)

        user.save()
        return user


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
