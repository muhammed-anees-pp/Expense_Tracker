from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Expense
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'tracker/dashboard.html'
    context_object_name = 'expenses'

    def get_queryset(self):
            return Expense.objects.filter(user=self.request.user).order_by('-date')
    
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Expense
from .forms import ExpenseForm

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'tracker/expense_form.html'
    success_url = reverse_lazy('tracker:dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

from django.views.generic import UpdateView

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'tracker/expense_form.html'
    success_url = reverse_lazy('tracker:dashboard')
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

from django.views.generic import DeleteView

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'tracker/expense_confirm_delete.html'
    success_url = reverse_lazy('tracker:dashboard')
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)