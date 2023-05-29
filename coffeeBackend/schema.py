import graphene
import api.schema
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
from users import schema

class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   token_auth = mutations.ObtainJSONWebToken.Field()
   update_account = mutations.UpdateAccount.Field()
   verify_token = mutations.VerifyToken.Field()
   refresh_token = mutations.RefreshToken.Field()

class Query(MeQuery,UserQuery,api.schema.Query,graphene.ObjectType):
   pass

class Mutation(schema.Mutation,AuthMutation, graphene.ObjectType):
   pass

schema = graphene.Schema(query=Query,mutation=Mutation)