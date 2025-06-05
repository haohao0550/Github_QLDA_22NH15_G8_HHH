from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator


class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("user", "User"),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    color = models.CharField(max_length=7, default="#3B82F6")  # Hex color code
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def vocabulary_count(self):
        return self.vocabulary_set.count()


class Vocabulary(models.Model):
    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=200)
    meaning = models.TextField()
    example = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY_CHOICES, default="medium"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["word"]
        unique_together = ["topic", "word"]

    def __str__(self):
        return f"{self.word} ({self.topic.name})"


class UserProgress(models.Model):
    STATUS_CHOICES = [
        ("not_started", "Not Started"),
        ("learning", "Learning"),
        ("mastered", "Mastered"),
        ("review", "Review"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default="not_started"
    )
    correct_count = models.PositiveIntegerField(default=0)
    total_attempts = models.PositiveIntegerField(default=0)
    last_studied = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "vocabulary"]
        ordering = ["-last_studied"]

    def __str__(self):
        return f"{self.user.username} - {self.vocabulary.word} ({self.status})"

    @property
    def accuracy(self):
        if self.total_attempts == 0:
            return 0
        return round((self.correct_count / self.total_attempts) * 100, 2)
