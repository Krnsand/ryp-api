from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment
from reviews.models import Review


class Like(models.Model):
    """
    Like model, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    comment = models.ForeignKey(
        Comment, related_name='likes', blank=True, null=True,
        on_delete=models.CASCADE
    )
    review = models.ForeignKey(
        Review, related_name='likes', blank=True, null=True,
        on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('owner', 'post'), ('owner', 'comment'), ('owner', 'review')

    def __str__(self):
        return f'{self.owner} {self.post}'
