import requests
import json

BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

# get resource from DB
def get_resources(id=None):
    data={}
    if id is not None:
        data={
            'id':id
        }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

# get_resources()
# get_resources(1)



# create/post new employee into DB
def create_resource():
    new_emp={
        'eno': 600,
        'ename':'akshay',
        'esal':6000,
        'eaddr':'vastral'
        }
    r=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(r.status_code)
    # print(r.text)
    print(r.json())

# create_resource()


# update employee into DB
def update_resource(id):
    update_emp={
        'id':id,
        'ename':'jay',
        'esal': 500,
        'eaddr':'vastral'
        }
    r=requests.put(BASE_URL+ENDPOINT,data=json.dumps(update_emp))
    print(r.status_code)
    # print(r.text)
    print(r.json())

# update_resource(5)


# delete employee obj into DB.
def delete_resource(id):
    update_emp={
        'id':id,
        }
    r=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(update_emp))
    print(r.status_code)
    # print(r.text)
    print(r.json())

# delete_resource(6)

