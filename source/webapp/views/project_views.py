from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import SimpleSearchForm, ProjectForm, TaskForm
from django.views.generic import ListView, TemplateView, FormView, DetailView, CreateView

from webapp.models import Project, Task


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'projects'
    model = Project
    paginate_by = 10
    paginate_orphans = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        # form = SimpleSearchForm(self.request.GET)
        # if form.is_valid():
        #     search = form.cleaned_data['search']
        #     kwargs['search'] = search
        # kwargs['form'] = form
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Project.objects.all()
        #
        # is_admin = self.request.GET.get('is_admin', None)
        # if not is_admin:
        #     data = Task.objects.filter('-created_at')
        # form = SimpleSearchForm(data=self.request.GET)
        # if form.is_valid():
        #     search = form.cleaned_data['search']
            # if search:
            #     data = data.filter(Q(title__icontains=search) | Q(description__icontains=search))
        return data.order_by('-start_date_at')


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Project
    paginate_tasks_by = 3
    paginate_tasks_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks, page, is_paginated = self.paginate_tasks(self.object)
        context['tasks'] = tasks
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        print(context)
        return context

    def paginate_tasks(self, project):
        tasks = project.project.all().order_by('-updated_at')
        if tasks.count() > 0:
            paginator = Paginator(tasks, self.paginate_tasks_by, orphans=self.paginate_tasks_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1
            return page.object_list, page, is_paginated
        else:
            return tasks, None, False


class ProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


# class ProjectTaskCreateView(CreateView):
#     model = Project
#     template_name = 'task/task_create.html'
#     form_class = TaskForm
#
#     def form_valid(self, form):
#         task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
#         comment = form.save(commit=False)
#         comment.article = task
#         comment.save()
#         return redirect('task_view', pk=task.pk)