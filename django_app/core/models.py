from django.db import models


class Note(models.Model):
    """
    Simple note that is stored in the shared PostgreSQL database.
    Because both web servers talk to the same DB, a note created on
    web1 is immediately visible when the request is handled by web2
    (and vice-versa). This is the core demonstration of high availability
    with a shared data store.
    """
    text = models.CharField(max_length=500)
    author = models.CharField(max_length=100, blank=True, default='Anonymous')
    created_at = models.DateTimeField(auto_now_add=True)
    # Optional: which backend originally received the create request
    created_on_host = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author}: {self.text[:40]}"

