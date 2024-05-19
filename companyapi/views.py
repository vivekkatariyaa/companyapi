from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page resquested")
    friens = ["vivek","pawan","keshav"]
    # HttpResponse("this is homepage")
    return JsonResponse(friens,safe=False)
    pass