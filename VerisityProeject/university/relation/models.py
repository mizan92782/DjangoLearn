from django.db import models

# Create your models here.

#one to one relationship between students and teachers
class Relation(models.Model):
    student = models.OneToOneField('students.Student', on_delete=models.CASCADE)
    teacher = models.OneToOneField('teachers.Teacher', on_delete=models.CASCADE)
    course = models.CharField(max_length=100)

    student_batch = models.CharField(max_length=20, blank=True)
    teacher_status = models.CharField(max_length=100, blank=True)

     # for automatically setting the student batch and teacher status
    def save(self, *args, **kwargs):
        if self.student:
            self.student_batch = self.student.batch
        if self.teacher:
            self.teacher_status = self.teacher.status
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.teacher} ({self.course})"



# many relationship between students and teachers
class RelationManyToOne(models.Model):
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)
    student = models.OneToOneField('students.Student', on_delete=models.CASCADE)
    course = models.CharField(max_length=100)

    student_batch = models.CharField(max_length=20, blank=True)
    teacher_status = models.CharField(max_length=100, blank=True)

     # for automatically setting the student batch and teacher status
    def save(self, *args, **kwargs):
        if self.student:
            self.student_batch = self.student.batch
        if self.teacher:
            self.teacher_status = self.teacher.status
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.teacher} ({self.course})"
      
      
      
      
      
# many to many relationship between students and teachers
class RelationManyToMany(models.Model):
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    course = models.CharField(max_length=100)

    student_batch = models.CharField(max_length=20, blank=True)
    teacher_status = models.CharField(max_length=100, blank=True)

     # for automatically setting the student batch and teacher status
    def save(self, *args, **kwargs):
        if self.student:
            self.student_batch = self.student.batch
        if self.teacher:
            self.teacher_status = self.teacher.status
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.teacher} ({self.course})"
    