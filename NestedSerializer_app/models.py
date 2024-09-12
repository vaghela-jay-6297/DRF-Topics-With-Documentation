from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)

    def __str__(self):
        return self.first_name
    
class Book(models.Model):
    title = models.CharField(max_length=128)
    # Foreignkey concept
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books_by_author")
    release_data = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title


class Musician(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    instrument = models.CharField(max_length=64)

    def __str__(self):
        return self.first_name
    
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name="album_musician", null=True)
    name = models.CharField(max_length=64)
    release_data = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name