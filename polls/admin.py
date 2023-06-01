from django.contrib import admin
from .models import Workout, Exercise, Program, WorkoutExercise
# Register your models here.
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Program)
admin.site.register(WorkoutExercise)