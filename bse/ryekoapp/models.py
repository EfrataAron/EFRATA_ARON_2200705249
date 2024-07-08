from django.db import models
from django.utils import timezone


# Create your models here.

#to create modeule, we use a class
# models.Model helps define model
class SoilMoistureReading(models.Model):
    #store the timestamp of reading with default value of current time
    timestamp = models.DateTimeField(default=timezone.now)
    moisture_level = models.FloatField() 
    # store soil moisture level as floating point number
    
    #define a string representing method of the class 
    
    def _str_(self):
        return f"{self.timestamp} - {self.moisture_level}" # returns string that includes timestamp and moisture level
    
#create a migration (info to database)

   
    
        
    
        class Meta:
            abstract = True
    