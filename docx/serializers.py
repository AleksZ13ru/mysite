from rest_framework import serializers
from .models import Memo  # Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ('id', 'number', 'title', 'to_whom', 'day_create', 'text', 'who', 'status')

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Memo.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.number = validated_data.get('number', instance.number)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.to_whom = validated_data.get('to_whom', instance.to_whom)
    #     instance.language = validated_data.get('day_create', instance.day_create)
    #     instance.day_create = validated_data.get('text', instance.text)
    #     instance.who = validated_data.get('who', instance.who)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()
    #     return instance
