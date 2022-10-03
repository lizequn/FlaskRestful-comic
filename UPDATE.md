# Version update history

----

### v 0.0.1
##### public API
 - auth
    - user register with role
     ```
       Post /register/secretkey
       body
           {
            "username":"username",
            "password":"password",
            ["role_id":"0"] //optional default id 0 as normal user, 999 as admin user,
            }
       response:
        '201' success
     ```
    - user login
    ```
       Post /login
       body
           {
            "username":"username",
            "password":"password"
            }
       response:
        {
            "access_token": "token",
            "id": "user_id"
        }
     ```
   - user info get
   ```
       Get /login
       header
            {
            "Authorization": "Bearer +token"//only admin can add
            }
       response:
        {
    "user_id": "id",
    "username": "name",
    "roles": [
            {
                "id": 999,
                "name": "admin",
                "description": "admin user"
            }
        ]
     }
     ```
    - role add
    ```
       Post /role
       header
            {
            "Authorization": "Bearer +token"//only admin can add
            }
       body
           {
            "name":"name_of_role",
            ["description":"desp"] //optional
            }
       response:
        '201' success
     ```
    - role view
    ```
       Get /role
       header
            {
            "Authorization": "Bearer +token"//only admin can add
            }
       response:
        list of role
     ```
  - questionnaire
    - endpoint add
    ```
       Post /survey
       header
            {
            "Authorization": "Bearer +token"//only admin can add
            }
        body
            {
                "endpoint":"name_of_endpoint",
                "name":"name_of_survey"
            }
       response:
        "201" success
     ```
    - endpoint view
    ```
       Get /survey
       header
            {
            "Authorization": "Bearer +token"//only admin can add
            }
       response:
        List of endpoint
        [
            {
                "id": 0,
                "endpoint": "test",
                "name": "test question",
                "description": "test question"
            },
            {
                "id": 1,
                "endpoint": "t1",
                "name": "newtest",
                "description": null
            }
        ]
     ```
    - question feedback data add
    ```
       Post /survey/name_of_endpoint
       body
           {
            questionnire feedback in json
            }
       response:
        "201", success
     ```
##### function
 - auth control
    - jwt/db based auth filter
    - build claim into jwt header
 - sqlite db setup
 - mongodb setup
 - alembic
    - init sql db schema
    - add initial db data(default user role)
    - add initial question endpoint
 - poetry
    - dependency package control
 - security.json
    - security pwd file
----------------------
### v 0.0.2
##### public API
- questionnaire
    - question feedback data get
    ```
       Get /survey/name_of_endpoint
       header
            {
            "Authorization": "Bearer +token"//only admin can do
            }
       response:
        List of question feedback data
        [
          {
            "_id": "{\"$oid\": \"5eb0b7a8c6bd6d0e5be4e6ee\"}",
            "created_time": "Tue, 05 May 2020 12:47:36 GMT",
            "haha": "ha",
            "hhsd": "asdt",
            "q1": 4,
            "q2": 6,
            "q5": 2,
            "question_id": 0
          },
          {
            "_id": "{\"$oid\": \"5eb0b7d2c6bd6d0e5be4e6ef\"}",
            "created_time": "Tue, 05 May 2020 12:48:18 GMT",
            "haha": "ssd",
            "hhsd": "43",
            "q1": 4,
            "q2": 6,
            "q5": 2,
            "question_id": 0
          }
        ]
     ```
##### function
- mongodb
    - add created_time
    - handle bson ObjectId to json
------------------
### v 0.0.3
##### public API
- version check
    ```
       get /
       response:
        version info
     ```
##### function
- add all config to flask context
- use relative path for all config
--------------
### v 0.1.0
big update according to https://github.com/flask-restful/flask-restful/issues/883
##### dependency
- remove flask-restful
- add webargs/Marshmallow replace reqparse
- add Flask-Marshmallow replace fields
##### function
- MethodView replace Resource Mapping
- Marshmallow all request/response for info security control
- json format abort message
---------------
### v 0.1.1
##### public API
- file upload
  ```
       post /file/upload
       form-data{
        file: value
        }
       response:
        201, success
     ```
- file download
  ```
       get /file/{filename}
       response:
        file to download
     ```
  
##### function
- update alembic database structure
- file upload security check
--------------------
### v 0.1.2
##### improvement
- comment for mongodb
- better logger
--------------------
### v 0.1.3
##### improvement
- add support mongodb test db

