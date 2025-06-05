from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import User, Topic, Vocabulary, UserProgress
from .serializers import (
    UserSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer,
    TopicSerializer,
    VocabularySerializer,
    UserProgressSerializer,
)


# Authentication Views
@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "name": f"{user.first_name} {user.last_name}".strip(),
                    "role": user.role,
                },
                "token": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "name": f"{user.first_name} {user.last_name}".strip(),
                    "role": user.role,
                },
                "token": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_200_OK,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Topic ViewSet
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            # Only admins can create, update, delete topics
            permission_classes = [IsAuthenticated]
        else:
            # All authenticated users can view topics
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return Response(
                {"error": "Only admins can create topics"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return Response(
                {"error": "Only admins can update topics"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return Response(
                {"error": "Only admins can delete topics"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)


# Vocabulary ViewSet
class VocabularyViewSet(viewsets.ModelViewSet):
    serializer_class = VocabularySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        topic_id = self.request.query_params.get("topic_id")
        if topic_id:
            return Vocabulary.objects.filter(topic_id=topic_id)
        return Vocabulary.objects.all()

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            # Only admins can create, update, delete vocabulary
            permission_classes = [IsAuthenticated]
        else:
            # All authenticated users can view vocabulary
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return Response(
                {"error": "Only admins can create vocabulary"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return Response(
                {"error": "Only admins can update vocabulary"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return Response(
                {"error": "Only admins can delete vocabulary"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)


# User Progress ViewSet
class UserProgressViewSet(viewsets.ModelViewSet):
    serializer_class = UserProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id", self.request.user.id)
        topic_id = self.request.query_params.get("topic_id")

        queryset = UserProgress.objects.filter(user_id=user_id)
        if topic_id:
            queryset = queryset.filter(topic_id=topic_id)

        return queryset

    def perform_create(self, serializer):
        # Ensure the user can only create progress for themselves (unless admin)
        user_id = self.request.data.get("user_id", self.request.user.id)
        if self.request.user.role != "admin" and user_id != self.request.user.id:
            user_id = self.request.user.id

        serializer.save(user_id=user_id)


# Custom API Views for specific frontend needs
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_vocabulary_by_topic(request, topic_id):
    """Get all vocabulary for a specific topic"""
    vocabulary = Vocabulary.objects.filter(topic_id=topic_id)
    serializer = VocabularySerializer(vocabulary, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_progress(request, user_id, topic_id):
    """Get user progress for a specific topic"""
    if request.user.role != "admin" and request.user.id != int(user_id):
        user_id = request.user.id

    # Get all vocabulary for the topic
    vocabulary_list = Vocabulary.objects.filter(topic_id=topic_id)
    progress_data = []

    for vocab in vocabulary_list:
        try:
            progress = UserProgress.objects.get(user_id=user_id, vocabulary=vocab)
            progress_data.append(
                {
                    "id": f"p{vocab.id}",
                    "userId": user_id,
                    "topicId": topic_id,
                    "vocabularyId": vocab.id,
                    "status": progress.status,
                    "correctCount": progress.correct_count,
                    "totalAttempts": progress.total_attempts,
                    "lastStudied": progress.last_studied.isoformat(),
                }
            )
        except UserProgress.DoesNotExist:
            # Create default progress entry
            progress_data.append(
                {
                    "id": f"p{vocab.id}",
                    "userId": user_id,
                    "topicId": topic_id,
                    "vocabularyId": vocab.id,
                    "status": "not_started",
                    "correctCount": 0,
                    "totalAttempts": 0,
                    "lastStudied": vocab.created_at.isoformat(),
                }
            )

    return Response(progress_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_user_progress(request):
    """Update user progress"""
    data = request.data
    user_id = data.get("userId", request.user.id)

    # Ensure users can only update their own progress (unless admin)
    if request.user.role != "admin" and user_id != request.user.id:
        user_id = request.user.id

    vocabulary_id = data.get("vocabularyId")

    try:
        vocabulary = Vocabulary.objects.get(id=vocabulary_id)
        progress, created = UserProgress.objects.get_or_create(
            user_id=user_id,
            vocabulary=vocabulary,
            defaults={
                "topic": vocabulary.topic,
                "status": data.get("status", "learning"),
                "correct_count": data.get("correctCount", 0),
                "total_attempts": data.get("totalAttempts", 1),
            },
        )

        if not created:
            # Update existing progress
            progress.status = data.get("status", progress.status)
            progress.correct_count += data.get("correctCount", 0)
            progress.total_attempts += data.get("totalAttempts", 1)
            progress.save()

        return Response({"success": True})

    except Vocabulary.DoesNotExist:
        return Response(
            {"error": "Vocabulary not found"}, status=status.HTTP_404_NOT_FOUND
        )
