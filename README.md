## eclipseteam
# Description project:

backend for EclipseShop project of E-commerce, this made with django-rest-framework and postgresql

# DJANGO REST FRAMEWORK
API-REST de las prendas, login

## Install backend Desparche


/1. Download python version 3.4 LTS

# install environment virtual:

pip install virtualenv

*********** tambien, para administrar facilmente los ambientes virtuales:
   pip install virtualenvwrapper(linux)
   pip install virtualenvwrapper-win(windows) 


#crear virtualenv:

mkvirtualenv #tiendaeclipse -p C:\Python34\python.exe
#activate: 

workon tiendaeclipse

# Dentro del directorio del repo clonado eclipseteam, instalar tools:

pip install -r requeriments.txt


# por ultimo correr el servidor:


python manage.py runserver
