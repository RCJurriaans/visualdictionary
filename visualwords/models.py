from django.db import models
from django.conf import settings

class VisualWord(models.Model):
    word = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='creations')
    uploaded_on = models.DateTimeField(auto_now=True)
    
    approved = models.BooleanField(default=False)
    nsfw = models.BooleanField(default=False)
    
    # URLs
    url_raw = models.URLField(blank=True)
    url_img = models.URLField()
    url_thumb = models.URLField(blank=True)
    url_animated = models.URLField(blank=True)
    
    class Meta:
        ordering = ['word', 'uploaded_on']
    def __str__(self):              # __unicode__ on Python 2
        return self.word
