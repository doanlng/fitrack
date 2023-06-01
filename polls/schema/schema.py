import graphene
from graphene_django import DjangoObjectType
from ..models import Workout, Exercise, Program, WorkoutExercise

from .queries.WorkoutQueries import WorkoutQueries
from .queries.ProgramQueries import ProgramQueries
from .queries.ExerciseQueries import ExerciseQueries
from .queries.WorkoutExerciseQueries import WorkoutExerciseQueries

#from mutations.WorkoutMutations import WorkoutMutations
from .mutations.ProgramMutations import ProgramMutations
#from mutations.ExerciseMutations import ExerciseMutations
#from mutations.WorkoutExerciseMutations import WorkoutExerciseMutations



class Query(WorkoutQueries, ProgramQueries, ExerciseQueries, WorkoutExerciseQueries, graphene.ObjectType):
    pass

    
class Mutation(ProgramMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation = Mutation) 