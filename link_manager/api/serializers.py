from rest_framework import serializers
from .models import Link, Collection
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import User


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password')


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'title', 'description', 'url', 'image', 'link_type', 'created_at', 'updated_at']
        read_only_fields = ['id', 'title', 'description', 'image', 'link_type', 'created_at', 'updated_at']

    def validate_url(self, value):
        if not value:
            raise serializers.ValidationError('URL is required')
        return value


class CollectionSerializer(serializers.ModelSerializer):
    links = serializers.PrimaryKeyRelatedField(many=True, queryset=Link.objects.all(), required=False)

    class Meta:
        model = Collection
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'links']

    def create(self, validated_data):
        links = validated_data.pop('links', [])
        collection = super().create(validated_data)
        collection.links.set(links)
        return collection

    def update(self, instance, validated_data):
        links = validated_data.pop('links', [])
        instance = super().update(instance, validated_data)
        instance.links.set(links)
        return instance
