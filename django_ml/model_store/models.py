from django.db import models

# Create your models here.

class TrainedModels(models.Model):
    picked_model = models.CharField(max_length=3000)
    model_parameters = models.CharField(max_length=1000)
    timestamp = models.DateTimeField()
    train_size = models.IntegerField()
    test_size = models.IntegerField()
    # the methods used to score the model
    model_measures = models.CharField(max_length=300)
    # the scores of the methods used
    model_scores = models.CharField(max_length=300)
    model_name = models.CharField(max_length=300)
