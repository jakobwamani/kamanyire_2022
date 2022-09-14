from django.urls import path
from django.conf.urls import include
from feedwork import views
from django.contrib import admin
from django.conf.urls import url

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [

    path('sentry-debug/', trigger_error),
    path('', views.index, name='index'),
    
    path('raw_material_names/',views.setup_raw_material_names,name="setup_raw_materials"),
    path('view_raw_material_names/',views.view_raw_material_names,name="view_raw_material_names"),
    path('update_raw_material_names/',views.update_raw_material_name,name="update_raw_material_names"),
    path('delete_raw_material_names/',views.delete_raw_material_name,name="delete_raw_material_names"),

    path('suppliers/',views.enroll_suppliers,name="setup_suppliers"),
    path('view_suppliers/',views.view_suppliers,name="view_suppliers"),
    path('update_suppliers/',views.update_suppliers,name="update_suppliers"),
    path('delete_suppliers/',views.delete_suppliers,name="delete_suppliers"),

    path('logistics/',views.setup_logistics,name="setup_logistics"),
    path('view_logistics/',views.view_logistics,name="view_logistics"),
    path('update_logistics/',views.update_logistics,name="update_logistics"),
    path('delete_logistics/',views.delete_logistics,name="delete_logistics"),

    path('purchases/',views.execute_purchases,name="purchases"),
    path('view_purchase/',views.see_purchases,name="see_purchases"),
    path('update_purchases/',views.update_purchases,name="update_purchases"),
    path('delete_purchases/',views.delete_purchases,name="delete_purchases"),


    path('execute_raw_material_transactions/',views.execute_raw_material_transactions,name="execute_raw_material_sales"),
    path('view_raw_material_transactions/',views.view_raw_material_transactions,name="view_raw_material_sales"),
    path('update_raw_material_transactions/',views.update_raw_material_transactions,name="update_raw_material_transactions"),
    path('delete_raw_material_transactions/',views.delete_raw_material_transactions,name="delete_raw_material_transactins"),

    path('setup_product_names/',views.setup_product_names,name="setup_product_names"),
    path('view_product_names/',views.view_product_names,name="view_product_names"),
    path('update_product_names/',views.update_product_names,name="update_product_names"),
    path('delete_product_names/',views.delete_product_names,name="delete_product_names"),

    path('products/',views.setup_products,name="setup_products"),
    path('view_products/',views.view_products,name="view_products"),
    path('update_products/',views.update_products,name="update_products"),
    path('delete_products/',views.delete_products,name="delete_products"),

    path('raw_material_separations/',views.setup_raw_material_separations,name="setup_raw_material_separations"),
    path('view_raw_material_separations/',views.view_raw_material_separations,name="view_raw_material_separations"),
    path('update_raw_material_separations/',views.update_raw_material_separations,name="update_raw_material_separations"),
    path('delete_raw_material_separations/',views.delete_raw_material_separations,name="delete_raw_material_separations"),

    path('execute_product_sales/',views.execute_product_sales,name="execute_product_sales"),
    path('view_product_sales/',views.view_product_sales,name="view_product_sales"),
    path('update_product_sales/',views.update_product_sales,name="update_product_sales"),
    path('delete_product_sales/',views.delete_product_sales,name="delete_product_sales"),

    path('expense_names/',views.setup_expense_names,name="setup_expense_names"),
    path('view_expense_names/',views.view_expense_names,name="view_expense_names"),
    path('update_expense_names/',views.update_expense_names,name="update_expense_names"),
    path('delete_expense_names/',views.delete_expense_names,name="delete_expense_names"),

    path('expense_units/',views.setup_expense_units,name="setup_expense_units"),
    path('update_expense_units/',views.update_expense_units,name="update_expense_units"),
    path('view_expense_units/',views.view_expense_units,name="view_expense_units"),
    path('delete_expense_units/',views.delete_expense_units,name="delete_expense_units"),

    path('indirect_expenses/',views.record_expenses,name="record_expenses"),
    path('view_indirect_expenses/',views.view_expenses,name="view_expenses"),
    path('update_indirect_expenses/',views.update_expenses,name="update_expenses"),
    path('delete_indirect_expenses/',views.delete_expenses,name="delete_expenses"),

    path('direct_expenses/',views.record_direct_expenses,name="record_direct_expenses"),
    path('view_direct_expenses/',views.view_direct_expenses,name="view_direct_expenses"),
    path('update_direct_expenses/',views.update_direct_expenses,name="update_direct_expenses"),
    path('delete_direct_expenses/',views.delete_direct_expenses,name="delete_direct_expenses"),

    path('employee/',views.enroll_employee,name="enroll_employees"),
    path('view_employees/',views.see_employees,name="view_employees"),
    path('update_employees/',views.update_employees,name="update_employees"),

    path('employee_terms/',views.make_employee_terms,name="make_employee_terms"),
    path('view_employee_terms/',views.view_employment_terms,name="view_employee_terms"),
    path('update_employment_terms/',views.updating_employment_terms,name="update_employee_terms"),
    path('delete_employement_terms/',views.deleting_employment_terms,name="delete_employment_terms"),

    path('advance/',views.make_advance,name="make_advance"),
    path('view_advance_payments/',views.view_advance,name="view_advances"),
    path('update_advance_payments/',views.update_advance,name="update_advances"),
    path('delete_advance_payments/',views.delete_advance,name="delete_advances"),

    path('salary/',views.pay_salary,name="pay_salary"),
    path('view_salaries/',views.view_salary,name="view_salaries"),
    path('update_salaries/',views.update_salary,name="update_salaries"),
    path('delete_salaries/',views.delete_salary,name="delete_salaries"),

    path('view_stock_balances/',views.view_stock_balance,name="view_stock_balance"),
    path('view_profits/',views.view_profit,name="view_profit"),

    ]