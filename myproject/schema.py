import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene.types import Scalar
import django_filters
from graphene_django import DjangoObjectType
from blog_backend.models import Category, Article, Writer

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "article")

class  CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (graphene.relay.Node , )

class WriterFilter(django_filters.FilterSet):
    class Meta:
        model = Writer
        fields = ("id", "name", "email", "last_update")

class WriterNode(DjangoObjectType):
    class Meta:
        model = Writer
        interfaces = (graphene.relay.Node , )


"""class CategoryType(DjangoObjectType):
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
        filter_fields = ["image"]"""

class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = ("title", "description", "content", "slug", "Category", 
            "author", "date_created", "date_modified")

class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        interfaces = (graphene.relay.Node , )

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "article")

class Query(graphene.ObjectType):
    category = graphene.List(CategoryType)
    node = graphene.relay.Node.Field()
    articles =  DjangoFilterConnectionField(ArticleNode , filterset_class=ArticleFilter)
    article = graphene.relay.Node.Field(ArticleNode)
    categories =  DjangoFilterConnectionField(CategoryNode , filterset_class=CategoryFilter)
    categori = graphene.relay.Node.Field(CategoryNode)
    writers =  DjangoFilterConnectionField(WriterNode , filterset_class=WriterFilter)
    writer = graphene.relay.Node.Field(WriterNode)
    """writer = graphene.Field(WriterType, name=graphene.String(required=True))
    image = graphene.Field(ArticleType, id=graphene.Int(required=True))"""

    def resolve_category(root, info):
        return Category.objects.all()

    """def resolve_articles(root, info):
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

schema = graphene.Schema(query=Query, mutation=Mutation)"""
            
schema = graphene.Schema(query=Query)
