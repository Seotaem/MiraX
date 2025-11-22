# MiraX - 가상 피팅 시스템

로컬에서 실행하는 방법입니다.

## 빠른 시작

### 방법 1: 배치 파일 사용 (Windows - 가장 간단)

**프로젝트 루트에서 실행:**
1. 프로젝트 루트 폴더의 `start-server.bat` 파일을 더블클릭
2. 브라우저가 자동으로 열립니다
3. 메인 페이지: `http://localhost:8000/프론트엔드(html, css, js)/index.html`

**프론트엔드 폴더에서 실행:**
1. `프론트엔드(html, css, js)` 폴더의 `start-server.bat` 파일을 더블클릭
2. 브라우저에서 `http://localhost:8000` 접속

### 방법 2: Python 스크립트 사용

**프로젝트 루트에서:**
```bash
python start-server.py
```

**프론트엔드 폴더에서:**
```bash
cd "프론트엔드(html, css, js)"
python start-server.py
```

### 방법 3: Python 명령어 직접 사용

**프로젝트 루트에서:**
```bash
python -m http.server 8000
```
그 다음 브라우저에서 `http://localhost:8000/프론트엔드(html, css, js)/index.html` 접속

**프론트엔드 폴더에서:**
```bash
cd "프론트엔드(html, css, js)"
python -m http.server 8000
```
그 다음 브라우저에서 `http://localhost:8000` 접속

## 주의사항

- **카메라 기능**을 사용하려면 HTTPS 또는 localhost에서 실행해야 합니다
- 일부 브라우저에서는 `file://` 프로토콜로 열 때 카메라 접근이 제한될 수 있습니다
- 로컬 서버를 사용하면 모든 기능이 정상적으로 작동합니다
- `select.html`에서 옷 이미지를 보려면 **프로젝트 루트에서 서버를 실행**하는 것을 권장합니다

## 페이지 구조

- `프론트엔드(html, css, js)/index.html` - 메인 페이지 (시작 페이지)
- `프론트엔드(html, css, js)/capture.html` - 카메라 촬영 페이지
- `프론트엔드(html, css, js)/review.html` - 촬영 결과 확인 페이지
- `프론트엔드(html, css, js)/select.html` - 옷 선택 페이지
- `프론트엔드(html, css, js)/loading.html` - 로딩 페이지
- `프론트엔드(html, css, js)/result.html` - 최종 결과 페이지

## Flask 서버 실행 (백엔드 포함)

백엔드 기능을 사용하려면:
```bash
python app.py
```

Flask 서버는 기본적으로 `http://localhost:5000`에서 실행됩니다.



