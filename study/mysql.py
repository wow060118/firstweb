from .models import student, teacher


class studentObj():
    def dels(id):
        student.objects.get(student, pk=id).delete()

    def sav(self):
        s = student.objects.create(no=1, name="fff")
        s1 = student()
        s1.no=123
        s1.name="ggg"
        s1.save()
