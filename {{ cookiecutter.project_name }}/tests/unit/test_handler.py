import json
import pytest
from first_function import app
import os

{ % if cookiecutter.include_apigw == "y" %}

@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": "{ \"test\": \"body\"}",
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": ""
            },
            "stage": "prod"
        },
        "queryStringParameters": {
            "foo": "bar"
        },
        "headers": {
            "Via":
                "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language":
                "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer":
                "true",
            "CloudFront-Is-SmartTV-Viewer":
                "false",
            "CloudFront-Is-Mobile-Viewer":
                "false",
            "X-Forwarded-For":
                "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country":
                "US",
            "Accept":
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests":
                "1",
            "X-Forwarded-Port":
                "443",
            "Host":
                "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto":
                "https",
            "X-Amz-Cf-Id":
                "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer":
                "false",
            "Cache-Control":
                "max-age=0",
            "User-Agent":
                "Custom User Agent String",
            "CloudFront-Forwarded-Proto":
                "https",
            "Accept-Encoding":
                "gzip, deflate, sdch"
        },
        "pathParameters": {
            "proxy": "/examplepath"
        },
        "httpMethod": "POST",
        "stageVariables": {
            "baz": "qux"
        },
        "path": "/examplepath"
    }


def test_lambda_handler(apigw_event):
    ret = app.lambda_handler(apigw_event, "")
    assert ret['statusCode'] == 200
    assert ret['body'] == json.dumps({'hello': 'world'})


{ % else %}

@pytest.fixture()
def lambda_event():
    """ Generates Lambda Event"""

    return {"foo": "bar"}


def test_lambda_handler(lambda_event):
    ret = app.lambda_handler(lambda_event, "")
    assert ret == {'hello': 'world'}


#
#
#
#
#
#
#
#
#
#
#
key = 'hello'
value = 'test'


def test_get_message(lambda_event, key, value):
    ret = app.lambda_handler(lambda_event, "")
    # assert ret == {'hello': 'world'}
    assert ret == {key: value}


def test_get_message(apigw_event, key, value):
    ret = app.lambda_handler(apigw_event, "")
    assert ret['statusCode'] == 200
    assert ret['body'] == json.dumps({key: value})


{ % else %}

@pytest.fixture()
def lambda_event():
    """ Generates Lambda Event"""

    return {"foo": "bar"}


def test_get_message(lambda_event, key, value):
    ret = app.lambda_handler(lambda_event, "")
    assert ret == {key: value}


#
#
#
#
#
#
#
#
#
#
#
#
def test_runs_on_aws_lambda():
    ret = app.lambda_handler(lambda_event, "")
    assert ret == {'hello': 'world'}


def test_runs_on_aws_lambda(apigw_event):
    ret = app.lambda_handler(apigw_event, "")
    assert ret['statusCode'] == 200
    assert ret['body'] == json.dumps({'hello': 'world'})


{ % else %}

@pytest.fixture()
def lambda_event():
    """ Generates Lambda Event"""

    return {"foo": "bar"}


def test_lambda_handler(lambda_event):
    ret = 'AWS_SAM_LOCAL' not in os.environ and 'LAMBDA_TASK_ROOT' in os.environ
    assert ret == True
