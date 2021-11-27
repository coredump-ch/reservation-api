#!/usr/bin/env python3
"""
Script that runs inside the Docker container and ensures that it's healthy.
"""

import http.client
import os

HOST = '127.0.0.1'
PORT = 8000

if __name__ == '__main__':
    hostname = os.environ.get('ALLOWED_HOST', 'localhost')
    conn = http.client.HTTPConnection(f'{HOST}:{PORT}')
    conn.request('GET', '/healthcheck/', headers={'host': hostname})
    response = conn.getresponse()
    print(f'HTTP {response.status} {response.reason}')
    body = response.read().decode('utf8')
    print(f'Body: {body}')
    assert response.status == 200, 'Non-200 response'
