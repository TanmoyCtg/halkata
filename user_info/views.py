from django.shortcuts import render

# Create your views here.
def show_user_info(request):
    
    print("request data: ", request.POST)
    if request.method == 'POST':
        user_name = request.POST["user_name"]
        context = {"name":user_name}
        return render(request, 'user_info/user_info.html', context)
    return render(request, 'user_info/user_info.html')
