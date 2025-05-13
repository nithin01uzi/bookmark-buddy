from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Bookmark
from .forms import BookmarkForm

@login_required
def add_bookmark(request):
    if Bookmark.objects.filter(user=request.user).count() >= 5:
        return render(request, 'bookmarks/error.html', {'message': 'You can only add 5 bookmarks.'})
    
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.save()
            return redirect('list_bookmarks')
    else:
        form = BookmarkForm()
    return render(request, 'bookmarks/add_bookmark.html', {'form': form})

@login_required
def list_bookmarks(request):
    bookmarks_list = Bookmark.objects.filter(user=request.user).order_by('-added_at')
    paginator = Paginator(bookmarks_list, 1)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bookmarks/list_bookmarks.html', {'page_obj': page_obj})

@login_required
def edit_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, id=bookmark_id, user=request.user)
    if request.method == 'POST':
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
            return redirect('list_bookmarks')
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'bookmarks/edit_bookmark.html', {'form': form})


@login_required

def delete_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, id=bookmark_id, user=request.user)
    bookmark.delete()
    return redirect('list_bookmarks')

@login_required
def search_bookmarks(request):
    query = request.GET.get('q')
    if query:
        bookmarks = Bookmark.objects.filter(user=request.user, title__icontains=query) | Bookmark.objects.filter(user=request.user, url__icontains=query)
    else:
        bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmarks/search_results.html', {'bookmarks': bookmarks})


