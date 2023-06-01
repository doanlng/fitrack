import graphene
from ..types.ProgramType import ProgramType
from ...models import Program

class ProgramQueries(graphene.ObjectType):
    all_programs = graphene.List(ProgramType)
    program = graphene.Field(ProgramType, id=graphene.Int(required=True))

    def resolve_all_programs(root, info):
        return Program.objects.all()

    def resolve_program(root, info, id):
        try:
            return Program.objects.get(id=id)
        except Program.DoesNotExist:
            return None