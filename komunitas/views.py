from django.shortcuts import render, redirect
from .models import * 
from .forms import * 

# Create your views here.
def community_main(request):
    community = Community.objects.all()
    count = community.count()
    context = {'community' : community,
                'count' : count}
    return render(request, 'community_main.html', context)
 
def addInCommunity(request):
    form = CreateCommunity()
    if request.method == 'POST':
        form = CreateCommunity(request.POST)
        if form.is_valid():
            community = form.save()
            return redirect('community_detail', join_code=community.join_code)
    context = {'form' : form}
    return render(request, 'addInCommunity.html', context)

def community_detail(request, join_code):
    community = Community.objects.get(join_code=join_code)
    return render(request, 'community_detail.html', {'community': community})

def join_community(request):
    if request.method == 'POST':
        form = JoinCommunityForm(request.POST)
        if form.is_valid():
            join_code = form.cleaned_data['join_code']
            try:
                community = Community.objects.get(join_code=join_code)
                user = request.user
                community.members.add(user)
                return redirect('community_detail', join_code=community.join_code)
            except Community.DoesNotExist:
                # Handle invalid join code
                pass
    else:
        form = JoinCommunityForm()
    context = {'form' : form}
    return render(request, 'join_community.html', context)
