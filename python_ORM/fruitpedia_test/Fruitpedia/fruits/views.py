from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView, TemplateView

from .forms import CategoryAddForm, AddFruitForm, EditFruitForm, DeleteFruitForm
from .models import Fruit, Category


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits
    }

    return render(request, 'common/dashboard.html', context)


# def create_view(request):
#     if request.method == 'GET':
#         form = AddFruitForm()
#
#     else:  # method is POST
#         form = AddFruitForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'fruits/create-fruit.html', context)


class CreateFruitView(CreateView):
    model = Fruit
    form_class = AddFruitForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')


def edit_view(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }

    return render(request, 'fruits/edit-fruit.html', context)


def details_view(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    context = {
        'fruit': fruit
    }

    return render(request, 'fruits/details-fruit.html', context)


# def delete_view(request, pk):
#     fruit = Fruit.objects.get(pk=pk)
#
#     if request.method == 'GET':
#         form = DeleteFruitForm(instance=fruit)
#     else:
#         fruit.delete()
#         return redirect('dashboard')
#
#     context = {
#         'fruit': fruit,
#         'form': form
#     }
#
#     return render(request, 'fruits/delete-fruit.html', context)


class DeleteFruitView(DeleteView):
    model = Fruit
    form_class = DeleteFruitForm
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object)
        return self.render_to_response(self.get_context_data(form=form, object=self.object))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


def create_category(request):
    if request.method == 'GET':
        form = CategoryAddForm()

    else:  # method is POST
        form = CategoryAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'categories/create-category.html', context)


class FruitTemplateView(TemplateView):
    template_name = 'common/index.html'


class DashBoardView(ListView):
    model = Fruit
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fruits = Fruit.objects.all()
        context['fruits'] = fruits
        return context


class CreateFruitView(CreateView):
    model = Fruit
    form_class = AddFruitForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')


class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryAddForm
    template_name = 'categories/create-category.html'
    success_url = reverse_lazy('dashboard')


class FruitDetailsView(DetailView):
    template_name = 'fruits/details-fruit.html'
    model = Fruit


class FruitEditView(UpdateView):
    model = Fruit
    form_class = EditFruitForm
    success_url = reverse_lazy('dashboard')
    template_name = 'fruits/edit-fruit.html'



