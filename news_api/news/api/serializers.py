from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist


class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()
    # author = JournalistSerializer(read_only=True)
    # author = serializers.StringRelatedField()

    class Meta:
        model = Article
        exclude = ("id",)
        # fields = "__all__"

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, attrs):
        if attrs['title'] == attrs['description']:
            raise serializers.ValidationError('Title and description')
        return attrs

    def validate_title(self, value):
        if len(value) < 30:
            raise serializers.ValidationError('Title menshe 30')
        return value


class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(read_only = True, many = True,  view_name='articles-detail')
    # articles = ArticleSerializer(many = True, read_only=True)
    class Meta:
        model = Journalist
        fields = "__all__"

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_date):
#         print(validated_date)
#         return Article.objects.create(**validated_date)

#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.created_at = validated_data.get('created_at', instance.created_at)
#         instance.updated_at = validated_data.get('updated_at', instance.updated_at)
#         instance.save()
#         return instance

#     def validate(self, attrs):
#         if attrs['title'] == attrs['description']:
#             raise serializers.ValidationError('Title and description')
#         return attrs

#     def validate_title(self, value):
#         if len(value) < 60:
#             raise serializers.ValidationError('Title menshe 60')
#         return value