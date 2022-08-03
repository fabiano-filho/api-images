from genericpath import isfile
import os
import uuid
from django.db import models

def upload_image_formatter(instance, filename):
    return f"{str(uuid.uuid4())}-{filename}"

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to=upload_image_formatter, blank=True, null=True)

    def has_image(self):
        return True if self.image else False

    def remove_image(self):
        if self.has_image():
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        self.image = None

    def delete(self):
        self.remove_image()
        super(Photo, self).delete()