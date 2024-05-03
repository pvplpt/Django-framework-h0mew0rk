import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    text = """
    <h1><a href="about/">Мое</a> первое приложение на Django!</h1>
    <h3>Для запуска выполнил следующее:</h3>
    <p>Создал виртуальное окружение: <b>python3 -m venv ~/.venvDjango</b></p>
    <p>Активировал виртуальное окружение: <b>source ~/.venvDjango/bin/activate</b></p>
    <p>Установил Django:<b> pip install django</b></p>
    <p>В папке <b>Django-framework-h0mew0rk</b> создал проект: <b>django-admin startproject h0mew0rk</b></p>
    <p>Добавил ip в файл settings.py: <b>ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.5',]</b></p>
    <p>Сменил текущую папку на папку проекта: <b>cd h0mew0rk</b></p>
    <p>Запустил сервер: <b>python3 manage.py runserver 0.0.0.0:8000</b></p>
    <p>Проверил, что сервер запускается и доступен со смартфона:<b> http://192.168.1.5:8000/</b></p>
    <p>Остановил сервер:<b> Ctrl+C</b></p>
    <p>Создал приложение: <b>python3 manage.py startapp les1app</b></p>
    <p>Сразу добавил приложение в файл проекта settings.py: <b>INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'les1app',]</b></p>
    <p>Создал представления в приложении в файле <b>views.py</b></p>
    <p>Настроил пути в файле проекта <b>urls.py</b>: <b>urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('les1app.urls')),]</b></p>
    <p>Создал файл <b>urls.py</b> в папке приложения: <br>
    <b>from django.urls import path</b><br>
    <b>from . import views</b><br>
    <b>urlpatterns = [<br>
    path('', views.index, name='index'),<br>
    path('about/', views.about, name='about'),<br>]</b></p>
    <p>Проверил работоспособность: <b>http://192.168.1.5:8000/</b><br>
    <b>http://192.168.1.5:8000/about/</b></p>
    <p>Подключил логирование</p>
    """
    logger.info('Index page accessed')
    return HttpResponse(text)


def about(request):
    text = """
    <h1>Обо мне</h1>
    <h2>Поздняков Павел Петрович</h2>
    <h3>Студент GeekBrains</h3>
    <h4>Специализация: Разработчик-Программист</h4>
    <h5>Технологическая специализация: Разработчик-Веб-разработка на Python</h5>
    <h6>Прохожу курс: Фреймворк Django</h6>
    """
    logger.debug('About page accessed')
    return HttpResponse(text)

