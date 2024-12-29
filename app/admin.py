from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "is_staff", "is_active"),
        }),
    )
    search_fields = ("username", "email")
    ordering = ("username",)

admin.site.register(User, CustomUserAdmin)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")
    search_fields = ("name", "owner__username")
    list_filter = ("created_at",)



@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ("project", "user", "role")
    list_filter = ("role", "project")
    search_fields = ("project__name", "user__username")



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "priority", "assigned_to", "project", "due_date", "created_at")
    list_filter = ("status", "priority", "project")
    search_fields = ("title", "project__name", "assigned_to__username")



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "user", "task", "created_at")
    list_filter = ("created_at", "task")
    search_fields = ("content", "user__username", "task__title")










