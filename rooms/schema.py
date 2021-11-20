import graphene
from .types import RoomListResponse
from .models import Room


class Query(object):

    rooms = graphene.Field(RoomListResponse, page=graphene.Int())

    def resolve_rooms(self, info, page=1):
        page_size = 5
        skipping = page_size * (page - 1)
        taking = page_size * page
        rooms = Room.objects.all()[skipping:taking]
        total = Room.objects.count()
        return RoomListResponse(arr=rooms, total=total)
