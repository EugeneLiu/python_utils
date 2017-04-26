class SqlMonitorMiddleware(object):

    def process_request(self, request):
        return None

    def process_response(self, request, response):
        print "in sql monitor middleware process response"
        if not settings.DEBUG:
            return response
        database_names = settings.DATABASES.keys()
        queries = {}
        for name in database_names:
            for query in connections[name].queries:
                queries.setdefault(name, []).append(query)
        try:
            content = json.loads(response.content)
            content['queries'] = queries
            response.content = json.dumps(content)
        except:
            pass
        return response
