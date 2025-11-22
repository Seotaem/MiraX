@echo off
chcp 65001 >nul
echo ========================================
echo   로컬 서버 시작 중...
echo ========================================
echo.
echo 서버 주소: http://localhost:8000
echo.
echo 브라우저에서 위 주소로 접속하세요.
echo 메인 페이지: http://localhost:8000/프론트엔드(html, css, js)/index.html
echo.
echo 종료하려면 Ctrl+C를 누르세요.
echo.
echo ========================================
echo.

cd /d "%~dp0"
python -m http.server 8000

pause



