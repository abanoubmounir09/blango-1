




from django.urls import path

from blog.api_views import post_list, post_detail,PostList, PostDetail
from rest_framework.urlpatterns import format_suffix_patterns

"""urlpatterns = [
    path("posts/", post_list, name="api_post_list"),
    path("posts/<int:pk>/", post_detail, name="api_post_detail"),
]"""

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
]

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token)
]

urlpatterns = format_suffix_patterns(urlpatterns)
