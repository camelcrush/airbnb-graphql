import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "hello"


class Mutation:
    pass


schema = graphene.Schema(query=Query)
