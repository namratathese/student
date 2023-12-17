
from django.urls import path,include
from rest_framework.routers import DefaultRouter
#from watchlist_app.api.views import movie_list,movie_details   #=======fun based views name========

#WatchListGV,StreamPlatformAV,StreamPlatformDetailAV
from watchlist_app.api.views import (WatchListAV,WatchDetailAV,
                                     StreamPlatformVS,
                                     ReviewList,ReviewDetail,ReviewCreate,UserReview)
# ========[MovieListAV,MovieDetailAV]=============



#==========================use of routers instead of urls-paths==============
router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

#====================================urls paths=========================
urlpatterns = [
    path('', WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>/',WatchDetailAV.as_view(),name='movie-detail'),
    #path('list2/',WatchListGV.as_view(),name='watch-list'),
    
    path('',include(router.urls)),
    
#----------16-12-23----
    path('<int:pk>/reviews/create/',ReviewCreate.as_view(),name='review-create'),

    path('<int:pk>/reviews/',ReviewList.as_view(),name='review-list'),
    path('reviews/<int:pk>/',ReviewDetail.as_view(),name='review-detail'),
    
    path('user-reviews/',UserReview.as_view(),name='user-review-detail'),
    
    
]   



#====================================================================================
    #path('stream/',StreamPlatformAV.as_view(),name='stream'),
    #path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='streamplatform-detail'),
    
    # path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),

    # path('stream/<int:pk>/review',ReviewList.as_view(),name='review-list'),
    # path('stream/review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),
    
#========================================================================================
