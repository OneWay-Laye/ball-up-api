from django.db import models
from django.contrib.auth import get_user_model

# This will create the Park model.
class Park(models.Model):
    """This is the Model for the Park"""
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    indoor = models.BooleanField()
    numOfCourts = models.IntegerField()

    def __str__(self):
        """This will return a string"""
        return f"This park is named '{self.name}. It is '{self.indoor}' that it is indoor and has '{self.numOfCourts}' courts. This Park is located at '{self.address}'."

    def as_dict(self):
        """Returns dictionary version of Park"""
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'indoor': self.indoor,
            'numOfCourts': self.numOfCourts
        }
