import os
import SocketServer
import SimpleHTTPServer
from .building import build


def preview(directory=None, host=None, port=None, watch=True):
    """Runs a local server to preview the working directory of a repository."""
    directory = directory or '.'
    host = host or '127.0.0.1'
    port = port or 5000

    # TODO: admin interface

    # TODO: use cache_only to keep from modifying output directly
    out_directory = build(directory)

    # Serve generated site
    os.chdir(out_directory)
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer((host, port), Handler)
    print ' * Serving on http://%s:%s/' % (host, port)
    httpd.serve_forever()
