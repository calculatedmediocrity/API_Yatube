from djoser.serializers import UserSerializer
from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


class UserSerializer(UserSerializer):
    posts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='posts',
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    read_only_fields = ('comments',)

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    def validate_following(self, following):
        user = self.context["request"].user
        if Follow.objects.filter(following=following, user=user).exists():
            raise serializers.ValidationError(
                "Невозможно подписаться повторно."
            )
        if following == user:
            raise serializers.ValidationError(
                "Невозможно подписаться на себя."
            )
        return following

    class Meta:
        model = Follow
        fields = '__all__'
