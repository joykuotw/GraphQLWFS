import unittest
import graphene
from flask import Flask, request
from main import graphqlwfs, Query
from graphene.test import Client

# Need this two lines to read .env
from dotenv import load_dotenv
load_dotenv()

def test_hello(self):
  
    schema = graphene.Schema(query=Query)
    client = Client(schema)
    query = ' { hello(count: 5, propertyName: "Type", literal: "Education") } '
    executed = client.execute(query)
    assert executed != {'data': {'hello': 'Error: Check your logs'}}
        
if __name__ == '__main__':
    unittest.main()