import graphene
from graphene_django import DjangoObjectType
from .models import Room


class RoomType(DjangoObjectType):

    users = graphene.Field("users.types.UserType")

    class Meta:
        model = Room


class RoomListResponse(graphene.ObjectType):

    arr = graphene.List(RoomType)
    total = graphene.Int()
