populate.py: This script can be used to populate Employee table with fake data by using faker and random modules.
swagger tool.txt: contains use of swagger and how to use it.
requirement.txt: contains installed plugings/library versions.
-----------------------------------------------------------------------------------------------------------------

*** Main Project urls.py file ***
----------------------------------
To get Swagger API View: http://127.0.0.1:8000/swagger/
To get Swagger API Documentation: http://127.0.0.1:8000/redoc/

----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------


*** NormalSerializer Application ***
--------------------------------------
Note: we are disable csrf_token for this app 

Documentation of Serializer avilable at -> NormalSerializer/intro.txt
Endpoints for NormalSerializer , EmployeeCRUD class:
    get: http://127.0.0.1:8000/api/
    post: http://127.0.0.1:8000/api/
    put: http://127.0.0.1:8000/api/
    delete: http://127.0.0.1:8000/api/


----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------

*** ModelSerializer Application ***
--------------------------------------
Note: we are disable csrf_token for this app

Documentation of ModelSerializer avilable at -> ModelSerializer/intro.txt
Endpoints for ModelSerializer , EmployeeCRUD class:
    get: http://127.0.0.1:8000/api/modelserializer/
    post: http://127.0.0.1:8000/api/modelserializer/
    put: http://127.0.0.1:8000/api/modelserializer/
    delete: http://127.0.0.1:8000/api/modelserializer/


----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------

*** APIview_ViewSet_app Application *** 
--------------------------------------
Note: APIview_ViewSet_app app methods by using browsable API

Documentation of APIView, Viewset, GenericAPIView, Mixins avilable at -> APIview_ViewSet_app/intro.txt
A). APIView -> without model
------------------------
Endpoints for APIview_ViewSet_app , DemoAPIView class:
    get: http://127.0.0.1:8000/api2/apiview/
    post: http://127.0.0.1:8000/api2/apiview/
    put: http://127.0.0.1:8000/api2/apiview/
    delete: http://127.0.0.1:8000/api2/apiview/


B). ViewSet -> without model
------------------------
Endpoints for APIview_ViewSet_app , DemoViewSet class:
    root api url = http://127.0.0.1:8000/api2/
    list: http://127.0.0.1:8000/api2/test-viewset/
    create: http://127.0.0.1:8000/api2/test-viewset/
    
    # in url we have to pass primary key(pk) that's why we pass 1 as a primarykey.
    retrieve: http://127.0.0.1:8000/api2/test-viewset/1/
    update: http://127.0.0.1:8000/api2/test-viewset/1/
    partial_update: http://127.0.0.1:8000/api2/test-viewset/1/
    destroy: http://127.0.0.1:8000/api2/test-viewset/1/


C). GenericAPIView
--------------------
Search name using function APIview_ViewSet_app.view -> StudentListAPIView (using ListAPIView)
Endpoint: 
    To get all records= http://127.0.0.1:8000/api2/apiview2/    
    To get records those sname row contain sunny = http://127.0.0.1:8000/api2/apiview2/?sname=sunny 

Create/Post record using function APIview_ViewSet_app.view -> StudentCreateAPIView (using CreateAPIView) 
Endpoint:
    To create record: http://127.0.0.1:8000/api2/apiview2/create

get/fetch/retrieve record using function APIview_ViewSet_app.view -> StudentRetrieveAPIView (using RetrieveAPIView) 
Endpoint:
    To retrieve record: http://127.0.0.1:8000/api2/apiview2/retrieve/3         # (here 3 is pk)

update/put/patch record using function APIview_ViewSet_app.view -> StudentUpdateAPIView (using UpdateAPIView) 
    To update record: http://127.0.0.1:8000/api2/apiview2/update/3         # (here 3 is pk)

Delete record using function APIview_ViewSet_app.view -> StudentDestroyAPIView (using DestroyAPIView) 
    To delete record: http://127.0.0.1:8000/api2/apiview2/delete/3         # (here 3 is id)


get list of records and create new once using APIview_ViewSet_app.view -> StudentListCreateAPIView (using ListCreateAPIView)
Single Endpoint:
    to get list & create/post record : http://127.0.0.1:8000/api2/apiview2/list_create


