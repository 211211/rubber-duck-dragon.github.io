from rest_framework import serializers
from .models import Word, List, User

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ("url", "traditional", "simplified", "pinyin", "english", "hsk")

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ("id", "url", "name", "words")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "url", "username", "date_joined", "lists", "words")
