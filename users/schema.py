from graphene_django.types import DjangoObjectType
from .models import CustomUser
from graphene import relay
import graphene
from graphql_relay import from_global_id

class UserNode(DjangoObjectType):
       class Meta:
        model=CustomUser
        filter_fields={
            'name':['exact','icontains','istartswith'],
        }
        interfaces=(relay.Node,)

class UserType(DjangoObjectType):
    class Meta:
        model=CustomUser


class UserVerifyMutation(relay.ClientIDMutation):
    class Input:
        id=graphene.ID(required=True)

    user=graphene.Field(UserType)

    @classmethod
    def mutate_and_get_payload(cls,root,info,**input):
        print(input.get('id'))
        id=input.get('id')
        print(from_global_id(id)[1])
        user=CustomUser.objects.get(pk=from_global_id(id)[1])
        print(user.status.verified)
        user.status.verified=True
        user.status.save()

        return UserVerifyMutation(user)


class Mutation(graphene.ObjectType):
    user_verify = UserVerifyMutation.Field()
  