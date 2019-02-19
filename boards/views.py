from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTopicForm
from .models import Category, Topic, Post

def home(request):
    boards = Category.objects.all()
    return render(request, 'home_forum.html', {'boards': boards})
	
def board_topics(request, pk):
    board = get_object_or_404(Category, pk=pk)
    return render(request, 'topics.html', {'board': board})
	
def new_topic(request, pk):
    board = get_object_or_404(Category, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.category = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})