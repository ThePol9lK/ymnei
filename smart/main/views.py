from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course, PreSchool, ExtraClass
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from .forms import ContactForm


# # Отправка письма
# def submit_form(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         phone = request.POST.get('phone', '')
#
#         # Отправка письма
#         send_mail(
#             'Новая заявка',
#             f'Имя: {name}\nНомер телефона: {phone}',
#             'ваш_email@gmail.com',
#             ['получатель@gmail.com'],
#             fail_silently=False,
#         )
#
#         return HttpResponseRedirect('')  # Перенаправление на страницу успешной отправки
#     else:
#         return render(request, "main/index.html")


class CourseDetailView(DetailView):
    model = Course
    template_name ='main/one-course.html'
    context_object_name = 'desk'

    def get_object(self):
        title = self.kwargs.get('title')
        return get_object_or_404(Course, title=title)

class PreSchoolDetailView(DetailView):
    model = PreSchool
    template_name ='main/one-course.html'
    context_object_name = 'desk'

    def get_object(self):
        title = self.kwargs.get('title')
        return get_object_or_404(PreSchool, title=title)

class ExtraClasslDetailView(DetailView):
    model = ExtraClass
    template_name ='main/one-course.html'
    context_object_name = 'desk'

    def get_object(self):
        title = self.kwargs.get('title')
        return get_object_or_404(ExtraClass, title=title)

def index(request):
    return render(request, "main/index.html")

def course(request):
    courses = Course.objects.all()
    preSchool = PreSchool.objects.all()
    extraClass = ExtraClass.objects.all()

    # Cоединение бд для последующей пердачи на страницу
    context = {
        'courses': courses,
        'preSchool': preSchool,
        'extraClass': extraClass,
    }
    return render(request, "main/course.html", context)




def about(request):
    return render(request, "main/about.html")

def contatcs(request):
    return render(request, "main/contacts.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = 'Имя: {}\nТелефон: {}'.format(name, phone)
            send_mail(
                'Новое сообщение от пользователя',
                message,
                'ssmart.4dmin@yandex.ru', # Адрес отправителя
                ['master_yoda_man@mail.ru'], # Адрес получателя
                #пороль : max214zet
                fail_silently=False,
            )
            return render(request, 'main/index.html')
    else:
        form = ContactForm()
    return render(request, 'main/index.html', {'form': form})

