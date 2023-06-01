from graphene_django import DjangoObjectType
from ...models import WorkoutExercise

class WorkoutExerciseType(DjangoObjectType):
    class Meta:
        model = WorkoutExercise
        fields = ("workout", "exercise", "sets", "reps")
