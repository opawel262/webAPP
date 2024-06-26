from django.urls import path, include
from api.views import CreateUserView, UserListView, NoteListView, NoteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', CreateUserView.as_view(), name='user-create'),
    path('users/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('users/token/verfiy/', TokenVerifyView.as_view(), name='token-verify'),
    path("api-auth/", include("rest_framework.urls")),
    path('users/notes/', NoteListView.as_view(), name='note-list'),
    path('users/note/<int:pk>/', NoteView.as_view(), name='note-detail'),
]

