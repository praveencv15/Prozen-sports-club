from django.db import models

class Member_details(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    PlayerType = models.CharField(max_length=200,null=True, blank=True)
    RunsScored = models.CharField(max_length=200,null=True, blank=True)
    passport = models.ImageField (upload_to="passports", blank=True, null=True)

    class Meta:
        ordering = ('firstname',) 
        verbose_name_plural = "Member details"

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}" 
    
class Sports_details(models.Model):
    name = models.CharField(max_length=200)
    passport = models.ImageField(upload_to="sporty", blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Sports details'

    def __str__(self):
        return self.name

class Store (models.Model):
    item_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="item_photo", blank=True, null=True)
    price = models.FloatField(default=0, null=True, blank=True)
    stock_available = models.IntegerField(default=0)

    class Meta:
        ordering = ("item_name",)
        verbose_name_plural = 'Store'

    def __str__(self):
        return self.item_name
    
class TournamentRegistration(models.Model):
    name = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    date = models.DateField(null=True, blank=True) 
    location = models.CharField(max_length=255, default='')

    def __str__(self):
        return f"{self.name} - {self.sport}"

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
