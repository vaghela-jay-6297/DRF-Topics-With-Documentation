from django.urls import path, include
from NestedSerializer_app import views

urlpatterns = [
    # for author classes
    path('author/',  views.AuthorListCreateView.as_view()), 
    path('author/<int:pk>',  views.AuthorRUDView.as_view()),  
    
    # for book classes
    path('book/',  views.BookListCreateView.as_view()),
    path('book/<int:pk>',  views.BookRUDView.as_view()), 

    # for album classes
    path('album/', views.AlbumListView.as_view()),
    path('album/<int:pk>', views.AlbumView.as_view()),

    # for musician classes
    path('musician/', views.MusicianListView.as_view()),
    path('musician/<int:pk>', views.MusicianView.as_view()),
]