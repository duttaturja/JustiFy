from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CrimePost, Comment, SharedPost, SavedPost, Vote
from .forms import CrimePostForm, CommentForm

@login_required
def vote_post(request, pk, vote_type):
    post = get_object_or_404(CrimePost, pk=pk)
    # Expect vote_type to be 'up' or 'down'
    try:
        vote = Vote.objects.get(user=request.user, crime_post=post)
        # If the vote already exists and matches the request, do nothing.
        if vote_type == 'up' and vote.vote_type == 1:
            messages.info(request, "You already upvoted this post.")
        elif vote_type == 'down' and vote.vote_type == -1:
            messages.info(request, "You already downvoted this post.")
        else:
            # Otherwise, update the vote_type.
            vote.vote_type = 1 if vote_type == 'up' else -1
            vote.save()
            messages.success(request, "Your vote has been updated.")
    except Vote.DoesNotExist:
        # Create a new vote
        new_vote = Vote.objects.create(
            user=request.user,
            crime_post=post,
            vote_type=1 if vote_type == 'up' else -1
        )
        messages.success(request, "Your vote has been recorded.")
    
    # Redirect back to the post detail page.
    return redirect(post.get_absolute_url())

@login_required
def share_post(request, pk):
    post = get_object_or_404(CrimePost, pk=pk)
    # Create a shared post record
    SharedPost.objects.create(user=request.user, original_post=post)
    post.share_count += 1
    post.save()
    messages.success(request, "Post shared successfully within the website!")
    return redirect('crime:post_detail', pk=pk)

@login_required
def create_crime_post(request):
    if request.method == 'POST':
        form = CrimePostForm(request.POST, request.FILES)
        if form.is_valid():
            crime_post = form.save(commit=False)
            crime_post.user = request.user
            crime_post.save()
            messages.success(request, "Crime post created successfully.")
            return redirect('crime:post_detail', pk=crime_post.pk)
    else:
        form = CrimePostForm()
    return render(request, 'crime/create_post.html', {'form': form})

def post_list(request):
    posts = CrimePost.objects.all().order_by('-post_time')
    return render(request, 'crime/feed.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(CrimePost, pk=pk)
    # Only top-level comments (replies are nested)
    comments = post.comments.filter(parent__isnull=True).order_by('-created_at')
    comment_form = CommentForm()
    return render(request, 'crime/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })

@login_required
def add_comment(request, pk):
    post = get_object_or_404(CrimePost, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.crime_post = post
            comment.user = request.user
            # Check if this is a reply to another comment
            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comment = Comment.objects.filter(id=parent_id).first()
                if parent_comment:
                    comment.parent = parent_comment
            comment.save()
            messages.success(request, "Comment added successfully.")
    return redirect('crime:post_detail', pk=pk)

@login_required
def save_post(request, pk):
    post = get_object_or_404(CrimePost, pk=pk)
    SavedPost.objects.get_or_create(user=request.user, crime_post=post)
    messages.success(request, "Post saved successfully.")
    return redirect('crime:post_detail', pk=pk)

# (Optional) View to handle share actions; typically front-end triggers this and you update share_count.
@login_required
def share_post(request, pk):
    post = get_object_or_404(CrimePost, pk=pk)
    post.share_count += 1
    post.save()
    messages.success(request, "Post shared!")
    return redirect('crime:post_detail', pk=pk)
