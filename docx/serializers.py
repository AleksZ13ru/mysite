from rest_framework import serializers
from .models import Memo, PeopleToWhom, PeopleWho, MemoStatus  # Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class PeopleToWhomSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleToWhom
        fields = ('id', 'name')


class PeopleWhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleWho
        fields = ('id', 'fio')


class MemoStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoStatus
        fields = ('id', 'title')


class MemoSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=True, read_only=True, source='category_id')
    people_to_whom = PeopleToWhomSerializer(many=False, read_only=True, source='to_whom')
    people_who = PeopleWhoSerializer(many=False, read_only=True, source='who')
    memo_status = MemoStatusSerializer(many=False, read_only=True, source='status')

    class Meta:
        model = Memo
        fields = ('id', 'number', 'title', 'day_create', 'text', 'people_to_whom', 'people_who', 'memo_status')
        extra_kwargs = {
            'to_whom': {
                'write_only': True,
            },
        }
