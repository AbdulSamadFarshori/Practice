from django.shortcuts import redirect, render
from django.views import View
from.forms import EmployeeForm
# Create your views here.


class IndexView(View):
    template = 'index.html'
    def get(self, request):
        context = {}
        context['form'] = EmployeeForm()
        return render(request, self.template, context)
    
    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')





