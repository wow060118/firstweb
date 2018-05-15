from django.db import models
import json


# Create your models here.
class student(models.Model, json.JSONEncoder):
    no = models.IntegerField(default=0)
    name = models.CharField(max_length=20)

    def out_student_name(self):
        return self.name


class teacher(models.Model, json.JSONEncoder):
    t_no = models.IntegerField(default=0)
    t_name = models.CharField(max_length=20)

    def out_teacher_name(self):
        return self.t_name
