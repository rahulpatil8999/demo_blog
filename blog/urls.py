from django.urls import path
from blog import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("user", views.UserCRUDOps)
router.register("post", views.PostCRUDOps)
router.register("comment",views.CommentCRUDOps)

urlpatterns = router.urls