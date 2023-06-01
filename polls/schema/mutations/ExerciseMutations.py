import graphene
from ..types.ExerciseType import ExerciseType
from ...models import Exercise, Workout


class ExerciseMutationAdd(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        exercise_type = graphene.String(required=True)
        workout_id = graphene.Int(required=True)

    exercise = graphene.Field(ExerciseType)

    @classmethod
    def mutate(cls, root, info, name, exercise_type, workout_id):
        workout = Workout.objects.get(id=workout_id)
        exercise = Exercise(
            name=name, exercise_type=exercise_type, workout=workout)
        exercise.save()
        return ExerciseMutationAdd(exercise=exercise)


class ExerciseMutationUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        exercise_type = graphene.String()
        workout_id = graphene.Int()

    exercise = graphene.Field(ExerciseType)

    @classmethod
    def mutate(cls, root, info, id, name=None, exercise_type=None, workout_id=None):
        exercise = Exercise.objects.get(id=id)
        if name is not None:
            exercise.name = name
        if exercise_type is not None:
            exercise.exercise_type = exercise_type
        if workout_id is not None:
            workout = Workout.objects.get(id=workout_id)
            exercise.workout = workout
        exercise.save()
        return ExerciseMutationUpdate(exercise=exercise)


class ExerciseMutationDelete(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    exercise = graphene.Field(ExerciseType)

    @classmethod
    def mutate(cls, root, info, id):
        exercise = Exercise.objects.get(id=id)
        exercise.delete()
        return True


class ExerciseMutations(graphene.ObjectType):
    add_exercise = ExerciseMutationAdd.Field()
    update_exercise = ExerciseMutationUpdate.Field()
    delete_exercise = ExerciseMutationDelete.Field()
