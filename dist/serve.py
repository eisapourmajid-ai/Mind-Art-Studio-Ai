#!/usr/bin/env python3
"""Download server for the Mind Art Studio AI package.

Serves dist/ with two behaviours the default http.server does not provide:

  1. The ZIP is returned with `Content-Disposition: attachment`, so the browser
     downloads it even when the click originates inside a cross-origin iframe,
     where the HTML `download` attribute is ignored.
  2. Framing and cross-origin fetches are permitted, so the page renders inside
     the preview panel.
"""

import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

DIST = os.path.dirname(os.path.abspath(__file__))
ZIP_NAME = "MindArtStudioAI.zip"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DIST, **kw)

    def end_headers(self):
        # Allow the page to render inside the preview iframe.
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-store")
        # Force a download rather than an in-frame navigation for the archive.
        if self.path.lstrip("/").split("?")[0] == ZIP_NAME:
            self.send_header(
                "Content-Disposition", f'attachment; filename="{ZIP_NAME}"'
            )
            self.send_header("Content-Type", "application/zip")
        super().end_headers()

    def log_message(self, fmt, *args):
        # Log the real client so iframe vs. direct requests are distinguishable.
        print(f"{self.address_string()} - {fmt % args}", flush=True)


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("0.0.0.0", 8000), Handler)
    print(f"Serving {DIST} on 0.0.0.0:8000", flush=True)
    srv.serve_forever()
