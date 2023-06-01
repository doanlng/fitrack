from graphene_django import DjangoObjectType
from ...models import Workout

class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout
        fields = ("id", "name", "date", "program")
