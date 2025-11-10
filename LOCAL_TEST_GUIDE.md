# StrideX Dashboard 로컬 테스트 가이드

## 📦 필요한 파일

```
stridex-dashboard/
├── stridex_dashboard_final.html   (또는 index.html)
├── run_local_server.py             (Python 서버 스크립트)
└── sample_data/                    (선택사항: 테스트용 JSON 파일들)
    ├── lb_01_insole_039.json
    ├── lb_01_imu_039.json
    ├── lb_01_pad_039.json
    ├── lb_02_insole_045.json
    ├── lb_02_imu_045.json
    └── lb_02_pad_045.json
```

---

## 🚀 실행 방법

### 방법 1: Python 서버 스크립트 사용 (추천)

```bash
# 1. 디렉토리 이동
cd /path/to/stridex-dashboard

# 2. Python 서버 실행
python run_local_server.py

# 또는 Python 3 명시
python3 run_local_server.py
```

**자동으로 실행되는 것:**
- ✅ 포트 8000에서 HTTP 서버 시작
- ✅ 브라우저 자동 실행
- ✅ CORS 설정 자동 적용
- ✅ 파일 존재 여부 확인

**출력 예시:**
```
============================================================
🚶 StrideX Dashboard 로컬 테스트 서버
============================================================

✅ stridex_dashboard_final.html 파일을 찾았습니다.

✅ 서버가 시작되었습니다!
📍 주소: http://localhost:8000/stridex_dashboard_final.html

💡 사용 방법:
   1. 브라우저에서 위 주소로 접속
   2. JSON 파일 또는 폴더 업로드
   3. 데이터 검수 진행

⚠️  종료하려면 Ctrl+C를 누르세요
============================================================

🌐 브라우저를 자동으로 열었습니다.

📊 서버 로그:
------------------------------------------------------------
```

### 방법 2: Python 기본 명령어 사용

```bash
# Python 3 (추천)
python3 -m http.server 8000

# Python 2 (레거시)
python -m SimpleHTTPServer 8000
```

그 후 브라우저에서 접속:
```
http://localhost:8000/stridex_dashboard_final.html
```

### 방법 3: Node.js 사용 (http-server)

```bash
# http-server 설치 (한 번만)
npm install -g http-server

# 서버 실행
http-server -p 8000 -c-1

# 접속
http://localhost:8000/stridex_dashboard_final.html
```

---

## 🧪 테스트 시나리오

### 1️⃣ 기본 기능 테스트

1. **서버 시작**
   ```bash
   python run_local_server.py
   ```

2. **브라우저 접속**
   - 자동으로 열림
   - 또는 `http://localhost:8000` 수동 접속

3. **빈 상태 확인**
   - 왼쪽: "데이터 추가" 섹션
   - 중앙: "데이터를 선택하세요" 메시지
   - 오른쪽: "환자 정보" 빈 상태

### 2️⃣ 파일 업로드 테스트

**개별 파일 업로드:**
```
1. "📄 파일 선택" 클릭
2. 3개의 JSON 파일 선택 (Ctrl+클릭)
   - lb_01_insole_039.json
   - lb_01_imu_039.json
   - lb_01_pad_039.json
3. "열기" 클릭
4. ✅ "3/3개의 파일이 성공적으로 업로드되었습니다" 확인
```

**폴더 업로드:**
```
1. "📁 폴더 선택" 클릭
2. sample_data 폴더 선택
3. ✅ "6/6개의 파일이 성공적으로 업로드되었습니다" 확인
4. 왼쪽에 SUBJ_001, SUBJ_002 순서로 표시 확인
```

### 3️⃣ Subject 정렬 테스트

**업로드 후 자동 정렬 확인:**
- ✅ SUBJ_001 (또는 SUBJ_039)
- ✅ SUBJ_002 (또는 SUBJ_045)
- ✅ 숫자 순으로 자동 정렬됨

### 4️⃣ ID 검증 테스트

**정상 케이스:**
```
1. SUBJ_039 선택
2. 중앙 상단에 "✓ ID 검증 완료" 녹색 메시지 확인
3. 3개 파일 모두 동일한 ID (SUBJ_039)
```

**오류 케이스 (의도적):**
```
1. 다른 ID를 가진 파일 3개 업로드
2. "✗ ID 불일치" 빨간 메시지 확인
```

### 5️⃣ Gait Cycle 계산 테스트

```
1. SUBJ_039 선택
2. 중앙 패널에서 "Smart Insole - Gait Cycle" 섹션 확인
3. Day 1-10 모두 표시되는지 확인
4. 각 Day별 L/R 값 계산 확인
   예: Day 1
   - Stride Length L: 142 cm
   - Gait Speed: 4.4 km/h → 1.22 m/s
   - Gait Cycle L = 1.42 / 1.22 ≈ 1.16s
```

### 6️⃣ Pass/Fail 검증 테스트

```
1. SUBJ_039 선택
2. 상단에서:
   - "ID 검증" → Pass 클릭
   - "Gait Cycle" → Pass 클릭
   - "Labeling" → Pass 클릭
3. 왼쪽 Subject 리스트에 "✓ 검증완료" 표시 확인
4. "📥 Download CSV" 클릭
5. CSV 파일 다운로드 확인
```

