from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now


class CustomUserManager(BaseUserManager):
    """Custom manager for the custom User model."""

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required.")
        if not username:
            raise ValueError("The Username field is required.")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model."""

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Handled securely by AbstractBaseUser
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(default=now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username


class Project(models.Model):
    """Model to store project details."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(
        User,  # Refers to the custom User model
        on_delete=models.CASCADE,
        related_name="projects",
    )
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    """Model to store project members and their roles."""

    PROJECT_MEMBER_ROLES = [
        ("Admin", "Admin"),
        ("Member", "Member"),
    ]

    project = models.ForeignKey(
        Project,  
        on_delete=models.CASCADE,
        related_name="members",
    )
    user = models.ForeignKey(
       User,  # Refers to the custom User model
        on_delete=models.CASCADE,
        related_name="project_memberships",
    )
    role = models.CharField(max_length=20, choices=PROJECT_MEMBER_ROLES)

    class Meta:
        unique_together = ("project", "user")  # Ensures a user cannot be added to the same project multiple times.

    def __str__(self):
        return f"{self.user.username} - {self.project.name} ({self.role})"



class Task(models.Model):
    """Model to store task details."""

    TASK_STATUSES = [
        ("To Do", "To Do"),
        ("In Progress", "In Progress"),
        ("Done", "Done"),
    ]

    TASK_PRIORITIES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=TASK_STATUSES, default="To Do")
    priority = models.CharField(max_length=20, choices=TASK_PRIORITIES, default="Medium")
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  # If the assigned user is deleted, this field is set to NULL
        null=True,
        blank=True,
        related_name="tasks",
    )
    project = models.ForeignKey(
        Project,  
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    created_at = models.DateTimeField(default=now)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.status} ({self.priority})"



class Comment(models.Model):
    """Model to store comments on tasks."""

    content = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    task = models.ForeignKey(
        Task, 
        on_delete=models.CASCADE,
        related_name="comments",
    )
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Comment by {self.user.username} on Task {self.task.title}"









