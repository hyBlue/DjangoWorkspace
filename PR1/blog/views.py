from django.shortcuts import render, get_object_or_404, redirect
import os
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import Post
from .forms import PostForm
from django.http import Http404
# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html ')

#파일 다운로드
def download(request):
    filepath = os.path.join(settings.BASE_DIR, 'hello.txt')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = '') # content - type 기본은 txt/html
        response['Content-Disposition'] = 'attachment; filename = "{}"'.format(filename)
        return response

#검색기능 구현
def post_list(request):
    qs = Post.objects.all()


    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'blog/post_list.html', { 'post_list' : qs, 'q' : q} )

def post_posting(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            #messages.add_message(request, messages.INFO, '새 글이 등록되었습니다.')
            messages.info(request, '새 글이 등록되었습니다.') # 메세지 등록만 하는 코드임.
            # 소비하는 코드는 템플릿에 넣어줘야함.

            #저장을 form 내에서 안할때는 commit = False 인자로 전달.
            #return redirect('blog:post_detail', post.id)
            return redirect(post) # get_absolute_url 이 post 내 구현 되어있음
        else:
            form.errors
    else: #Get 요청일 때
        form = PostForm()
    return render(request, 'blog/post_posting.html', {'form' : form})
def post_edit(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            messages.info(request, '글이 수정되었습니다.')

            return redirect('blog:post_detail', post.id)
        else:
            form.errors
    else: #Get 요청일 때
        form = PostForm(instance = post)
    return render(request, 'blog/post_posting.html', {'form' : form})
def post_detail(request, id):
    """
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        raise Http404
    """
    #아래 코드와 동일
    post = get_object_or_404(Post, id= id) # 지정 레코드가 없을 경우 404에러 발생
    return render(request, 'blog/post_detail.html', {
        'post':post,
         })