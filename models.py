from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

# model2

class StreamPlatform(models.Model):
    name= models.CharField(max_length=30)
    about=models.CharField(max_length=150)
    website=models.URLField(max_length=100)
    
    def __str__(self):
        return self.name


#model 1
class WatchList(models.Model):
    title=models.CharField(max_length=50)
    storyline=models.CharField(max_length=200)
    #django relationships(One webseries can have only one platform)
    platform = models.ForeignKey(StreamPlatform, on_delete= models.CASCADE, related_name="watchlist") 
    active=models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    created_on=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    

#model 3
class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description= models.CharField(max_length=200, null=True)
    watchlist=models.ForeignKey(WatchList,on_delete= models.CASCADE, related_name="reviews")
    active=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update =models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title + " | " + str(self.review_user)



    
# class Movie(models.Model):
#     name=models.CharField(max_length=50)
#     description=models.CharField(max_length=200)
#     active=models.BooleanField(default=True)
    
    
#     def __str__(self):
#         return self.name    