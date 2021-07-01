from customUsers.models import User
from blogs.models import Comments, Post
from django.views import generic
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from .decorators import get_query, query_debugger
from .forms import LogInForm, SignUpForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class HomePage(generic.ListView):
    template_name = 'blogs/home.html'
    model = Post

    def get(self, request):
        context = {}
        all_posts = Post.objects.all()
        paginator = Paginator(all_posts, 2)
        page = request.GET.get('page', 1)
        context["page"] = page
        try:
            context["posts"] = paginator.page(page)
        except PageNotAnInteger:
            context["posts"] = paginator.page(1)
        except EmptyPage:
            context["posts"] = paginator.page(paginator.num_pages)
        return render(request, 'blogs/home.html', context)

class DetailPage(generic.DetailView):
    template_name = 'blogs/read.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        del context['object']
        context['reply_to_comments'] = self.reply_to_comments
        context['reply_to_reply'] = self.reply_to_reply
        context.update(self.context_data)
        return context


    @get_query
    # @query_debugger
    def get(self, request, *args, **kwargs):
        context_data = {}
        all_comments = self.comments
        paginator = Paginator(all_comments, 3)
        page = request.GET.get('page', 1)
        context_data["page"] = page
        try:
            context_data["comments"] = paginator.page(page)
        except PageNotAnInteger:
            context_data["comments"] = paginator.page(1)
        except EmptyPage:
            context_data["comments"] = paginator.page(paginator.num_pages)
        self.context_data = context_data
        return super().get(request, *args, **kwargs)

class RegisterView(generic.CreateView):
    template_name = 'auth/register.html'
    model = User
    form_class = SignUpForm

    def get_success_url(self) -> str:
        return reverse('home')


class LogInView(generic.View):

    def get(self, request):
        context = {}
        form = LogInForm(request.POST)
        context['form'] = form
        return render(request, 'auth/login.html', context)

    def post(self, request):
        context = {
            'data': request.POST,
            'has_error': False
        }
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if not user and not context['has_error']:
            messages.add_message(request, messages.ERROR, 'Invalid login')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'auth/login.html', status=401, context=context)
        login(request, user)
        return redirect('home')

class LogOutView(generic.View):
    
    def get(self, request):
        logout(request)
        messages.add_message(request, messages.SUCCESS, "Logout successfully")
        return redirect('home')