get record and update record using APIview_ViewSet_app.view -> StudentRetrieveUpdateAPIView (using RetrieveUpdateAPIView)
Single Endpoint:
    to get list & update record : http://127.0.0.1:8000/api2/apiview2/retrieve_update/2    # (here 3 is id)


get record and destroy record using APIview_ViewSet_app.view -> StudentRetrieveDestroyAPIView (using RetrieveDestroyAPIView)
Single Endpoint:
    to get list & destroy record : http://127.0.0.1:8000/api2/apiview2/retrieve_destroy/2    # (here 3 is id)


get record, update record & destroy record using APIview_ViewSet_app.view -> StudentRetrieveUpdateDestroyAPIView (using RetrieveUpdateDestroyAPIView)
Single Endpoint:
    to get list & update & destroy record : http://127.0.0.1:8000/api2/apiview2/retrieve_update_destroy/2    # (here 3 is id)


D). Mixins
-------------
get records list & create new record using mixin:
Endpoint: http://127.0.0.1:8000/api2/apiview2/list_create_mixin

retrieve record details & update & destroy record using mixin:
Endpoint: http://127.0.0.1:8000/api2/apiview2/retrieve_update_destroy_mixin/2
Note: pass pk/id in url


----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------

*** ViewSets_app Application ***
--------------------------------------
Endpoints for ViewSets_app , EmployeeCRUD_CBV class:
    root api url = http://127.0.0.1:8000/api3/
    list: http://127.0.0.1:8000/api3/modelViewset/
    create: http://127.0.0.1:8000/api3/modelViewset/
    
    # in url we have to pass primary key(pk) that's why we pass 1 as a primarykey.
    retrieve(fetch single record details): http://127.0.0.1:8000/api3/modelViewset/1/
    update: http://127.0.0.1:8000/api3/modelViewset/1/
    partial_update: http://127.0.0.1:8000/api3/modelViewset/1/
    destroy: http://127.0.0.1:8000/api3/modelViewset/1/


----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------

*** authentication_n_authorization_app Application ***
------------------------------------------------------

Documentation of authentication, authorization, their types & classes, token & JWT authentication avilable at -> authentication_n_authorization_app/intro.txt

Token Authentication:
---------------------
Endpoint to get api token: 
    Post: http://127.0.0.1:8000/api4/get-api-token/     With passing this parameter in body form-data: username="sunny" password="durga123"

Note: without token below apis are not working so first you have to get token from above post api endpoint then add that token into 
header part of postmen/client app.(like Authentication = Token 0b35f78cd8b8b6a2fc57ce306ab5b9fe9bb486d0)

Endpoint for access employee data 
    root api = http://127.0.0.1:8000/api4/
    Get: http://127.0.0.1:8000/api4/emp-data        # Token is must to access Employee data.
    Put: http://127.0.0.1:8000/api4/emp-data/1/     # Token is must to access Employee data.
    Patch: http://127.0.0.1:8000/api4/emp-data/1/   # Token is must to access Employee data.

Endpoint to get student data only with custom permission class:
    root api = http://127.0.0.1:8000/api4/
    get = http://127.0.0.1:8000/api4/stu-data/


JWT Authentication:
-------------------
Endpoint to get JWT access & refresh & verify token:
    post: http://127.0.0.1:8000/api4/auth-jwt/     
        Body section:
            Key: username, value:admin
            Key: password, value:admin

    post: http://127.0.0.1:8000/api4/auth-jwt-refresh/
        Headers section:
            Key: Content-Type value: application/json
        Body Section:
            KEY: token,
            value: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImR1cmdhIiwiZXhwIjoxNTQ4NjczNDgzLCJlbWFpbCI6
                    IiIsIm9yaWdfaWF0IjoxNTQ4NjczMTgzfQ.tdC5css67Ix8v4Tci4q5YjhobQoLnaSqOOh6wfl2qpk (existing access token)

    post: http://127.0.0.1:8000/api4/auth-jwt-verify/
        Headers section:
            Key: Content-Type, value: application/json
        Body Section:
            KEY: token,
            value: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImR1cmdhIiwiZXhwIjoxNTQ4NjczNDgzLCJlbWFpbCI6
                    IiIsIm9yaWdfaWF0IjoxNTQ4NjczMTgzfQ.tdC5css67Ix8v4Tci4q5YjhobQoLnaSqOOh6wfl2qpk (Verify this token)  

