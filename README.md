# Gait Physiological Signal Dashboard - StrideX

## 개요

StrideX는 **["초거대 AI 확산 생태계 조성 사업"](https://www.msit.go.kr/bbs/view.do?mId=311&bbsSeqNo=100&nttSeqNo=3179387)'의 "2025년 초거대 AI 학습용 데이터 품질검증"** 활용을 위해 개발된 품질 전문 도구입니다.

보행 관련 센서데이터 기반의 근골격계 질환 생체신호 데이터 **의미정확성** 검증을 목적으로 설계되었으며 무릎관절염 등 근골격계 질환 환자의 보행 신호 라벨링 품질을 검증하는 데 특화되어 있습니다.

![StrideX Dashboard](../StrideX%20Dashboard(v1.0).png)

---

## ⚡ 빠른 시작

### 1️⃣ 로컬에서 바로 테스트

```bash
# Python 스크립트 실행
python run_local_server.py
```

브라우저가 자동으로 열리고 `http://localhost:8000`에서 접속 가능합니다!

### 2️⃣ 외부인에게 링크 공유하기 (Netlify 배포) 🌟

```bash
# 1. 배포 준비
prepare_for_netlify.bat 실행

# 2. https://www.netlify.com 접속 후 가입
# 3. "Deploy manually" → 폴더 드래그 앤 드롭
# 4. 완료! (1분 소요)
```

**결과:** 영구적인 공개 URL (예: `https://stridex-dashboard.netlify.app`)
- ✅ 완전 무료
- ✅ 영구적인 URL
- ✅ HTTPS 자동 제공

**자세한 가이드:** `DEPLOYMENT_GUIDE.md` 참고

---

## 주요 기능

### 생체신호 데이터
- **IMU 센서**: 좌/우 무릎 관절의 보행 지표 비교 분석
- **스마트인솔**: 일별 압력 분포 및 보행 패턴 추이 분석  
- **보행매트**: 보행 주기, 속도, 입각기/유각기 비율 등 종합 분석

### 의미정확성 검증
- **라벨링 정보**: 질환 분류(정상/무릎관절염), 병변 측, 부위, 진단 내용 표시
- **환자 생체신호 시각화**: 좌측 발(파란색), 우측 발(주황색) 기반 환자 보행 신호 시각화
- **지표 설명**: 각 센서별 측정 지표의 의미와 단위 자동 표시

### 데이터 관리
- ✅ **개별 파일 업로드**: 여러 JSON 파일 선택
- ✅ **폴더 업로드**: 폴더 전체 업로드로 자동 읽기
- ✅ **자동 정렬**: Subject ID 순으로 자동 정렬 (SUBJ_001, SUBJ_002...)
- ✅ **ID 검증**: 3개 센서 파일의 ID 일치 여부 자동 확인

### 검수 시스템
- ✓ **3단계 검수**: ID 검증 / Gait Cycle / Labeling
- ✓ **Pass/Fail 버튼**: 클릭만으로 검수 진행
- ✓ **상태 표시**: 검수 진행 상황 실시간 표시
- 💾 **CSV 다운로드**: 검수 결과 타임스탬프와 함께 저장

### 다양한 데이터 형식 지원
- 스마트인솔, 보행매트, IMU 센서 등 다양한 생체신호 데이터 형식 지원
- 데이터 유형 및 구조별 자동 인식 및 분류

---

## 센서별 측정 지표

### 👟 스마트인솔 (Smart Insole)
발바닥 압력 분포를 센서로 측정하여 보행 시 발의 접촉 패턴과 균형을 분석합니다.

| 지표 | 설명 | 단위 |
|------|------|------|
| `gait_speed` | 보행 속도 | km/h |
| `foot_pressure_rear` | 후방 압력 - 발뒤꿈치 부분의 압력 비율 | % |
| `foot_pressure_mid` | 중앙 압력 - 발 중앙 부분의 압력 비율 | % |
| `foot_pressure_fore` | 전방 압력 - 발 앞부분의 압력 비율 | % |
| `balance` | 좌우 균형 - 양발 간의 압력 균형 | % |
| `foot_angle` | 발각도 - 발의 정렬 상태 (0: 내반슬, 1: 정상, 2: 외반슬) | 0, 1, 2 |
| `gait_distance` | 보행 거리 | 미터(m) |
| `stride_length` | 보폭 - 한 걸음의 길이 | 센티미터(cm) |

### 🦵 IMU 센서 (Inertial Measurement Unit)
무릎 관절의 움직임을 3축 가속도계와 자이로스코프로 측정하여 보행 패턴을 분석합니다.

| 지표 | 설명 | 단위 |
|------|------|------|
| `gait_cycle` | 보행 주기 - 한 걸음이 완료되는 데 걸리는 시간 | 초(s) |
| `knee_flexion_max` | 무릎 굴곡 최대각 - 무릎이 구부러지는 최대 각도 | 도(deg) |
| `knee_extension_max` | 무릎 신전 최대각 - 무릎이 펴지는 최대 각도 | 도(deg) |
| `foot_clearance` | 발 들림 높이 - 보행 시 발이 바닥에서 떠오르는 최대 높이 | 밀리미터(mm) |

### 🚶 보행매트 (Gait Pad)
보행 시 발의 접촉 패턴을 매트 센서로 측정하여 보행의 시간적 특성을 분석합니다.

| 지표 | 설명 | 단위 |
|------|------|------|
| `step_length` | 보폭 - 한 걸음의 길이 | 센티미터(cm) |
| `velocity` | 보행 속도 | cm/s |
| `stance_phase_rate` | 입각기 비율 - 발이 땅에 닿아있는 시간 비율 | % |
| `swing_phase_rate` | 유각기 비율 - 발이 공중에 있는 시간 비율 | % |
| `double_support_time` | 양측지지시간 - 양발이 모두 땅에 닿아있는 시간 비율 | % |

---

## 데이터 형식

### JSON 구조

```json
{
  "meta": {
    "patient": {
      "id": "SUBJ_001",
      "gender": "1",
      "age": "40.0",
      "height": "170.0",
      "weight": "71.6",
      "bmi": "24.8",
      "foot_size": "260",
      "leg_length_L": "85.0",
      "leg_length_R": "85.0",
      "condition": "정상",
      "symptom": null
    }
  },
  "data": {
    "smart_insole": {
      "values": {
        "day_1": {
          "balance": { "L": "50.0", "R": "50.0" },
          "stride_length": { "L": "119.9", "R": "110.4" },
          "gait_speed": "3.4",
          "foot_pressure_fore": { "L": "33", "R": "34" },
          "foot_pressure_mid": { "L": "32", "R": "33" },
          "foot_pressure_rear": { "L": "35", "R": "33" }
        }
      }
    },
    "imu_sensor": {
      "values": {
        "gait_cycle": { "L": "1.2", "R": "1.3" },
        "knee_flexion_max": { "L": "45.2", "R": "42.1" },
        "knee_extension_max": { "L": "15.3", "R": "14.8" },
        "foot_clearance": { "L": "12.5", "R": "11.8" }
      }
    },
    "gait_pad": {
      "values": {
        "step_length": { "L": "71.2", "R": "70.5" },
        "velocity": "132.4",
        "stance_phase_rate": { "L": "39.8", "R": "40.1" },
        "swing_phase_rate": { "L": "60.2", "R": "59.9" },
        "double_support_time": { "L": "18.5", "R": "18.5" }
      }
    }
  },
  "labels": {
    "annotation": {
      "class": "0",
      "side": null,
      "region": null
    },
    "diagnosis_text": "임상의 진단 소견"
  }
}
```

### 파일 명명 규칙

- ✅ `*_insole_*.json` → Smart Insole
- ✅ `*_imu_*.json` → IMU Sensor  
- ✅ `*_pad_*.json` → Gait Pad

**예시:**
- `lb_01_insole_039.json` ✓
- `subject_002_imu.json` ✓
- `data_pad_045.json` ✓

---

## 사용법

### 기본 사용 흐름

1. **데이터 로드**: "📄 파일 선택" 또는 "📁 폴더 선택" 버튼을 클릭하여 데이터 업로드
2. **데이터 선택**: 왼쪽 패널에서 검증할 Subject 선택
3. **데이터 확인**: 
   - 중앙 패널에서 센서별 데이터 시각화 확인
   - 오른쪽 패널에서 환자 메타 정보 및 라벨링 정보 확인
4. **데이터 검증 수행**: 
   - 상단의 Pass/Fail 버튼으로 검수 진행
   - ID 검증 / Gait Cycle / Labeling 3단계 검증
5. **결과 다운로드**: "📥 Download CSV" 버튼으로 검수 결과 저장

### 상세 가이드

- 📖 **로컬 테스트**: `LOCAL_TEST_GUIDE.md`
- 🚀 **웹 배포**: `DEPLOYMENT_GUIDE.md` (Netlify, GitHub Pages 등)

---

## 데이터 품질 검증을 통한 품질 확보 기대효과

### 무릎관절염 진단 지원
- 좌/우 무릎 관절의 비대칭성 분석
- 보행 패턴의 이상 징후 감지
- 치료 전후 비교 분석

### 보행 능력 평가
- 보행 속도, 보폭, 균형 능력 종합 평가
- 일상생활 활동 능력 예측
- 재활 치료 효과 모니터링

### 의미정확성 검증
- 생체신호 데이터와 라벨링 정보 간 정렬성 검증
- 라벨링 품질 자동화 검수
- 검수 결과 추적 및 관리

---

## 📦 패키지 내용물

```
stridex-dashboard/
├── stridex_dashboard_final.html    ⭐ 메인 대시보드 (웹 배포용)
│
├── 🖥️ 서버 실행 스크립트
│   └── run_local_server.py             로컬 테스트 서버 (localhost)
│
├── 🚀 배포 도구
│   └── prepare_for_netlify.bat         Netlify 배포 준비 스크립트
│
├── 📚 가이드 문서
│   ├── README.md                        이 파일 (전체 가이드)
│   ├── LOCAL_TEST_GUIDE.md             로컬 테스트 상세 가이드
│   └── DEPLOYMENT_GUIDE.md             웹 배포 가이드 (Netlify, GitHub Pages 등)
│
├── 🔨 유틸리티
│   └── create_sample_data.py           샘플 데이터 생성기
│
└── 📁 데이터
    └── dataset/                         실제 데이터셋 (선택사항)
```

---

## 🔒 보안 및 프라이버시

### 데이터 처리
- ✅ 모든 데이터는 **브라우저에서만** 처리
- ✅ 서버로 전송 **절대 안 됨**
- ✅ 파일은 메모리에만 임시 저장
- ✅ 페이지 새로고침 시 자동 삭제

### HIPAA 준수
- ✅ 환자 데이터 로컬 처리
- ✅ 네트워크 전송 없음
- ✅ 서버 저장 없음

**주의사항:**
- 공용 컴퓨터 사용 후 브라우저 탭 닫기
- 중요 데이터는 다운로드 후 안전하게 보관

---

## 🌐 브라우저 지원

### 권장 브라우저
- ✅ Chrome 90+ (최적)
- ✅ Edge 90+
- ✅ Safari 14+
- ⚠️ Firefox 88+ (폴더 업로드 제한적)

### 모바일
- 📱 태블릿에서 최적
- 📱 스마트폰은 큰 화면 권장

---

## 📞 지원 및 문제 해결

### 일반적인 문제

**Q: 파일 업로드가 안 돼요**
```
A: 
1. JSON 파일 형식 확인
2. 파일 크기 확인 (브라우저 제한)
3. 브라우저 콘솔(F12) 확인
```

**Q: 폴더 업로드가 안 돼요**
```
A:
1. Chrome/Edge/Safari 사용
2. Firefox는 제한적 지원
3. 브라우저 최신 버전 확인
```

**Q: CSV 다운로드가 안 돼요**
```
A:
1. 팝업 차단 해제
2. 최소 1개 검증 완료 필요
3. 다운로드 권한 확인
```

**Q: Subject가 정렬이 안 돼요**
```
A:
새로고침 후 다시 업로드
(SUBJ_001, SUBJ_002... 순서로 자동 정렬됨)
```

---

## Fund

***본 도구는 한국지능정보사회진흥원의 '초거대 AI 확산 생태계 조성 사업'의 '초거대 AI 학습용 데이터 품질검증' 사업의 지원을 받아 개발되었음(R25TA0074842300)***

---

## License

**GCU License**  Copyright (c) 2025 Limminsik

---

## Information

- **Version**: 1.1
- **Date**: 2025.01
- **Contact**: ms4002@gachon.ac.kr

### 버전 히스토리

#### v1.1 (최신)
- 🚀 **배포 기능 추가**
  - ✅ Netlify 배포 자동화 스크립트
  - ✅ 웹 배포 가이드 문서
- 🎨 UI 개선
  - ✅ Plotly 차트 툴바 제거
  - ✅ Gait Cycle 차트 제거 (레이아웃 정리)

#### v1.0 (초기 릴리즈)
- ✨ 초기 릴리즈
- ✅ 파일/폴더 업로드
- ✅ Subject 자동 정렬
- ✅ ID 검증 자동화
- ✅ Gait Cycle 계산
- ✅ Pass/Fail 검수 시스템
- ✅ CSV 다운로드
- ✅ 전체 초기화
- ✅ 에러 핸들링 강화

---

**✨ 성공적인 데이터 검수를 기원합니다! ✨**
