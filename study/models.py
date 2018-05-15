from django.db import models


# Create your models here.
class student(models.Model):
    no = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    def out_student_name(self):
        return self.name

class teacher(models.Model):
    t_no = models.IntegerField(default=0)
    t_name = models.CharField(max_length=20)

    def out_teacher_name(self):
        return self.t_name