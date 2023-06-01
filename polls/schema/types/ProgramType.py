from graphene_django import DjangoObjectType
from ...models import Program

class ProgramType(DjangoObjectType):
    class Meta:
        model = Program
        fields = ("id", "name", "description")