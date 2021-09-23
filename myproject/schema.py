import graphene
from graphene_django import DjangoObjectType
from backend.models import Category, Article, Writer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "slug")

class WriterType(DjangoObjectType):
    class Meta:
        model = Writer
        fields = ("id", "name", "picture", "email", "last_update")

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ("id", "title", "description", "content", "slug", "image", "category", 
            "author", "date_created", "date_modified")
        filter_fields = ["image"]

class Query(graphene.ObjectType):
    articles = graphene.List(ArticleType)
    category = graphene.Field(CategoryType, name=graphene.String(required=True))
    writer = graphene.Field(WriterType, name=graphene.String(required=True))
    image = graphene.Field(ArticleType, id=graphene.Int(required=True))

    def resolve_image(self, info, id):
        return Article.objects.get(id=id)

    def resolve_articles(root, info):
        return Article.objects.select_related("category").all()

    def resolve_category(root, info, slug):
        try:
            return Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            return None

    def resolve_writer(root, info, name):
        try:
            return Writer.objects.get(name=name)
        except Writer.DoesNotExist:
            return None

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