Endpoint with appling CRUD operation with JWT token:
    post: http://127.0.0.1:8000/api4/auth-jwt/
        Body section:
            Key: username, value:admin
            Key: password, value:admin

    list: http://127.0.0.1:8000/api4/stu-jwt/
        Headers section:
            KEY: Authorization,
            value: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1OTIxMzI4LCJpYXQiOjE3MTU5MjEwM
            jgsImp0aSI6IjUyNTBjOWVjNzYwMTQ2MDk5NTRiY2Q4YzFkODgxYzFmIiwidXNlcl9pZCI6MX0.PGgIhrR47ZfiW2_cF4jOHvXh62EVxQcwG1ZbPo2f7q4
        or
        Authorization section:
            select: Bearer Token and pass token value.

    get: http://127.0.0.1:8000/api4/stu-jwt/1
        Headers section:
            KEY: Authorization,
            value: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1OTIxMzI4LCJpYXQiOjE3MTU5MjEwM
            jgsImp0aSI6IjUyNTBjOWVjNzYwMTQ2MDk5NTRiY2Q4YzFkODgxYzFmIiwidXNlcl9pZCI6MX0.PGgIhrR47ZfiW2_cF4jOHvXh62EVxQcwG1ZbPo2f7q4
        or
        Authorization section:
            select: Bearer Token and pass token value.

    put: http://127.0.0.1:8000/api4/stu-jwt/1
        Headers section:
            KEY: Authorization,
            value: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1OTIxMzI4LCJpYXQiOjE3MTU5MjEwM
            jgsImp0aSI6IjUyNTBjOWVjNzYwMTQ2MDk5NTRiY2Q4YzFkODgxYzFmIiwidXNlcl9pZCI6MX0.PGgIhrR47ZfiW2_cF4jOHvXh62EVxQcwG1ZbPo2f7q4
        or
        Authorization section:
            select: Bearer Token and pass token value.

        Body section:
            Key: fieldName, value: val
            Key: fieldName, value: val

    patch: http://127.0.0.1:8000/api4/stu-jwt/1
        Headers section:
            KEY: Authorization,
            value: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1OTIxMzI4LCJpYXQiOjE3MTU5MjEwM
            jgsImp0aSI6IjUyNTBjOWVjNzYwMTQ2MDk5NTRiY2Q4YzFkODgxYzFmIiwidXNlcl9pZCI6MX0.PGgIhrR47ZfiW2_cF4jOHvXh62EVxQcwG1ZbPo2f7q4
        or
        Authorization section:
            select: Bearer Token and pass token value.

        Body section:
            Key: fieldName, value: val
            Key: fieldName, value: val

    delete: http://127.0.0.1:8000/api4/stu-jwt/1
        Headers section:
            KEY: Authorization,
            value: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1OTIxMzI4LCJpYXQiOjE3MTU5MjEwM
            jgsImp0aSI6IjUyNTBjOWVjNzYwMTQ2MDk5NTRiY2Q4YzFkODgxYzFmIiwidXNlcl9pZCI6MX0.PGgIhrR47ZfiW2_cF4jOHvXh62EVxQcwG1ZbPo2f7q4
        or
        Authorization section:
            select: Bearer Token and pass token value.


Custom Authentication:
----------------------
1). custom authenticate1
Endpoint for getting list of student: 
    Get: http://127.0.0.1:8000/api4/stu-custom-auth/?username=admin     # username is must to pass as query string.
Note: if username field not found than return found None. if username field valid than get the list of student.

1). custom authenticate2 
Endpoint for getting list of student: 
    Get: http://127.0.0.1:8000/api4/stu-custom-auth/?username=admin&key=n7ZXa98     # username,key are must to pass as query string.
