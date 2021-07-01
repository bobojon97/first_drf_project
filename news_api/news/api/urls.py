from django.urls import path
from news.api.views import ArticleDetailAPIView, ArticleListCreateAPIView, JournlistListCreateAPIView

# from news.api.views import article_list_create_api_view, article_detail_api_view

urlpatterns = [
    path('articles/', ArticleListCreateAPIView.as_view(), name='articles-list'),
    path("articles/<int:pk>", ArticleDetailAPIView.as_view(), name='articles-detail'),
    path('journalists/', JournlistListCreateAPIView.as_view(), name='journalist-list'),

    # path('articles/', article_list_create_api_view, name='articles_list'),
    # path("articles/<int:pk>", article_detail_api_view, name='articles_detail'),
]