import graphene
from ..types.WorkoutType import WorkoutType
from ...models import Workout

class WorkoutQueries(graphene.ObjectType):
    workouts = graphene.List(WorkoutType)
    workout = graphene.Field(WorkoutType, id=graphene.Int())

    def resolve_workouts(self, info):
        return Workout.objects.all()

    def resolve_workout(self, info, id):
        return Workout.objects.get(pk=id)