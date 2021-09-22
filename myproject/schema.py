import graphene
from graphene_django import DjangoObjectType

from backend.models import Category, Article

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "slug")

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ("id", "title", "description", "content", "slug", "image", "category", "author")

class Query(graphene.ObjectType):
    all_articles = graphene.List(ArticleType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_articles(root, info):
        # We can easily optimize query count in the resolve method
        return Article.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
schema = graphene.Schema(query=Query)