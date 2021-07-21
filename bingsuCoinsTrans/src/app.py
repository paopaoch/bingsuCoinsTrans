import json
import boto3
from boto3.dynamodb.conditions import Key
from .bingsuCoinsTransaction import PynamoBingsuCoinsTrans
from datetime import datetime
import os
# import requests

def add_bingsu_coins_transaction(event, context):
    item = event['arguments']
    user_item = PynamoBingsuCoinsTrans(
        coin_transaction_id = item['coin_transaction_id'],
        user_id = item['user_id'],
        date_time = str(datetime.utcnow()).replace(' ','T')[0:19]+'+00:00',
        carbon_coins = item['carbon_coins'],
    )
    user_item.save()
    return {'status': 200}


def get_bingu_coins_transaction(event, context):
    item = event['arguments']
    user_id = item['user_id']
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table("BingsuCoinsTrans")
    scan_kwargs = {
        'FilterExpression': Key('user_id').eq(user_id),
    }
    
    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None

    return {'status': 200, 'data': response['Items']}

def lambda_handler(event, context):
    return {'data': 'Hello World'}