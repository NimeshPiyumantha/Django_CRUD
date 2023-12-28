# Django_CRUD

### Python Django + PostgreSQL

### install libs

```
pip install django
pip install djangorestframework
pip install django-cors-headers
```

### project create

```
python -m django startproject django_backend
django-admin startproject <name of the project>
```

### run server

```
python manage.py runserver
```

### to create an app

```
 python manage.py startapp <the name of the app>
```

### Next let us register the app and the required modules in settings.py file.

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'EmployeeApp.apps.EmployeeappConfig'
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```

### install postgres

```
pip install psycopg2
```

### Lets write the command to make migrations file for our models.

```
python manage.py makemigrations <app name>
```

### Once it looks fine, we can execute the command to push these changes to the database.

```
python manage.py migrate <app name>
```

## Links

- 🔗 <a href="https://documenter.getpostman.com/view/21678240/2s9Ykraz2T" target="_blank">PostMan Page 1</a>

- 🔗 <a href="https://documenter.getpostman.com/view/21678240/2s9Ykraz2U" target="_blank">PostMan Page 2</a>

### Clone this repository ✅

```md
https://github.com/NimeshPiyumantha/Django_CRUD.git
```

## Connect with me

#### If you have any bugs or issues , If you want to explain my code please contact me on :

<div align="center">
 <br><b>MAIL ME</b>&nbsp;
  <a href="mailto:nimeshpiyumantha11@gmail.com">
      <img width="20px" src="https://github.com/NimeshPiyumantha/red-alpha/blob/main/gmail.svg" />
  </a></p>

 </div>

<p align="center">
<a href="https://twitter.com/NPiyumantha60"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="__NimeshPiyumantha__" height="30" width="40" /></a>
<a href="https://www.linkedin.com/in/nimesh-piyumantha-33736a222" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile" height="30" width="40" /></a>
<a href="https://www.facebook.com/profile.php?id=100025931563090" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Nimesh Piyumantha" height="30" width="40" /></a>
<a href="https://www.instagram.com/_.nimmaa._/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="_.nimmaa._" height="30" width="40" /></a>
</p>

##

<div align="center">

![repo license](https://img.shields.io/github/license/NimeshPiyumantha/Django_CRUD?&labelColor=black&color=3867d6&style=for-the-badge)
![repo size](https://img.shields.io/github/repo-size/NimeshPiyumantha/Django_CRUD?label=Repo%20Size&style=for-the-badge&labelColor=black&color=20bf6b)
![GitHub forks](https://img.shields.io/github/forks/NimeshPiyumantha/Django_CRUD?&labelColor=black&color=0fb9b1&style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/NimeshPiyumantha/Django_CRUD?&labelColor=black&color=f7b731&style=for-the-badge)
![GitHub LastCommit](https://img.shields.io/github/last-commit/NimeshPiyumantha/Django_CRUD?logo=github&labelColor=black&color=d1d8e0&style=for-the-badge)

</div>

<div align="center">

#### @2023 [Nimesh Piyumantha](https://github.com/NimeshPiyumantha/), Inc.All rights reserved

</div>
