# Schedule - Database #

Manage Databases

#### Release Information ####

* Version: 1.0.0
  
#### Default ####

  * Primary
  
## Installation ##

* Remove current migrations

    `rm -Rf database/default/migrations/`

* Make Migration Configurations

    `python manage.py makemigrations`

* Create Database Structure

    `python manage.py migrate`

* Remove Database Structure

    ```
    python manage.py migrate default zero
    python manage.py migrate auth zero
    python manage.py migrate sessions zero
    python manage.py migrate contenttypes zero
    ```