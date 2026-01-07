#!/usr/bin/env python3
"""
Lightweight smoke tests for a model endpoint.

Usage:
  export MODEL_API_URL="https://..."
  export MODEL_API_KEY="..."    # optional
  python tests/smoke_test.py

Or pass args:
  python tests/smoke_test.py --url https://... --key ...

This script uses only the Python standard library so it runs without extra deps.
"""
import os
import sys
import json
import argparse
from urllib import request, error


def post_json(url, data, headers=None, timeout=15):
    body = json.dumps(data).encode('utf-8')
    req = request.Request(url, data=body, method='POST')
    req.add_header('Content-Type', 'application/json')
    if headers:
        for k, v in headers.items():
            req.add_header(k, v)
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            resp_body = resp.read().decode('utf-8')
            return resp.getcode(), resp_body
    except error.HTTPError as e:
        try:
            return e.code, e.read().decode('utf-8')
        except Exception:
            return e.code, ''
    except Exception as e:
        print('Request error:', e)
        return None, ''


def extract_text(mixed):
    """Extract visible text from a nested JSON response by concatenating string fields."""
    if mixed is None:
        return ''
    if isinstance(mixed, str):
        return mixed
    if isinstance(mixed, dict):
        parts = []
        for v in mixed.values():
            t = extract_text(v)
            if t:
                parts.append(t)
        return '\n'.join(parts)
    if isinstance(mixed, list):
        parts = [extract_text(x) for x in mixed]
        return '\n'.join([p for p in parts if p])
    return ''


def run_checks(api_url, api_key=None):
    headers = {}
    if api_key:
        headers['Authorization'] = f'Bearer {api_key}'

    tests = [
        {'id': 'smoke-1', 'prompt': 'Write a two-line haiku about winter.'},
        {'id': 'smoke-2', 'prompt': 'Summarize the Battle of Hastings in one sentence.'},
    ]

    for t in tests:
        payload = { 'input': t['prompt'] }
        code, body = post_json(api_url, payload, headers=headers)
        if code is None:
            print('FAIL', t['id'], 'no response')
            return 2
        if code < 200 or code >= 300:
            print('FAIL', t['id'], 'HTTP', code)
            print(body)
            return 3
        try:
            parsed = json.loads(body) if body else {}
        except Exception:
            parsed = {}
        text = extract_text(parsed).strip() or body.strip()
        if len(text) < 10:
            print('FAIL', t['id'], 'output too short')
            print('Output:', repr(text))
            return 4
        # simple domain-specific checks
        if t['id'] == 'smoke-1':
            # expect at least two lines for a haiku-like output
            if text.count('\n') < 1:
                print('WARN', t['id'], 'did not contain multiple lines; continuing')
        if t['id'] == 'smoke-2':
            low = text.lower()
            if not ('hastings' in low or '1066' in low or 'battle' in low):
                print('WARN', t['id'], 'summary may be off; continuing')
        print('OK', t['id'], text.replace('\n', ' / ')[:200])

    print('All smoke tests passed')
    return 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--url', help='Model API URL', default=os.getenv('MODEL_API_URL'))
    p.add_argument('--key', help='API key', default=os.getenv('MODEL_API_KEY'))
    args = p.parse_args()
    if not args.url:
        print('Error: specify --url or set MODEL_API_URL')
        sys.exit(1)
    rc = run_checks(args.url, args.key)
    sys.exit(rc)


if __name__ == '__main__':
    main()
