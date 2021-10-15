import graphene
from graphene.types import Scalar
from graphene_django import DjangoObjectType
from blog_backend.models import Category, Article, Writer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "article")

class WriterType(DjangoObjectType):
    class Meta:
        model = Writer
        fields = ("id", "name", "picture", "email", "last_update")


class FileField(Scalar):
    @staticmethod
    def serialize(value):
        if not value:
            return ""
        return value.url

    @staticmethod
    def parse_literal(node):
        return node

    @staticmethod
    def parse_value(value):
        return value

class ArticleType(DjangoObjectType):
    image = FileField()
    class Meta:
        model = Article
        fields = ("id", "title", "description", "content", "slug", "image", "Category", 
            "author", "date_created", "date_modified")
        filter_fields = ["image"]

class Query(graphene.ObjectType):
    articles = graphene.List(ArticleType)
    article = graphene.Field(ArticleType, slug=graphene.String(required=True))
    category = graphene.List(CategoryType)
    categories = graphene.Field(CategoryType, slug=graphene.String(required=True))
    writer = graphene.Field(WriterType, name=graphene.String(required=True))
    image = graphene.Field(ArticleType, id=graphene.Int(required=True))

    def resolve_articles(root, info):
        return Article.objects.select_related("Category").all()

    def resolve_article(root, info, slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            return None

    def resolve_category(root, info):
        return Category.objects.all()

    def resolve_categories(root, info, slug):
        try:
            return Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            return None

    def resolve_writer(root, info, name):
        try:
            return Writer.objects.get(name=name)
        except Writer.DoesNotExist:
            return None
    
    def resolve_image(self, info, id):
        return Article.objects.get(id=id)

class Image(graphene.Mutation):
    image = graphene.Field(ArticleType)
    @classmethod
    def mutate(cls, root, info):
        files = info.context.FILES['imageFile']
        imgobj = Article(image=files)
        imgobj.save()
        return Image(profile_image=imgobj)

class Mutation(graphene.ObjectType):
    image = Image.Field()
            
schema = graphene.Schema(query=Query, mutation=Mutation)
