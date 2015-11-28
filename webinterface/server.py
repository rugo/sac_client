import time
import BaseHTTPServer
from sac import util

PORT_NUMBER = 8080
TEMPLATE_DIR = "templates/"

contents = {
    "registered": "",
    "unregistered": ""
}

class DefHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """
    Only delivers the html code that POSTs data to the
    Middleware.
    """
    def do_GET(s):
        """Only Get is supported"""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        if util.is_registered():
            s.wfile.write(contents["registered"])
        else:
            s.wfile.write(contents["unregistered"])

def read_file(name):
    # TODO: basic templating
    with open (TEMPLATE_DIR + name + ".html", "r") as f:
        contents[name] = f.read()

def read_files():
    for k in contents:
        read_file(k)

def run_server():
    httpd = BaseHTTPServer.HTTPServer(("", PORT_NUMBER), DefHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    read_files()
    run_server()