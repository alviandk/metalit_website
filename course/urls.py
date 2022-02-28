from django.urls import path
from . import views
from .views import CourseView

urlpatterns = [
    path('api/course/', CourseView.as_view()),
    path('api/course/<slug>', CourseView.as_view()),
    path('api/course/', views.CourseView),
    path('api/course/<slug>', views.CourseView),
    path("<cart_id>/delete", views.delete, name="delete"),
	path("cart", views.cart, name="cart"),
	path("checkout", views.checkout, name="checkout"),
    path("course", views.course, name="course"),
    path("<slug>", views.detail, name="detail"),
    path("course_added/<cart_id>", views.add_to_cart, name="add_to_cart")
]