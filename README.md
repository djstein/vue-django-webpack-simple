# Vue.js and Django Web Application

- use of Vue.js in component form
- Webpack building the JavaScript application
- Django serving builds with django-wepack-loader

##Installation
```bash
# Virtual environment
virtualenv env
. env/bin/activate

pip install -r requirements.txt
npm install
```

## Run Servers
```bash
# Run Django server
./manage.py runserver

# Run node server
node server.js
```

## Sources 
Any changes made to `assets/js/App.vue` will now be seen automatically.

Compilation of these resources:

https://github.com/vuejs-templates/webpack-simple/tree/master/template

https://github.com/owais/django-webpack-loader/tree/master/examples