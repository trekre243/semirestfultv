from django.db import models

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        print(len(postData['network']))
        if len(postData['title']) <= 2:
            errors['title'] = 'Title should be at least 2 characters.'
        if len(postData['network']) < 3:
            errors['network'] = 'Network should be at least 3 characters.'
        if len(postData['description']) <= 10 and len(postData['description']) != 0:
            errors['description'] = 'Description should be at least 10 charcters if present.'
        
        if Show.objects.filter(title=postData['title']).count() != 0:
            errors['title'] = 'Title must be unique.'

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()