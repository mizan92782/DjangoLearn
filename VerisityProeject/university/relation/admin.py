from django.contrib import admin
from .models import Relation, RelationManyToMany, RelationManyToOne

# Register your models here.
@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
	list_display = ('id', 'student', 'teacher', 'course','student_batch', 'teacher_status')
 
 
 
@admin.register(RelationManyToOne)
class RelationManyToOneAdmin(admin.ModelAdmin):
	list_display = ('id', 'teacher',  'student','course','student_batch', 'teacher_status')
 
 
 
 
 
@admin.register(RelationManyToMany)
class RelationManyToManyAdmin(admin.ModelAdmin):
	list_display = ('id', 'teacher',  'student','course','student_batch', 'teacher_status')