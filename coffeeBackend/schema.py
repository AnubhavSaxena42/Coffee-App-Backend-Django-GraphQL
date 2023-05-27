import graphene
import api.schema
from graphql_auth.schema import UserQuery, MeQuery

class Query(MeQuery,UserQuery,api.schema.Query,graphene.ObjectType):
   pass

schema = graphene.Schema(query=Query)