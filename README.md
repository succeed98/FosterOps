# Foster Ops


## Important Notes ##
1. Update requirements file before pushing to remote
2. Create user in mysql with name: dbms, password: password

## Procedure for adding new functionality##
Add functionalities which are independent of Employee data
1. pull from github
2. delete previous orphanage_management_system mysql database and create new emply database
3. delete migrations folder
4. create new class model for your functionality in models.py
5. Follow this order for creating tables: makemigrations child_app, migrate child_app, makemigrations, migrate
6. Create a superuser for doing login through admin
7. Add and edit html template files by copying template from room functionality or YouTube video repo
8. Add new item to sidebar_template.html
9. update urls.py
10. update AdminDBvIews.py with required functions and raw sql queries
11. Use objects.raw() for reading
12. Use cursor() for updating, inserting, deleting

Use command `python manage.py collectstatic` before `python manage.py runserver` if the static files are not rendered.
Use mysql in new console or Workbench for checking updates to database
# FosterOps
