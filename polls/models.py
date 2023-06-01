from django.db import models

class Program(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    EXERCISE_TYPE_CHOICES = (
        ('strength', 'Strength'),
        ('cardio', 'Cardio'),
    )

    name = models.CharField(max_length=100)
    exercise_type = models.CharField(max_length=10, choices=EXERCISE_TYPE_CHOICES)

    def __str__(self):
        return self.name


class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField()
    length = models.IntegerField()
    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING)
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

    def __str__(self):
        return self.name


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return f"{self.exercise.name} - Workout {self.workout.id}"

""" class CustomUser(AbstractUser):
    emails = models.EmailField(unique=True, blank=False, null=False)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email' """