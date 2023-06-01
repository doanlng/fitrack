import graphene
from ..types.ProgramType import ProgramType
from ...models import Program

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

class ProgramMutations(graphene.ObjectType):
    add_program = ProgramMutationAdd.Field()
    update_program = ProgramMutationUpdate.Field()
    delete_program = ProgramtMutationDelete.Field()