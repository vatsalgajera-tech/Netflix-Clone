from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(max_length=50, default='Play')
    redirect_url = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    TYPE_MOVIE = 'Movie'
    TYPE_SERIES = 'Series'
    TYPE_CHOICES = (
        (TYPE_MOVIE, 'Movie'),
        (TYPE_SERIES, 'Series'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    content_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    release_year = models.IntegerField()
    duration = models.CharField(max_length=50, help_text="e.g., 2h 15m or 3 Seasons")
    language = models.CharField(max_length=50, default='English')
    rating = models.CharField(max_length=10, blank=True, null=True)
    poster_image = models.ImageField(upload_to='posters/', blank=True, null=True)
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.content_type})"

class WatchHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now=True)
    progress_percentage = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'content')

    def __str__(self):
        return f"{self.user} - {self.content}"

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content')

    def __str__(self):
        return f"{self.user} - {self.content} ({self.rating}★)"

class MyList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content')

    def __str__(self):
        return f"{self.user} - {self.content}"
