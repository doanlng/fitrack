import graphene
from ..types.ExerciseType import ExerciseType
from ...models import Exercise
class ExerciseQueries:
    exercises = graphene.List(ExerciseType)
    exercise = graphene.Field(ExerciseType, id=graphene.Int())
    
    def resolve_exercises(self, info):
        return Exercise.objects.all()
    def resolve_exercise(self, info, id):
        return Exercise.objects.get(pk=id)