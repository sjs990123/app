from django.shortcuts import render
from .models import Post,SearchList
from django.views.generic import ListView, DetailView
from django.db.models import Q

# Create your views here.

# [CBV:Class Based View]
class Search(ListView):
    model = SearchList

    def get_queryset(self):
        lt = SearchList.objects.order_by('-data')
        print('searchList>>', lt)

        return lt


class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostSearch(PostList):
    def get_queryset(self):
        q = self.kwargs['question']

        object_list = Post.objects.filter(Q(title__contains=q) | Q(content__contains=q))
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostSearch, self).get_context_data()
        context['search_info'] = 'Search Result >> {}'.format(self.kwargs['question'])

        s = SearchList(searchword=self.kwargs['question'])
        s.save()



        return context


# [FBV : Function Based View]---------------
# def post_detail(request, pk):
#     blog_post = Post.objects.get(pk=pk)
#     context={
#         'blog_post': blog_post,
#     }
#     return render(request, 'blog/post_detail.html', context)

#
# def index(request):
#     post = Post.object.all()
#     context = {
#         'post': post,
#     }
#
#     return render(request, 'blog/index.html',context)
#
# -----------
