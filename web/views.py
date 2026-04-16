from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import user, BlogModel, BlogComment, ContactInfo


class userlst(ListView):
    model = user
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_posts'] = BlogModel.objects.all()
        contact_info, _ = ContactInfo.objects.get_or_create(pk=1)
        context['contact_info'] = contact_info
        return context


def blog_list(request):
    posts = BlogModel.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogModel, slug=slug)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'like':
            post.likes += 1
            post.save(update_fields=['likes'])
            return redirect('blog_detail', slug=post.slug)

        if action == 'comment':
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            content = request.POST.get('content', '').strip()

            if name and content:
                BlogComment.objects.create(
                    blog=post,
                    name=name,
                    email=email,
                    content=content,
                )
            return redirect('blog_detail', slug=post.slug)

    return render(request, 'blog_detail.html', {'post': post})