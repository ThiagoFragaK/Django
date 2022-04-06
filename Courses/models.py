from django.db import models

class Course(models.Model):
    CourseId = models.CharField(max_length=30)
    Name = models.CharField(max_length=200)
    Descr = models.CharField(max_length=300)
    Value = models.IntegerField()

    class Meta:
        db_table = 'courses'
