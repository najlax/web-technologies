from django.shortcuts import render
from .models import Student , Address

# Create your views here.


def std(request):
  objs= Address.objects.all()
  for obj in objs:
    obj.num_students = Student.objects.filter(address=obj).count()

  return render(request, 'usermodule/shoestd.html', {'studetns': objs})