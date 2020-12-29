from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Entity, Activity,  Comment
from .forms import EntityForm,ActivityForm,  CommentForm
# Create your views here.

from django.views import generic

from django.contrib.auth import get_user_model
User = get_user_model()

class EntityListView(generic.ListView):
    model = Entity

class EntityDetailView(generic.DetailView):
    model = Entity

class CreateEntityView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    # redirect_field_name = 'entities/entity_detail.html'

    model = Entity
    form_class = EntityForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class UpdateEntityView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    # redirect_field_name = 'entities/entity_detail.html'

    model = Entity
    form_class = EntityForm

class DeleteEntityView(LoginRequiredMixin, generic.DeleteView):
    model = Entity

    success_url = reverse_lazy('entity_list')


class CreateActivityView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    # redirect_field_name = 'entities/entity_detail.html'

    model = Activity
    form_class = ActivityForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ActivityDetailView(generic.DetailView):
    model = Activity



# probably a bad idea to give users power to change the activity, better to let this in admin view
# class UpdateActivityView(LoginRequiredMixin, generic.UpdateView):
#     login_url = '/login/'
#     # redirect_field_name = 'entities/entity_detail.html'
#
#     model = Activity
#     form_class = ActivityForm
#
# class DeleteActivityView(LoginRequiredMixin, generic.DeleteView):
#     model = Activity
#
#     success_url = reverse_lazy('entity_list')



class HomePageView(generic.ListView):
    # model = Entity
    queryset = Entity.objects.all().values('activity').annotate(total=Count('activity')).order_by('total')







#######################################
## Functions that require a pk match ##
#######################################

# @login_required
def add_comment_to_entity(request, pk):
    entity = get_object_or_404(Entity, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.entity = entity
            comment.save()
            return redirect('entity_detail', pk=entity.pk)
    else:
        form = CommentForm()
    return render(request, 'entities/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('entity_detail', pk=comment.entity.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    entity_pk = comment.entity.pk
    comment.delete()
    return redirect('entity_detail', pk=entity_pk)
