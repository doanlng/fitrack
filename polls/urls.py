from django.urls import path
from graphene_django.views import GraphQLView
from . import views
from polls.schema.schema import schema

urlpatterns = [
    path("", views.index, name="index"),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]
