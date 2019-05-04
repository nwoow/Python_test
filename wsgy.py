def application(environ,start_response):
    status = '200 OK'
    html = {
        'chart': {
            'result': "eer",
            'error':"hhh"
        }
    }
    response_header = [('Content-type','json')]
    start_response(status,response_header)
    return [html]