### 7️⃣ 초기화 테스트

```
1. "🗑️ 전체 초기화" 클릭
2. 확인 대화상자에서 "확인" 클릭
3. 모든 데이터 삭제 확인
4. 빈 상태로 복귀 확인
```

---

## 🐛 에러 처리 테스트

### 1. 잘못된 JSON 파일

**테스트용 잘못된 JSON 만들기:**
```json
{
  "invalid": "json",
  "no_meta": true
}
```

**예상 결과:**
```
❌ 오류 발생 파일 (1개):
- invalid.json: 유효하지 않은 JSON 구조: meta.patient.id가 없습니다.
```

### 2. 빈 폴더 선택

**예상 결과:**
```
❌ JSON 파일이 없습니다.
```

### 3. 파일명에 센서 유형 없음

**파일명:** `data_001.json`

**예상 결과:**
```
⚠️ 콘솔 경고: 파일 유형을 알 수 없습니다: data_001.json
```

### 4. Subject 선택 없이 Pass/Fail 클릭

**예상 결과:**
```
❌ Subject를 먼저 선택해주세요.
```

---

## 🔍 브라우저 콘솔 체크

### 콘솔 열기
- **Chrome/Edge:** F12 또는 Ctrl+Shift+I
- **Firefox:** F12 또는 Ctrl+Shift+K
- **Safari:** Cmd+Option+I

### 확인할 항목

**정상 로그:**
```
✅ "SUBJ_039의 insole 데이터가 업데이트되었습니다."
```

**에러 로그 (없어야 함):**
```
❌ Uncaught TypeError
❌ Uncaught ReferenceError
❌ Failed to fetch
```

---

## 📊 성능 테스트

### 대량 파일 업로드

**테스트:**
```
1. 30개 이상의 JSON 파일 업로드
2. 로딩 시간 확인
3. 메모리 사용량 확인 (개발자 도구 → Performance)
```

**예상:**
- ✅ 100개 파일: ~2-3초
- ✅ 브라우저 멈춤 없음
- ✅ 메모리 사용량: ~50MB 이하

---

## 🔧 문제 해결

### 1. 서버가 시작되지 않음

**원인:** 포트 8000이 이미 사용 중

**해결:**
```bash
# 다른 포트 사용
python run_local_server.py  # 스크립트에서 PORT 변수 수정

# 또는
python3 -m http.server 8080  # 다른 포트 번호
```

### 2. 브라우저가 자동으로 열리지 않음

**해결:**
- 수동으로 `http://localhost:8000` 접속
- 또는 서버 로그에 표시된 URL 복사

### 3. 파일 업로드 후 반응 없음

**확인사항:**
1. 브라우저 콘솔에서 JavaScript 에러 확인
2. JSON 파일 형식 검증
3. 파일 크기 확인 (브라우저 제한)

**해결:**
```javascript
// 콘솔에서 확인
console.log(subjects);  // 업로드된 데이터 확인
```

### 4. CSV 다운로드 안 됨

**확인사항:**
- 팝업 차단 해제
- 브라우저 다운로드 권한 확인
- 최소 1개 이상 검증 완료

---

## 📱 브라우저 호환성

### 지원 브라우저
- ✅ Chrome 90+
- ✅ Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+

### 폴더 업로드 지원
- ✅ Chrome, Edge, Safari
- ⚠️ Firefox (제한적 - webkitdirectory 지원 필요)

---

## 💾 샘플 데이터 생성

직접 테스트용 JSON 파일을 만들려면:

```python
# create_sample_data.py
import json

sample_data = {
    "meta": {
        "patient": {
            "id": "SUBJ_001",
            "gender": "1",
            "age": "40.0",
            "height": "170.0",
            "weight": "70.0",
            "bmi": "24.2"
        }
    },
    "data": {
        "smart_insole": {
            "values": {
                "day_1": {
                    "balance": {"L": "50", "R": "50"},
                    "stride_length": {"L": "140", "R": "135"},
                    "gait_speed": "4.5"
                }
            }
        }
    },
    "labels": {
        "annotation": {
            "class": "0",
            "side": None,
            "region": None
        },
        "diagnosis_text": "정상"
    }
}

with open('test_insole_001.json', 'w', encoding='utf-8') as f:
    json.dump(sample_data, f, indent=2, ensure_ascii=False)
```

---

## ✅ 최종 체크리스트

배포 전 확인사항:

- [ ] Python 서버로 로컬 테스트 완료
- [ ] 파일 업로드 (개별/폴더) 정상 작동
- [ ] Subject 정렬 확인 (숫자 순)
- [ ] ID 검증 정상 작동
- [ ] Gait Cycle 계산 정확성 확인
- [ ] Pass/Fail 버튼 정상 작동
- [ ] CSV 다운로드 정상 작동
- [ ] 초기화 기능 정상 작동
- [ ] 브라우저 콘솔 에러 없음
- [ ] 모바일/태블릿 반응형 확인

---

**테스트 완료 후 배포 진행! 🚀**
