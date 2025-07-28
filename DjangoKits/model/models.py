from django.db import models

#! Creat image path function
def user_image_path(instance, filename):
  return 'users/{0}/{1}'.format(instance.name, filename)

# ! **fileld validator
def ageValidtor(value):
  if value < 18:
    raise ValueError("Age must be greater than or equal to 18")
  if value > 60:
    raise ValueError("Age must be less than or equal to 60")
  return value



#! for choice
group=[
  ('sci',"Science"),
  ('arts',"Arts"),
  ('com',"Commerce"),
  
  
  
]

def products_image(instance, filename):
  return 'users/{0}/{1}'.format(instance.name, filename)



class Students(models.Model):
  name=models.CharField(max_length=20)
  age=models.IntegerField(validators=[ageValidtor])
  batch=models.IntegerField()
  
  #file upload
  pic = models.FileField(upload_to='pics/% Y/%m/%d/',null=True)
  userpic = models.FileField(upload_to=user_image_path, null=True, blank=True)
  
  #choices field
  group = models.CharField(max_length=10, choices=group, default='sci')
  

  
  # save mehtod : create instance default  and also can perform task in the time of instacne creating
  

    
  def __str__(self):
    return self.name
  
  
  
  
  #! ................relation.......
  
  #!------ one to many
  
class Mans(models.Model):
  name = models.CharField(max_length=20)
  age = models.IntegerField()
  batch = models.IntegerField()
  
  def __str__(self):
      return self.name


class Womens(models.Model):
  name = models.CharField(max_length=20)
  age = models.IntegerField()
  batch = models.IntegerField()


  def __str__(self):
      return self.name


class Couples(models.Model):
   husband  = models.ForeignKey(Mans, on_delete=models.CASCADE)
   wife = models.OneToOneField(Womens,on_delete=models.CASCADE)
   husband_age = models.IntegerField(blank=True, null=True,editable=False)
   wife_age = models.IntegerField(blank=True, null=True,editable=False)
   husband_batch = models.IntegerField(blank=True, null=True,editable=False)
   wife_batch = models.IntegerField(blank=True, null=True,editable=False)
   
   
   def save(self, *args, **kwargs):
       self.husband_batch = self.husband.batch
       self.wife_batch = self.wife.batch
       self.husband_age = self.husband.age
       self.wife_age = self.wife.age
       super().save(*args, **kwargs)
   