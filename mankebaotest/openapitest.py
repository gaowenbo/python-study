import requests
import json
import uuid


def add():
        url = "http://localhost:8080/open/api"

        method = "api.base.supplierUser.create"
        dataData = {"userCode": "32232", "userName": "daf", "tUserId": "9404"}

        data = {"method": method, "supplierCode": "300123", "requestId": str(uuid.uuid1()),
                "timestamp": 0, "version": "1.0", "sign": "dd", "data": json.dumps(dataData)}
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        res = requests.post(url=url, headers=headers, data=json.dumps(data)).text

        print(res)


def update():
        url = "http://localhost:8080/open/api"

        method = "api.base.supplierUser.update"
        dataData = {"userCode": "32232", "userName": "d3af", "tUserId": "9404"}

        data = {"method": method, "supplierCode": "300123", "requestId": str(uuid.uuid1()),
                "timestamp": 0, "version": "1.0", "sign": "dd", "data": json.dumps(dataData)}
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        res = requests.post(url=url, headers=headers, data=json.dumps(data)).text

        print(res)


def delete():
        url = "http://localhost:8080/open/api"

        method = "api.base.supplierUser.delete"
        dataData = {"userCode": "32232", "userName": "d3af", "tUserId": "9404"}

        data = {"method": method, "supplierCode": "300123", "requestId": str(uuid.uuid1()),
                "timestamp": 0, "version": "1.0", "sign": "dd", "data": json.dumps(dataData)}
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        res = requests.post(url=url, headers=headers, data=json.dumps(data)).text

        print(res)


update()