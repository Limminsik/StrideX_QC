#!/usr/bin/env python3
"""
StrideX Dashboard 웹 서버 (로컬 + 외부 접속 가능)

사용법:
    python run_local_server.py
    
로컬 접속: http://localhost:8000
외부 접속: http://[본인IP주소]:8000
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import socket
from pathlib import Path

# 설정
PORT = 8000
DIRECTORY = "."

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """CORS를 허용하는 커스텀 HTTP 핸들러"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # CORS 헤더 추가
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    
    def log_message(self, format, *args):
        """로그 메시지 포맷팅"""
        sys.stdout.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format % args))

def get_local_ip():
    """로컬 IP 주소 가져오기"""
    try:
        # 외부 서버에 연결하여 로컬 IP 확인
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        try:
            # 대체 방법
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            return ip
        except:
            return "127.0.0.1"

def check_files():
    """필요한 파일 존재 확인"""
    html_file = Path("stridex_dashboard_final.html")
    
    if not html_file.exists():
        # index.html도 확인
        if Path("index.html").exists():
            print("✅ index.html 파일을 찾았습니다.")
            return True
        print("❌ 오류: stridex_dashboard_final.html 또는 index.html 파일을 찾을 수 없습니다.")
        print(f"   현재 디렉토리: {os.getcwd()}")
        return False
    
    print("✅ stridex_dashboard_final.html 파일을 찾았습니다.")
    return True

def main():
    """메인 함수"""
    print("=" * 60)
    print("🚶 StrideX Dashboard 로컬 테스트 서버")
    print("=" * 60)
    
    # 파일 확인
    if not check_files():
        sys.exit(1)
    
    # 서버 설정
    handler = CustomHTTPRequestHandler
    
    # 로컬 IP 주소 가져오기
    local_ip = get_local_ip()
    
    try:
        # 0.0.0.0으로 바인딩하여 외부 접속 허용
        with socketserver.TCPServer(("0.0.0.0", PORT), handler) as httpd:
            local_url = f"http://localhost:{PORT}"
            external_url = f"http://{local_ip}:{PORT}"
            
            # index.html이 있으면 그것을, 없으면 stridex_dashboard_final.html 사용
            html_file = "index.html" if Path("index.html").exists() else "stridex_dashboard_final.html"
            local_url += f"/{html_file}"
            external_url += f"/{html_file}"
            
            print(f"\n✅ 서버가 시작되었습니다!")
            print(f"\n📍 접속 주소:")
            print(f"   로컬:  {local_url}")
            print(f"   외부:  {external_url}")
            print(f"\n💡 사용 방법:")
            print(f"   1. 브라우저에서 위 주소로 접속")
            print(f"   2. JSON 파일 또는 폴더 업로드")
            print(f"   3. 데이터 검수 진행")
            print(f"\n🌐 외부 접속 안내:")
            print(f"   - 같은 네트워크의 다른 기기에서 {external_url} 로 접속 가능")
            print(f"   - 방화벽에서 포트 {PORT}를 허용해야 할 수 있습니다")
            print(f"   - Windows 방화벽: 제어판 > Windows Defender 방화벽 > 고급 설정")
            print(f"   - 인바운드 규칙 추가: 포트 {PORT} (TCP) 허용")
            print(f"\n⚠️  종료하려면 Ctrl+C를 누르세요")
            print("=" * 60)
            
            # 자동으로 브라우저 열기
            try:
                webbrowser.open(local_url)
                print(f"\n🌐 브라우저를 자동으로 열었습니다.")
            except:
                print(f"\n⚠️  브라우저를 수동으로 열어주세요: {local_url}")
            
            print("\n📊 서버 로그:")
            print("-" * 60)
            
            # 서버 실행
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 서버를 종료합니다...")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"\n❌ 오류: 포트 {PORT}가 이미 사용 중입니다.")
            print(f"   다른 프로그램이 {PORT} 포트를 사용하고 있는지 확인하세요.")
            print(f"   또는 코드에서 PORT 변수를 다른 값으로 변경하세요.")
        else:
            print(f"\n❌ 오류: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 예상치 못한 오류: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