Note: if username field not found than return found None. if username field valid than check our custom condtion if all 
conditions are True then get the list of student.


----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------

*** pagination_app Application ***
----------------------------------

Documentation of pagination avilable at -> pagination_app/intro.txt
endpoint for pagination class of VendorListView:
    PageNumberPagination Class:
        get list: http://127.0.0.1:8000/api5/   # get all data from vendor table.
        get records of page number 2: http://127.0.0.1:8000/api5/?mypage=2  
        get 8 records of page number 2: http://127.0.0.1:8000/api5/?mypage=2&page_size=8  
        get last page with 6 records: http://127.0.0.1:8000/api5/?mypage=endpage&page_size=6  

    LimitOffsetPagination:
        get list of 8 records starts from 22 record id:
            http://127.0.0.1:8000/api5/?mylimit=8&myoffset=21 

    CursorPagination:
        get list in order by vsal with 5 records per page:
            http://127.0.0.1:8000/api5/


----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------

*** DRF_filtering_app Application ***
--------------------------------------

Documentation of Searching, Ordering avilable at -> DRF_filtering_app/intro.txt
Seaching:
---------
Planin Vanilla Filtering: 
    Get: http://127.0.0.1:8000/api/     # Returns all Employee records without any filtering
    Get: http://127.0.0.1:8000/api/?ename=Jhon  # Returns Employee records where vname contains 'Jhon'

By using Django RestFramework API:
    Get: http://127.0.0.1:8000/api/     # Returns all Employee records without any filtering
    Get: http://127.0.0.1:8000/api6/?search=jo  # Returns Employee records where vname contains 'jo'


Ordering:
---------
   Get: http://127.0.0.1:8000/api6/?ordering=vaddr  # Return all records in asending order by vaddr
   Get: http://127.0.0.1:8000/api6/?search=J&ordering=-vsal # Return all records where ename contains J & order by desending order of vsal.


----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------

*** NestedSerializer_app Application ***
-----------------------------------------

Documentation of Nested serializer(foreign key concepts) avilable at -> NestedSerializer_app/intro.txt

Author TB:
---------
For Author table -> AuthorListCreateView, AuthorRUDView classes
Note : in nested serializer we get book information by the author only we can read those information but can't change it.
Note: if you are delete author than automatically deleted author related books from book table.

Get list(all records): http://127.0.0.1:8000/api7/author    # List out all authors with their book information
post: http://127.0.0.1:8000/api7/author/
    Body section:
        Key: first_name, value: XXXX
        Key: last_name, value: XXXX
        Key: subject, value: XXXX

retrieve (single record with details): http://127.0.0.1:8000/api7/author/3     # Get single author information when you pass their PriamryKey (like 3)

put: http://127.0.0.1:8000/api7/author/3 
    Body section:
        Key: first_name, value: XXXX
        Key: last_name, value: XXXX
        Key: subject, value: XXXX

patch: http://127.0.0.1:8000/api7/author/3 
    Body section:
        Key: first_name, value: XXXX         # optional field 
        Key: last_name, value: XXXX          # optional field
        Key: subject, value: XXXX            # optional field

delete: http://127.0.0.1:8000/api7/author/3 


Book TB:
--------
For Author table -> BookListCreateView, BookRUDView classes

Get list(all records): http://127.0.0.1:8000/api7/book    # List out all Books information
post: http://127.0.0.1:8000/api7/book
    Body section:
        Key: first_name, value: XXXX
        Key: last_name, value: XXXX
        Key: subject, value: XXXX

retrieve (single record with details): http://127.0.0.1:8000/api7/book/3      # Get single book information when you pass their PriamryKey (like 3)

put: http://127.0.0.1:8000/api7/book/3 
    Body section:
        Key: first_name, value: XXXX
        Key: last_name, value: XXXX
        Key: subject, value: XXXX

patch: http://127.0.0.1:8000/api7/book/3 
    Body section:
        Key: first_name, value: XXXX         # optional field 
        Key: last_name, value: XXXX          # optional field
        Key: subject, value: XXXX            # optional field

delete: http://127.0.0.1:8000/api7/book/3


----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------

