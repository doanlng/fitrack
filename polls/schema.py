import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Workout, Exercise, Program, WorkoutExercise

class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout
        fields = ("id", "name", "date", "program")

class ExerciseType(DjangoObjectType):
    class Meta:
        model = Exercise
        fields = ("id", "name", "exercise_type")

class ProgramType(DjangoObjectType):
    class Meta:
        model = Program
        fields = ("id", "name", "description")
    
class WorkoutExerciseType(DjangoObjectType):
    class Meta:
        model = WorkoutExercise
        fields = ("workout", "exercise", "sets", "reps")

class Query(graphene.ObjectType):
    """     all_workouts = DjangoListField(WorkoutType)
        workouts_by_program = graphene.Field(WorkoutType, id=graphene.Int(required=True))

        all_programs = DjangoListField(ProgramType)
        programs_by_id = graphene.Field(
            ProgramType, id=graphene.Int(required=True))
        
        all_exercises = DjangoListField(ExerciseType)
        exercises_by_workout = graphene.Field(ExerciseType, id=graphene.Int(required=True))

        def resolve_all_programs(root, info):
            return Program.objects.all()
        
        def resolve_all_workouts(root, info):
            return Workout.objects.all()

        def resolve_all_exercises(root, info):
            return Exercise.objects.all()
        
        def resolve_programs_by_id(root, info, id):
            return Program.objects.filter(pk=id)
        
        def resolve_workouts_by_program(root, info, id):
            return Workout.objects.filter(program=id)
        
        def resolve_exercises_by_workout(root, info, id):
            return Exercise.objects.filter(workout=id) """
    
    all_programs = graphene.Field(ProgramType, id=graphene.Int(required=True))

    def resolve_all_programs(root, info, id):
        return Program.objects.get(pk=id)
    
    all_workouts = graphene.List(WorkoutType, id=graphene.Int(required=True))

    def resolve_all_workouts(root, info, id):
        return list(Workout.objects.filter(program=id))

class ProgramMutationAdd(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        desc = graphene.String(required=True)

    program = graphene.Field(ProgramType)
    
    @classmethod
    def mutate(cls, root, info, name, desc):
        program = Program(name=name, description=desc)
        program.save()
        return ProgramMutationAdd(program=program)

class ProgramMutationUpdate(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(default_value=None)
        desc = graphene.String(default_value=None)

    program = graphene.Field(ProgramType)
    
    @classmethod
    def mutate(cls, root, info, name, desc, id):
        program = Program.objects.get(id=id)
        if name is not None:
            program.name = name
        if desc is not None:
            program.description = desc
        program.save()
        return ProgramMutationUpdate(program=program)

class ProgramtMutationDelete(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)
    
    program = graphene.Field(ProgramType)

    @classmethod
    def mutate(cls, root, info, id):
        program = Program.objects.get(id=id)
        program.delete()
        return True
    
class Mutation(graphene.ObjectType):

    add_program = ProgramMutationAdd.Field()
    update_program = ProgramMutationUpdate.Field()
    delete_program = graphene.Field(ProgramType, id=graphene.Int(required=True))

schema = graphene.Schema(query=Query, mutation = Mutation) 