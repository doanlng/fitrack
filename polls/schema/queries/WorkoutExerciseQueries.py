import graphene
from ..types.WorkoutExerciseType import WorkoutExerciseType
from ...models import WorkoutExercise
class WorkoutExerciseQueries:
    workout_exercises = graphene.List(WorkoutExerciseType)
    
    def resolve_workout_exercises(self, info):
        return WorkoutExercise.objects.all()
