# StrideX Dashboard 배포 가이드 🚀

## 📋 목차
1. [배포 방법 개요](#배포-방법-개요)
2. [옵션 1: GitHub Pages (무료, 추천)](#옵션-1-github-pages)
3. [옵션 2: Netlify (무료, 가장 쉬움)](#옵션-2-netlify)
4. [옵션 3: Vercel (무료)](#옵션-3-vercel)
5. [옵션 4: 자체 서버](#옵션-4-자체-서버)
6. [사용 방법](#사용-방법)

---

## 배포 방법 개요

StrideX Dashboard는 **완전한 정적 웹사이트**입니다. 
- ✅ 서버 불필요
- ✅ 데이터베이스 불필요
- ✅ 백엔드 불필요
- ✅ 단일 HTML 파일로 작동

**필요한 파일:**
- `stridex_dashboard_final.html` (단 하나!)

---

## 옵션 1: GitHub Pages (무료, 추천)

### 장점
- 완전 무료
- GitHub 계정만 있으면 됨
- HTTPS 자동 제공
- 버전 관리 가능

### 배포 단계

#### 1. GitHub 저장소 생성
```bash
# 로컬에서
mkdir stridex-dashboard
cd stridex-dashboard
git init
```

#### 2. 파일 준비
- `stridex_dashboard_final.html` 파일을 `index.html`로 이름 변경
```bash
cp stridex_dashboard_final.html index.html
```

#### 3. GitHub에 푸시
```bash
git add index.html
git commit -m "Initial commit: StrideX Dashboard"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/stridex-dashboard.git
git push -u origin main
```

#### 4. GitHub Pages 활성화
1. GitHub 저장소 페이지로 이동
2. `Settings` → `Pages` 클릭
3. Source: `main` 브랜치 선택
4. Save 클릭

#### 5. 접속
5-10분 후 `https://YOUR_USERNAME.github.io/stridex-dashboard/` 에서 접속 가능!

---

## 옵션 2: Netlify (무료, 가장 쉬움)

### 장점
- 드래그 앤 드롭만으로 배포
- 즉시 배포 (1분 이내)
- 무료 HTTPS
- 자동 빌드/배포

### 배포 단계

#### 방법 A: 드래그 앤 드롭 (가장 쉬움)

1. **Netlify 가입**
   - https://www.netlify.com/ 접속
   - GitHub/GitLab/Email로 가입

2. **새 사이트 생성**
   - "Add new site" → "Deploy manually" 클릭
   
3. **파일 업로드**
   - `stridex_dashboard_final.html` 파일을 `index.html`로 이름 변경
   - 폴더를 만들고 `index.html` 파일을 넣기
   - 폴더 전체를 드래그 앤 드롭

4. **완료!**
   - 자동으로 URL 생성 (예: `https://stridex-dashboard-abc123.netlify.app`)
   - 커스텀 도메인 설정 가능

#### 방법 B: Git 연결 (자동 배포)

1. GitHub 저장소를 먼저 생성
2. Netlify에서 "Import from Git" 선택
3. 저장소 선택 후 배포
4. 코드 푸시 시 자동 재배포

---

## 옵션 3: Vercel (무료)

### 장점
- 빠른 CDN
- 자동 HTTPS
- GitHub 통합

### 배포 단계

1. **Vercel 가입**
   - https://vercel.com 접속
   - GitHub 계정으로 로그인

2. **프로젝트 생성**
   ```bash
   npm i -g vercel  # Vercel CLI 설치 (선택사항)
   vercel           # 배포 명령어
   ```
   
   또는 웹에서:
   - "Add New" → "Project"
   - GitHub 저장소 선택
   - 자동 배포

3. **완료!**
   - URL: `https://stridex-dashboard.vercel.app`

---

## 옵션 4: 자체 서버

### 웹 서버에 직접 배포

#### Apache
```bash
# 파일 복사
cp stridex_dashboard_final.html /var/www/html/index.html

# 권한 설정
chmod 644 /var/www/html/index.html
```

#### Nginx
```bash
# 파일 복사
cp stridex_dashboard_final.html /usr/share/nginx/html/index.html

# 권한 설정
chmod 644 /usr/share/nginx/html/index.html
```

#### Python 간단 서버 (테스트용)
```bash
# Python 3
python -m http.server 8000

# 접속: http://localhost:8000/stridex_dashboard_final.html
```

---

## 사용 방법

### 1. 데이터 업로드

#### 파일 업로드
```
1. "📄 파일 선택" 버튼 클릭
2. 여러 JSON 파일 선택 (Ctrl/Cmd + 클릭)
3. 자동으로 Subject별 분류
```

#### 폴더 업로드
```
1. "📁 폴더 선택" 버튼 클릭
2. 데이터 폴더 선택
3. 폴더 내 모든 JSON 파일 자동 읽기
```

**폴더 구조 예시:**
```
data/
├── lb_01_insole_039.json
├── lb_01_imu_039.json
├── lb_01_pad_039.json
├── lb_02_insole_045.json
├── lb_02_imu_045.json
└── lb_02_pad_045.json
```

### 2. 데이터 검수

1. **Subject 선택**: 왼쪽 패널에서 환자 선택
2. **ID 검증**: 상단에서 Pass/Fail 선택
3. **Gait Cycle 검증**: 중앙 패널 확인 후 Pass/Fail
4. **Labeling 검증**: 우측 패널 확인 후 Pass/Fail

### 3. 결과 다운로드

- 우측 상단 "📥 Download CSV" 클릭
- 모든 Subject의 검수 결과가 CSV로 저장됨

**CSV 형식:**
```csv
Subject ID,ID Validation,Gait Cycle Validation,Labeling Validation
SUBJ_039,pass,pass,pass
SUBJ_045,pass,fail,pass
```

### 4. 데이터 초기화

- "🗑️ 전체 초기화" 버튼으로 모든 데이터 삭제
- 새로운 데이터 세트로 다시 시작 가능

---

## 🔒 보안 고려사항

### 데이터 보안
- ✅ **모든 데이터는 브라우저에서만 처리됨**
- ✅ 서버로 전송되지 않음
- ✅ 파일은 브라우저 메모리에만 저장
- ✅ 페이지 새로고침 시 데이터 초기화

### HIPAA 준수
- 환자 데이터는 로컬에서만 처리
- 네트워크 전송 없음
- 서버 저장 없음

**단, 주의사항:**
- 공용 컴퓨터 사용 시 주의
- 작업 완료 후 브라우저 탭 닫기
- 중요 데이터는 다운로드 후 안전하게 보관

---

## 🎨 커스터마이징

### 로고 변경
HTML 파일 상단의 헤더 부분 수정:
```html
<h1>🚶 Your Organization Name — StrideX</h1>
```

### 색상 변경
CSS 부분의 그라디언트 색상 수정:
```css
background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
```

### 도메인 연결
- Netlify/Vercel에서 커스텀 도메인 설정
- 예: `dashboard.yourorganization.com`

---

## ❓ 문제 해결

### 1. 파일 업로드가 안 됨
- 브라우저 콘솔 확인 (F12)
- JSON 파일 형식 검증
- 파일 크기 확인 (브라우저 제한)

### 2. 폴더 업로드가 안 됨
- Chrome, Edge, Safari 사용 (Firefox는 제한적)
- 브라우저가 최신 버전인지 확인

### 3. 차트가 표시 안 됨
- 인터넷 연결 확인 (Plotly CDN 필요)
- 브라우저 JavaScript 활성화 확인

### 4. CSV 다운로드 안 됨
- 팝업 차단 해제
- 브라우저 다운로드 권한 확인

---

## 📱 모바일 지원

- 반응형 디자인 적용
- 태블릿에서 최적
- 스마트폰에서는 제한적 (큰 화면 권장)

---

## 🔄 업데이트 방법

### GitHub Pages
```bash
git pull origin main
# HTML 파일 수정
git add .
git commit -m "Update dashboard"
git push origin main
```

### Netlify/Vercel
- Git 푸시 시 자동 배포
- 또는 드래그 앤 드롭으로 재배포

---

## 📞 지원

문제가 있으면:
1. 브라우저 콘솔 확인
2. HTML 파일 검증
3. 네트워크 연결 확인

---

## ✅ 배포 체크리스트

- [ ] HTML 파일을 `index.html`로 이름 변경
- [ ] 배포 플랫폼 선택 (GitHub Pages/Netlify/Vercel)
- [ ] 저장소/프로젝트 생성
- [ ] 파일 업로드/푸시
- [ ] URL 접속 테스트
- [ ] 샘플 데이터로 기능 테스트
- [ ] 팀원에게 URL 공유
- [ ] (선택) 커스텀 도메인 설정

---

**추천 배포 순서:**
1. 🥇 **Netlify** (가장 쉬움, 드래그 앤 드롭)
2. 🥈 **GitHub Pages** (무료, 버전 관리)
3. 🥉 **Vercel** (빠른 속도)

모두 완전 무료이며 HTTPS를 자동 제공합니다! 🎉
