# lightweight flask restful server 
-----------
1. Dependency

    Using [poetry](https://python-poetry.org/) to manage the dependency and python env. 
    You may find the dependencies in **pyproject.toml** file. 
  
    To install poetry via pip:
    ```shell script
    $ pip install --user poetry
    ```
    Install dependency
    ```shell script
    $ poetry install
    ```
    Run the server with project's virtualenv
    ```shell script
    $ poetry shell
    $ python run.py 
    ```
    or
    ```shell script
    $ poetry run python run.py
    ```
2. Structure of project
    ```text
    -root
       -app 
           -models // Model DAO related file
           -resources // Controller and Service restful request end-point
           __init__.py // include router mapping
       -client // will delete
       -config.py //config file of project(include secret key for security hash)
       -run.py // python run.py to run the server
     ```
3. Alembic: database migration
    - init alembic
    ```shell script
     $ alembic init alembic
    ```
    - define database schemas in app.schemas
    - set auto generation target metadata in env.py
    - generate migration code
    ```shell script
     $ alembic revision --autogenerate -m "init table" 
   ```
    - add init role data
    ```shell script
     $ alembic revision -m "Init role data"  
   ```
   - do migration and initialization
   ```shell script
     $ alembic upgrade head
   ```

