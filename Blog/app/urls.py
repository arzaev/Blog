from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.ArticleListView.as_view(), name='main'),
	path('<slug:slug>/', views.ArticleDetailView.as_view()),
    path('category/<slug:slug>', views.ArticleListCategoryView.as_view()),
]
