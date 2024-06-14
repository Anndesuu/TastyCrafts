from django.db import models

class newRecipe(models.Model):
     recipeimage = models.ImageField(upload_to = 'pics/')
     recipename = models.CharField(max_length = 20)
     recipedesc = models.TextField()
     ingredients = models.TextField()
     procedure = models.TextField()

