from django.db import models

import random
import string

CHARACTERS = string.ascii_letters + string.digits

def shorten_url(original_url):
    length = random.choice(range(5,9))
    short_url = ''.join(random.choice(CHARACTERS) for i in range(length))
    return short_url

class URL(models.Model):
    original_url = models.CharField(max_length=2048)
    short_url = models.CharField(max_length=20,blank=True,null=True)
    red_counter = models.IntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return f"Original URL: {self.original_url}  Short URL: http://{self.short_url} Redirect counter: {self.red_counter}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.short_url = shorten_url(self.original_url)
        super().save(*args, **kwargs)
