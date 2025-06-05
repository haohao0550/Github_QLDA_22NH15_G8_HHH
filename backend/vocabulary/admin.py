from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Topic, Vocabulary, UserProgress


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_active",
        "date_joined",
    ]
    list_filter = ["role", "is_active", "is_staff", "date_joined"]
    search_fields = ["username", "email", "first_name", "last_name"]

    fieldsets = BaseUserAdmin.fieldsets + (("Additional Info", {"fields": ("role",)}),)

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("role", "email", "first_name", "last_name")}),
    )


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "color", "vocabulary_count", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name", "description"]
    readonly_fields = ["vocabulary_count", "created_at", "updated_at"]

    def vocabulary_count(self, obj):
        return obj.vocabulary_count

    vocabulary_count.short_description = "Vocabulary Count"


@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ["word", "topic", "difficulty", "pronunciation", "created_at"]
    list_filter = ["topic", "difficulty", "created_at"]
    search_fields = ["word", "meaning", "example"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        (
            "Basic Information",
            {"fields": ("topic", "word", "pronunciation", "difficulty")},
        ),
        ("Content", {"fields": ("meaning", "example", "image_url")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ["user", "vocabulary", "topic", "status", "accuracy", "last_studied"]
    list_filter = ["status", "topic", "last_studied"]
    search_fields = ["user__username", "vocabulary__word", "topic__name"]
    readonly_fields = ["accuracy", "created_at", "last_studied"]

    def accuracy(self, obj):
        return f"{obj.accuracy}%"

    accuracy.short_description = "Accuracy"

    fieldsets = (
        ("Progress Information", {"fields": ("user", "vocabulary", "topic", "status")}),
        ("Statistics", {"fields": ("correct_count", "total_attempts", "accuracy")}),
        (
            "Timestamps",
            {"fields": ("last_studied", "created_at"), "classes": ("collapse",)},
        ),
    )


# Customize admin site
admin.site.site_header = "Wordify Administration"
admin.site.site_title = "Wordify Admin"
admin.site.index_title = "Welcome to Wordify Administration"
