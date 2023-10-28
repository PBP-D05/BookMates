# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
# from django.urls import reverse
# from django.core import serializers
# from django.views.decorators.csrf import csrf_exempt



# # Create your views here.
# def show_main(request):
#     context = {
#         'name': request.user,
#     }

#     return render(request, "dashboard_user.html", context)

# @csrf_exempt
# def sort_ajax(request):
#     order_by=""
#     if request.method == 'POST':
#         order_by_value = request.POST.get('order_by')
#         if order_by_value == '1':
#             order_by = "ascending"
#         elif order_by_value == '2':
#             order_by = "descending"
#         else:
#             order_by = request.GET.get('order_by', 'ascending')
#     else:
#         order_by = request.GET.get('order_by', 'ascending')
        
#     sorted_books = get_katalog(order_by)
    
#     return HttpResponse(serializers.serialize('json',sorted_books))
