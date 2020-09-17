from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, FormView, CreateView, DeleteView, UpdateView
from webapp.models import Task, Project
from webapp.forms import TaskForm, SimpleSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# class IndexView(ListView):
#     template_name = 'index.html'
#     context_object_name = 'tasks'
#     paginate_by = 10
#     paginate_orphans = 2
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         form = SimpleSearchForm(self.request.GET)
#         if form.is_valid():
#             search = form.cleaned_data['search']
#             kwargs['search'] = search
#         kwargs['form'] = form
#         return super().get_context_data(object_list=object_list, **kwargs)
#
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     tasks = Task.objects.all()
#     #     context['tasks'] = tasks
#     #     return context
#
#     def get_queryset(self):
#         data = Task.objects.all()
#         #
#         # is_admin = self.request.GET.get('is_admin', None)
#         # if not is_admin:
#         #     data = Task.objects.filter('-created_at')
#         form = SimpleSearchForm(data=self.request.GET)
#         if form.is_valid():
#             search = form.cleaned_data['search']
#             if search:
#                 data = data.filter(Q(summary__icontains=search) | Q(description__icontains=search))
#         return data.order_by('-created_at')


class TaskView(TemplateView):
    template_name = 'task/task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context['task'] = task
        return context


# class ProjectTaskCreateView(FormView):
#     template_name = 'task/task_create.html'
#     form_class = TaskForm
#
#     def form_valid(self, form):
#         self.tasks = form.save()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('task_view', kwargs={'pk': self.tasks.pk})
#
#     def get(self, request):
#         return render(request, 'task_create.html', context={
#             'form': TaskForm()
#         })
#
#     def post(self, request):
#         form = TaskForm(data=request.POST)
#         if form.is_valid():
#             data = {}
#             for key, value in form.cleaned_data.items():
#                 if value is not None:
#                     data[key] = value
#             task = Task.objects.create(**data)
#             return redirect('task_view', pk=task.pk)
#         else:
#             return render(request, 'task_create.html', context={
#                 'form': form
#             })

# class TaskUpdateView(FormView):
#     template_name = 'task/task_update.html'
#     form_class = TaskForm
#
#
#     def dispatch(self, request, *args, **kwargs):
#         self.tasks = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tasks'] = self.tasks
#         return context
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['instance'] = self.tasks
#         return kwargs
#
#     def form_valid(self, form):
#         self.tasks = form.save()
#         return super().form_valid(form)
#
#
#     def get_success_url(self):
#         return reverse('project_view', kwargs={'pk': self.project.pk})
#
#     def get_object(self):
#         pk = self.kwargs.get('pk')
#         return get_object_or_404(Task, pk=pk)


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     pk = self.kwargs.get('pk')
    #     task = get_object_or_404(Task, pk=pk)
    #
    #     initial = {}
    #     for key in 'summary', 'description', 'status', 'type':
    #         initial[key] = getattr(task, key)
    #     form = TaskForm(initial=initial)
    #
    #     context['task'] = task
    #     context['form'] = form
    #
    #     return context
    #
    # def post(self, request, pk):
    #     task = get_object_or_404(Task, pk=pk)
    #     form = TaskForm(data=request.POST)
    #     if form.is_valid():
    #         for key, value in form.cleaned_data.items():
    #             if value is not None:
    #                 setattr(task, key, value)
    #         task.save()
    #         return redirect('task_view', pk=task.pk)
    #     else:
    #         return self.render_to_response({
    #             'task': task,
    #             'form': form
    #         })


class TaskUpdateView(UserPassesTestMixin, UpdateView):
    model = Task
    template_name = 'task/task_update.html'
    form_class = TaskForm
    # context_object_name = 'task'

    def test_func(self):
        return self.request.user.has_perm('webapp.update_task') and self.request.user in self.get_object().project.user.all()

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})

# class TaskDeleteView(TemplateView):
#     template_name = 'task/task_delete.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         pk = self.kwargs.get('pk')
#         task = get_object_or_404(Task, pk=pk)
#         context['task'] = task
#         return context
#
#     def post(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         task.delete()
#         return redirect('index')


class TaskDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'task/task_delete.html'
    model = Task
    context_object_name = 'task'

    def test_func(self):
        return self.request.user.has_perm('webapp.delete_task') and self.request.user in self.get_object().project.user.all()

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pk = self.kwargs.get('pk')
    #     task = get_object_or_404(Task, pk=pk)
    #     context['task'] = task
    #     return context
    #
    # def post(self, request, pk):
    #     task = get_object_or_404(Task, pk=pk)
    #     task.delete()
    #     return redirect('index')


class ProjectTaskCreateView(UserPassesTestMixin, CreateView):
    model = Task
    template_name = 'task/task_create.html'
    form_class = TaskForm

    def test_func(self):
        return self.request.user.has_perm('webapp.delete_task') and self.request.user in self.get_object().project.user.all()



    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('project_view', pk=project.pk)





