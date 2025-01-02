from django.db import models

class MuscialDescription(models.Model):
    musical_name = models.CharField(max_length=255)
    musical_description = models.TextField()
    musical_image = models.ImageField(upload_to='games_images')

class BingoDescription(models.Model):
    bingo_name = models.CharField(max_length=255)
    bingo_description = models.TextField()
    bingo_image = models.ImageField(upload_to='games_images')

class FindImposterDescription(models.Model):
    findimposter_name = models.CharField(max_length=255)
    findimposter_description = models.TextField()
    findimposter_image = models.ImageField(upload_to='games_images')

class MonkeyDescription(models.Model):
    monkey_name = models.CharField(max_length=255)
    monkey_description = models.TextField()
    monkey_image = models.ImageField(upload_to='games_images')

class PinataDescription(models.Model):
    pinata_name = models.CharField(max_length=255)
    pinata_description = models.TextField()
    pinata_image = models.ImageField(upload_to='games_images')

class SpinnerDescription(models.Model):
    spinner_name = models.CharField(max_length=255)
    spinner_description = models.TextField()
    spinner_image = models.ImageField(upload_to='games_images')