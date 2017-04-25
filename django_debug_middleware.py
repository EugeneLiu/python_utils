# coding: utf-8
import json
from django.db import connections
from django.conf import settings

class SqlMonitorMiddleware(object):

    def process_request(self, request):
        return None

    def process_response(self, request, response):
        print "in sql monitor middleware process response"
        database_names = settings.DATABASES.keys()
        queries = {}
        for name in database_names:
            for query in connections[name].queries:
                queries[name] = query
        content = json.loads(response.content)
        content['queries'] = queries
        response.content = json.dumps(content)
        return response
