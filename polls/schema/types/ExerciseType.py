from graphene_django import DjangoObjectType
from ...models import Exercise

class ExerciseType(DjangoObjectType):
    class Meta:
        model = Exercise
        fields = ("id", "name", "exercise_type")
