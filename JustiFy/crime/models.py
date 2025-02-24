from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class CrimePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="crime_posts")
    title = models.CharField(max_length=255)
    description = models.TextField()
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    image = models.ImageField(upload_to='crime_images/')
    video = models.FileField(upload_to='crime_videos/', blank=True, null=True)
    post_time = models.DateTimeField(default=timezone.now)
    crime_time = models.DateTimeField()
    share_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('crime:post_detail', kwargs={'pk': self.pk})
    
    @property
    def upvote_count(self):
        return self.votes.filter(vote_type=1).count()

    @property
    def downvote_count(self):
        return self.votes.filter(vote_type=-1).count()


class SharedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shared_posts")
    original_post = models.ForeignKey(CrimePost, on_delete=models.CASCADE, related_name="shares")
    shared_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} shared {self.original_post}"

class Comment(models.Model):
    crime_post = models.ForeignKey(CrimePost, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="crime_comments")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.crime_post}"


class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saved_posts")
    crime_post = models.ForeignKey(CrimePost, on_delete=models.CASCADE, related_name="saves")
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'crime_post')

    def __str__(self):
        return f"{self.user} saved {self.crime_post}"
    
class Vote(models.Model):
    VOTE_CHOICES = (
        (1, 'Upvote'),
        (-1, 'Downvote'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    crime_post = models.ForeignKey(CrimePost, on_delete=models.CASCADE, related_name="votes")
    vote_type = models.SmallIntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'crime_post')

    def __str__(self):
        return f"{self.user} voted {self.get_vote_type_display()} on {self.crime_post}"
