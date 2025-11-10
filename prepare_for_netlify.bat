@echo off
chcp 65001 >nul
echo ============================================================
echo 🌐 Netlify 배포 준비
echo ============================================================
echo.

cd /d "%~dp0"

if not exist "stridex_dashboard_final.html" (
    echo ❌ 오류: stridex_dashboard_final.html 파일을 찾을 수 없습니다.
    pause
    exit /b 1
)

if exist "index.html" (
    echo ⚠️  index.html 파일이 이미 존재합니다.
    echo.
    set /p overwrite="덮어쓰시겠습니까? (Y/N): "
    if /i not "%overwrite%"=="Y" (
        echo 취소되었습니다.
        pause
        exit /b 0
    )
)

copy /Y "stridex_dashboard_final.html" "index.html" >nul

if exist "index.html" (
    echo.
    echo ✅ 준비 완료!
    echo.
    echo 📋 다음 단계:
    echo    1. https://www.netlify.com 접속
    echo    2. "Add new site" → "Deploy manually" 클릭
    echo    3. 이 폴더를 드래그 앤 드롭
    echo    4. 완료! 공개 URL이 생성됩니다.
    echo.
) else (
    echo ❌ 오류: 파일 복사 실패
)

pause

