from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View, TemplateView, FormView
from .models import Task
from .forms import TaskForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()
        context['tasks'] = tasks
        return context


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context['task'] = task
        return context


class TaskCreateView(FormView):
    template_name = 'task_create.html'
    form_class = TaskForm

    def form_valid(self, form):
        data = {}
        type = form.cleaned_data.pop('type')
        for key, value in form.cleaned_data.items():
            if value is not None:
                data[key] = value
        self.tasks = Task.objects.create(**data)
        self.tasks.type.set(type)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.tasks.pk})

    # def get(self, request):
    #     return render(request, 'task_create.html', context={
    #         'form': TaskForm()
    #     })
    #
    # def post(self, request):
    #     form = TaskForm(data=request.POST)
    #     if form.is_valid():
    #         data = {}
    #         for key, value in form.cleaned_data.items():
    #             if value is not None:
    #                 data[key] = value
    #         task = Task.objects.create(**data)
    #         return redirect('task_view', pk=task.pk)
    #     else:
    #         return render(request, 'task_create.html', context={
    #             'form': form
    #         })


class TaskUpdateView(FormView):
    template_name = 'task_update.html'
    form_class = TaskForm


    def dispatch(self, request, *args, **kwargs):
        self.tasks = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.tasks
        return context

    def get_initial(self):
        initial = {}
        for key in 'summary', 'description', 'status':
            initial[key] = getattr(self.tasks, key)
        initial['type'] = self.tasks.type.all()
        return initial

    def form_valid(self, form):
        type = form.cleaned_data.pop('type')
        for key, value in form.cleaned_data.items():
            if value is not None:
                setattr(self.tasks, key, value)
        self.tasks.save()
        self.tasks.type.set(type)
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('index', kwargs={'pk': self.tasks.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)


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


class TaskDeleteView(TemplateView):
    template_name = 'task_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context['task'] = task
        return context

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')