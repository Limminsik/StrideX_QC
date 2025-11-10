#!/usr/bin/env python3
"""
테스트용 샘플 데이터 생성 스크립트

이 스크립트는 StrideX Dashboard 테스트를 위한
샘플 JSON 파일들을 생성합니다.
"""

import json
import os
from pathlib import Path

def create_sample_data():
    """샘플 데이터 생성"""
    
    # 출력 디렉토리 생성
    output_dir = Path("sample_data")
    output_dir.mkdir(exist_ok=True)
    
    print("🔨 샘플 데이터 생성 중...")
    
    # Subject 001 - 정상 케이스
    subjects = [
        {
            "id": "SUBJ_001",
            "gender": "1",
            "age": "40.0",
            "height": "170.0",
            "weight": "71.6",
            "bmi": "24.8",
            "class": "0",
            "diagnosis": "보행 시 특이사항 없음"
        },
        {
            "id": "SUBJ_002",
            "gender": "0",
            "age": "66.0",
            "height": "159.8",
            "weight": "52.1",
            "bmi": "20.4",
            "class": "1",
            "diagnosis": "관절염 증상으로 보행 시 좌우 균형이 맞지 않음"
        }
    ]
    
    created_files = []
    
    for subject in subjects:
        # Insole 데이터
        insole_data = {
            "meta": {
                "patient": {
                    "id": subject["id"],
                    "gender": subject["gender"],
                    "age": subject["age"],
                    "height": subject["height"],
                    "weight": subject["weight"],
                    "bmi": subject["bmi"],
                    "foot_size": "255.0",
                    "leg_length_L": "900.0",
                    "leg_length_R": "905.0",
                    "condition": "없음",
                    "symptom": None if subject["class"] == "0" else "보행시 통증"
                }
            },
            "data": {
                "smart_insole": {
                    "source_path": f"sample_data/{subject['id']}_insole.json",
                    "values": {}
                }
            },
            "labels": {
                "annotation": {
                    "class": subject["class"],
                    "side": None if subject["class"] == "0" else "좌측",
                    "region": None if subject["class"] == "0" else "무릎"
                },
                "diagnosis_text": subject["diagnosis"]
            }
        }
        
        # Day 1-10 데이터 생성
        for day in range(1, 11):
            insole_data["data"]["smart_insole"]["values"][f"day_{day}"] = {
                "balance": {
                    "L": "50" if subject["class"] == "0" else "48",
                    "R": "50" if subject["class"] == "0" else "52"
                },
                "stride_length": {
                    "L": str(130 + day),
                    "R": str(128 + day)
                },
                "gait_distance": str(1200 + day * 50),
                "gait_speed": str(round(3.5 + day * 0.2, 1)),
                "foot_pressure_fore": {
                    "L": str(35 + day % 5),
                    "R": str(40 + day % 5)
                },
                "foot_pressure_mid": {
                    "L": str(38 - day % 5),
                    "R": str(32 - day % 5)
                },
                "foot_pressure_rear": {
                    "L": str(27),
                    "R": str(28)
                },
                "foot_angle": {
                    "L": "1",
                    "R": "1"
                }
            }
        
        # IMU 데이터
        imu_data = {
            "meta": {
                "patient": {
                    "id": subject["id"],
                    "gender": subject["gender"],
                    "age": subject["age"],
                    "height": subject["height"],
                    "weight": subject["weight"],
                    "bmi": subject["bmi"],
                    "foot_size": "255.0",
                    "leg_length_L": "900.0",
                    "leg_length_R": "905.0",
                    "condition": "없음",
                    "symptom": None if subject["class"] == "0" else "보행시 통증"
                }
            },
            "data": {
                "imu_sensor": {
                    "source_path": f"sample_data/{subject['id']}_imu.json",
                    "values": {
                        "gait_cycle": {
                            "L": "1.1" if subject["class"] == "0" else "1.2",
                            "R": "1.1"
                        },
                        "knee_flexion_max": {
                            "L": "47" if subject["class"] == "0" else "69",
                            "R": "50" if subject["class"] == "0" else "57"
                        },
                        "knee_extension_max": {
                            "L": "13" if subject["class"] == "0" else "4",
                            "R": "11" if subject["class"] == "0" else "6"
                        },
                        "foot_clearance": {
                            "L": "10",
                            "R": "12"
                        }
                    }
                }
            },
            "labels": {
                "annotation": {
                    "class": subject["class"],
                    "side": None if subject["class"] == "0" else "좌측",
                    "region": None if subject["class"] == "0" else "무릎"
                },
                "diagnosis_text": subject["diagnosis"]
            }
        }
        
        # Pad 데이터
        pad_data = {
            "meta": {
                "patient": {
                    "id": subject["id"],
                    "gender": subject["gender"],
                    "age": subject["age"],
                    "height": subject["height"],
                    "weight": subject["weight"],
                    "bmi": subject["bmi"],
                    "foot_size": "255.0",
                    "leg_length_L": "900.0",
                    "leg_length_R": "905.0",
                    "condition": "없음",
                    "symptom": None if subject["class"] == "0" else "보행시 통증"
                }
            },
            "data": {
                "gait_pad": {
                    "source_path": f"sample_data/{subject['id']}_pad.json",
                    "values": {
                        "step_length": {
                            "L": "72.6" if subject["class"] == "0" else "49.4",
                            "R": "72.3" if subject["class"] == "0" else "48.2"
                        },
                        "velocity": "130.6" if subject["class"] == "0" else "76.8",
                        "stance_phase_rate": {
                            "L": "63.5" if subject["class"] == "0" else "65.1",
                            "R": "62.8" if subject["class"] == "0" else "65.6"
                        },
                        "swing_phase_rate": {
                            "L": "36.5" if subject["class"] == "0" else "34.8",
                            "R": "37.2" if subject["class"] == "0" else "34.4"
                        },
                        "double_support_time": {
                            "L": "26.2" if subject["class"] == "0" else "30.8",
                            "R": "26.4" if subject["class"] == "0" else "30.5"
                        }
                    }
                }
            },
            "labels": {
                "annotation": {
                    "class": subject["class"],
                    "side": None if subject["class"] == "0" else "좌측",
                    "region": None if subject["class"] == "0" else "무릎"
                },
                "diagnosis_text": subject["diagnosis"]
            }
        }
        
        # 파일 저장
        files = [
            (f"lb_insole_{subject['id']}.json", insole_data),
            (f"lb_imu_{subject['id']}.json", imu_data),
            (f"lb_pad_{subject['id']}.json", pad_data)
        ]
        
        for filename, data in files:
            filepath = output_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            created_files.append(filepath)
            print(f"  ✅ 생성: {filepath}")
    
    print(f"\n✨ 완료! {len(created_files)}개의 샘플 파일이 생성되었습니다.")
    print(f"📁 위치: {output_dir.absolute()}")
    print(f"\n💡 사용 방법:")
    print(f"   1. Python 서버 실행: python run_local_server.py")
    print(f"   2. 브라우저에서 '📁 폴더 선택' 클릭")
    print(f"   3. sample_data 폴더 선택")
    
    return created_files

if __name__ == "__main__":
    create_sample_data()
