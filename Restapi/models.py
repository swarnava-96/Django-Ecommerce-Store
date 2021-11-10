from django.db import models

# Create your models here.
class Users(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    ranking = models.FloatField()

    def upload_photo(self, filename):
        path = "Restapi/photo/()".format(filename)
        return path

    photo = models.ImageField(upload_to = "upload_photo", null=True, blank=True)

    def upload_file(self, filename):
        path = "Restapi/file/()".format(filename)
        return path
    
    resume = models.ImageField(upload_to=upload_file, null=True, blank=True)


class profile(models.Model):
    def nameFile(instance, filename):
     return '/'.join(['images', str(instance.name), filename])
    name = models.CharField(max_length=10)
    picture=models.ImageField(upload_to=nameFile,blank=True)