from django.urls import path
from .views import TodoApiView, TodoUpdateApiView, TodoIsCheckApiView, TodoCheckApiView, TodoFilterApiView, UserApiView

urlpatterns = [
    path('todo/', TodoApiView.as_view()),
    path('todo/<int:pk>/', TodoUpdateApiView.as_view()),
    path('todo/isCheck/', TodoIsCheckApiView.as_view()),
    path('todo/check/', TodoCheckApiView.as_view()),
    path('todo/filter/', TodoFilterApiView.as_view()),
    path('user/', UserApiView.as_view()),


    # path('todo/', TodoCreateApiView.as_view()),
    # path('todo/create/<int:pk>/', TodoUpdateApiView.as_view()),
    # path('todo/isCheck/', TodoListIsCheckView.as_view()),
    # path('todo/check/', TodoListCheckView.as_view()),
    # path('todo/filter/', TodoFilterApiView.as_view()),
]
