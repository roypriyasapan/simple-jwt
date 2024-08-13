from django.db import models

# Create your models here.
class SchoolModel (models.Model):
    stu_name= models.CharField(max_length=50)
    stu_email= models.EmailField()
    stu_roll = models.BigIntegerField()
    def __str__(self):
        return self.stu_name
    

class StudentModel(models.Model):
    stu_name= models.CharField(max_length=50)
    stu_email= models.EmailField()
    stu_roll = models.BigIntegerField()