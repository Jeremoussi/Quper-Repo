from django.urls import path
from . import views


urlpatterns = [
    path('',views.EntityListView.as_view(), name = 'entity_list'),
    path('entity/<int:pk>',views.EntityDetailView.as_view(), name = 'entity_detail'),
    path('entity/new',views.CreateEntityView.as_view(), name = 'entity_new'),
    path('entity/<int:pk>/remove/', views.DeleteEntityView.as_view(), name='entity_remove'),
    path('entity/<int:pk>/update/', views.UpdateEntityView.as_view(), name='entity_update'),

    path('activity/new',views.CreateActivityView.as_view(), name = 'activity_new'),
    path('activity/<int:pk>',views.ActivityDetailView.as_view(), name = 'activity_detail'),

    path('homepage',views.HomePageView.as_view(template_name='homepage.html'), name = 'homepage'),

    path('entity/<int:pk>/comment/', views.add_comment_to_entity, name='add_comment_to_entity'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
