from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Topic, Vocabulary, UserProgress


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "role"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "name"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "An account with this email already exists."
            )
        return value

    def create(self, validated_data):
        name = validated_data.pop("name")
        email = validated_data["email"]
        password = validated_data["password"]

        # Split name into first and last name
        name_parts = name.strip().split(" ", 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        user = User.objects.create_user(
            username=email,  # Use email as username
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role="user",  # Default role for registration
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    raise serializers.ValidationError("User account is disabled.")
            else:
                raise serializers.ValidationError(
                    "Invalid email or password. Please check your credentials and try again."
                )
        else:
            raise serializers.ValidationError("Must include email and password.")

        return data


class TopicSerializer(serializers.ModelSerializer):
    vocabulary_count = serializers.ReadOnlyField()

    class Meta:
        model = Topic
        fields = [
            "id",
            "name",
            "description",
            "color",
            "vocabulary_count",
            "created_at",
        ]


class VocabularySerializer(serializers.ModelSerializer):
    topic_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Vocabulary
        fields = [
            "id",
            "topic_id",
            "word",
            "pronunciation",
            "meaning",
            "example",
            "image_url",
            "difficulty",
        ]

    def create(self, validated_data):
        topic_id = validated_data.pop("topic_id", None)
        if topic_id:
            validated_data["topic_id"] = topic_id
        return super().create(validated_data)


class UserProgressSerializer(serializers.ModelSerializer):
    vocabulary_id = serializers.IntegerField(write_only=True, required=False)
    topic_id = serializers.IntegerField(write_only=True, required=False)
    user_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = UserProgress
        fields = [
            "id",
            "user_id",
            "topic_id",
            "vocabulary_id",
            "status",
            "correct_count",
            "total_attempts",
            "last_studied",
            "accuracy",
        ]
        read_only_fields = ["accuracy"]

    def create(self, validated_data):
        user_id = validated_data.pop("user_id", None)
        topic_id = validated_data.pop("topic_id", None)
        vocabulary_id = validated_data.pop("vocabulary_id", None)

        if user_id:
            validated_data["user_id"] = user_id
        if topic_id:
            validated_data["topic_id"] = topic_id
        if vocabulary_id:
            validated_data["vocabulary_id"] = vocabulary_id

        return super().create(validated_data)
