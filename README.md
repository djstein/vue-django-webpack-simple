# Vue.js and Django Web Application

- use of Vue.js in component form
- Webpack building the JavaScript application
- Django serving builds with django-wepack-loader

##Installation
```bash
# Virtual environment
virtualenv -p python3 env
source env/bin/activate

pip install -r requirements.txt
npm install
```

## Development
```bash
# Run Django server
python manage.py runserver

# Run node server
npm run watch
```

## Webpack Build
```bash
# Local Build
npm run build

# Production Build
npm run build-production
```

# Build the JavaScript Package
npm run build

# Run Django server
python manage.py runserver
```

## Sources 
Any changes made to `assets/js/App.vue` will now be seen automatically.

Compilation of these resources:

https://github.com/vuejs-templates/webpack-simple/tree/master/template

https://github.com/owais/django-webpack-loader/tree/master/examples

## Contributions
Please feel free to pull, fork, or add suggestions