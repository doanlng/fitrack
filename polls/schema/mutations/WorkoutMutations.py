import graphene
from ..types.WorkoutType import WorkoutType
from ...models import Workout, Program


class WorkoutMutationAdd(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        date = graphene.Date(required=True)
        program_id = graphene.Int(required=True)

    workout = graphene.Field(WorkoutType)

    @classmethod
    def mutate(cls, root, info, name, date, program_id):
        program = Program.objects.get(id=program_id)
        workout = Workout(name=name, date=date, program=program)
        workout.save()
        return WorkoutMutationAdd(workout=workout)


class WorkoutMutationUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        date = graphene.Date()
        program_id = graphene.Int()

    workout = graphene.Field(WorkoutType)

    @classmethod
    def mutate(cls, root, info, id, name=None, date=None, program_id=None):
        workout = Workout.objects.get(id=id)
        if name is not None:
            workout.name = name
        if date is not None:
            workout.date = date
        if program_id is not None:
            program = Program.objects.get(id=program_id)
            workout.program = program
        workout.save()
        return WorkoutMutationUpdate(workout=workout)


class WorkoutMutationDelete(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    workout = graphene.Field(WorkoutType)

    @classmethod
    def mutate(cls, root, info, id):
        workout = Workout.objects.get(id=id)
        workout.delete()
        return True


class WorkoutMutations(graphene.ObjectType):
    add_workout = WorkoutMutationAdd.Field()
    update_workout = WorkoutMutationUpdate.Field()
    delete_workout = WorkoutMutationDelete.Field()
