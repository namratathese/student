# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# # Create your views here.
# def movie_list(request):
#     movies=Movie.objects.all()
#     data={'movies':list(movies.values())} #jsonresponse for all element

#     return JsonResponse(data)

# #jsonresponse for individual element
# def movie_details(request,pk):
#     movie=Movie.objects.get(pk=pk)
#     data={
#         'name':movie.name,
#         'description':movie.description,
#         'activate':movie.active
#     }
#     return JsonResponse(data)
    