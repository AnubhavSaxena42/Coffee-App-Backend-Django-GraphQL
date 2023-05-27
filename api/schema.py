import graphene
from .models import Coffee,CoffeeCategory
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

# class CoffeeCategoryType(DjangoObjectType):
#     class Meta:
#         model=CoffeeCategory

class CoffeeNode(DjangoObjectType):
    class Meta:
        model=Coffee
        filter_fields={
            'name':['exact','icontains','istartswith'],
        }
        interfaces=[relay.Node]
         
class CoffeeCategoryNode(DjangoObjectType):
    class Meta:
        model=CoffeeCategory
        filter_fields={
            'id':['exact']
        }
        interfaces=[relay.Node]

         

class Query(graphene.ObjectType):
    all_coffees=DjangoFilterConnectionField(CoffeeNode)
    coffee_categories=DjangoFilterConnectionField(CoffeeCategoryNode)
    category=relay.Node.Field(CoffeeCategoryNode)
