from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)        # নাম
    age = models.IntegerField()                   # বয়স
    batch = models.IntegerField()                 # ব্যাচ নাম্বার
    group = models.CharField(                     # গ্রুপ (choice সহ)
        max_length=10,
        choices=[
            ('sci', 'Science'),
            ('arts', 'Arts'),
            ('com', 'Commerce'),
        ],
        default='sci'
    )

    def __str__(self):
        return f"{self.name} ({self.batch})"
