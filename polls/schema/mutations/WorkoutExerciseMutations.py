import graphene
from ..types.WorkoutExerciseType import WorkoutExerciseType
from ...models import WorkoutExercise, Workout, Exercise


class WorkoutExerciseMutationAdd(graphene.Mutation):
    class Arguments:
        workout_id = graphene.Int(required=True)
        exercise_id = graphene.Int(required=True)
        sets = graphene.Int(required=True)
        reps = graphene.Int(required=True)

    workout_exercise = graphene.Field(WorkoutExerciseType)

    @classmethod
    def mutate(cls, root, info, workout_id, exercise_id, sets, reps):
        workout = Workout.objects.get(id=workout_id)
        exercise = Exercise.objects.get(id=exercise_id)
        workout_exercise = WorkoutExercise(
            workout=workout, exercise=exercise, sets=sets, reps=reps)
        workout_exercise.save()
        return WorkoutExerciseMutationAdd(workout_exercise=workout_exercise)


class WorkoutExerciseMutationUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        sets = graphene.Int()
        reps = graphene.Int()

    workout_exercise = graphene.Field(WorkoutExerciseType)

    @classmethod
    def mutate(cls, root, info, id, sets=None, reps=None):
        workout_exercise = WorkoutExercise.objects.get(id=id)
        if sets is not None:
            workout_exercise.sets = sets
        if reps is not None:
            workout_exercise.reps = reps
        workout_exercise.save()
        return WorkoutExerciseMutationUpdate(workout_exercise=workout_exercise)


class WorkoutExerciseMutationDelete(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    workout_exercise = graphene.Field(WorkoutExerciseType)

    @classmethod
    def mutate(cls, root, info, id):
        workout_exercise = WorkoutExercise.objects.get(id=id)
        workout_exercise.delete()
        return True


class WorkoutExerciseMutations(graphene.ObjectType):
    add_workout_exercise = WorkoutExerciseMutationAdd.Field()
    update_workout_exercise = WorkoutExerciseMutationUpdate.Field()
    delete_workout_exercise = WorkoutExerciseMutationDelete.Field()
