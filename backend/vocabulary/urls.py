from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"topics", views.TopicViewSet)
router.register(r"vocabulary", views.VocabularyViewSet, basename="vocabulary")
router.register(r"progress", views.UserProgressViewSet, basename="progress")

urlpatterns = [
    # Authentication endpoints
    path("auth/register/", views.register_view, name="register"),
    path("auth/login/", views.login_view, name="login"),
    # Custom endpoints for frontend compatibility
    path(
        "vocabulary/topic/<int:topic_id>/",
        views.get_vocabulary_by_topic,
        name="vocabulary-by-topic",
    ),
    path(
        "progress/<int:user_id>/<int:topic_id>/",
        views.get_user_progress,
        name="user-progress",
    ),
    path("progress/update/", views.update_user_progress, name="update-progress"),
    # Router URLs
    path("", include(router.urls)),
]
