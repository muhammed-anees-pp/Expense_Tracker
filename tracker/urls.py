from django.urls import path
from . import views

app_name = 'tracker'  # Namespacing the URLs

urlpatterns = [
    # Dashboard view (list of expenses)
    path('', views.DashboardView.as_view(), name='dashboard'),

    # Add expense
    path('add/', views.ExpenseCreateView.as_view(), name='add_expense'),

    # Edit expense
    path('edit/<int:pk>/', views.ExpenseUpdateView.as_view(), name='edit_expense'),

    # Delete expense
    path('delete/<int:pk>/', views.ExpenseDeleteView.as_view(), name='delete_expense'),
]