#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
로컬 웹 서버 실행 스크립트 (프로젝트 루트)
Python 3.x 필요
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000

# 현재 스크립트가 있는 디렉토리로 이동
os.chdir(Path(__file__).parent)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}"
    main_page = f"{url}/프론트엔드(html, css, js)/index.html"
    print("=" * 50)
    print("  로컬 서버가 시작되었습니다!")
    print("=" * 50)
    print(f"\n서버 주소: {url}")
    print(f"메인 페이지: {main_page}")
    print("\n브라우저가 자동으로 열립니다...")
    print("종료하려면 Ctrl+C를 누르세요.")
    print("=" * 50)
    print()
    
    # 자동으로 브라우저 열기
    webbrowser.open(main_page)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n서버를 종료합니다...")
        httpd.shutdown()



