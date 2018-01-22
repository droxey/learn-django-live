# learn-django-live

## Purpose

This repo contains the source for Django demonstration during the Week 21: Python and Django unit.

All code written live during class on 1/18/2018 (21.2) and 1/20/2018 (21.3).

## Setup

1. Clone the repository: `git clone git@github.com:outputs-io/learn-django-live.git`
1. Navigate to the freshly cloned directory: `cd learn-django-live`
1. Create and activate a new virtualenv via `virtualenv`:
  1. `virtualenv env`
  1. `source env/bin/activate`
1. Install Django in your new virtualenv: `pip install django`
1. Navigate to the root Django project: `cd proj`
1. Run migrations: `python manage.py migrate`
1. Run the Django development server: `python manage.py runserver`
1. Navigate to http://127.0.0.1:8000/tasks/list/ in your browser to view the Tasks user interface.
1. When done developing, deactivate the virtualenv: `deactivate`

## Notes

This repo is a work in progress, and covers the following (basic!) Django topics:
- **App Creation**
  - Creating a new `tasks` app via `python manage.py startapp tasks`.
  - Editing `settings.py` to add the new app.
  - Including an app's `urls.py` in the root URLconf.
- **Models**
  - Basic field types.
  - Model migrations.
  - Registering new models in the admin interface in `admin.py`.
- **Views**
  - Importing a model into `views.py`.
  - Rendering a Django template using `render`.
  - Querying the Django ORM within a view.
  - Passing the resulting `QuerySet` to a custom template.
  - Passing additional variables to the template.
  - Simple HTML responses via `HttpResponse`.
  - Gluing views to URLs via the `urlpatterns`  array in `urls.py`.
- **Templates**
  - Base templates.
  - Child templates using `{% extends "base.html" %}`.
  - Injecting child templates content into parent content blocks.
  - Demonstrates the use of basic templatetag logic: `{% if %}{% else %}{% endif %}`
  - Iterating over a `QuerySet` via `{% for %}{% empty %}{% endfor %}`.
  - Using a variable in a template with the `{{ variable_name }}` syntax.
- **Generic Views**
  - Writing a generic view.
  - Modifying a generic view's context.
- **Forms**
  - Rendering a `ModelForm` in a template.
