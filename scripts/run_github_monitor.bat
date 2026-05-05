@echo off
REM GitHub Monitor - Scheduled Task Runner
REM Runs twice daily: 12:00 PM and 12:00 AM

echo ========================================
echo GitHub Repository Monitor
echo Running at: %date% %time%
echo ========================================
echo.

REM Navigate to script directory
cd /d "%~dp0"

REM Run the Python monitor script
python github_monitor.py

REM Check exit code
if %errorlevel% equ 0 (
    echo.
    echo ✅ Monitor completed successfully - No issues found
) else (
    echo.
    echo ⚠️  Monitor completed with alerts - Check reports!
)

echo.
echo Report saved to: github-monitor-reports\latest.txt
echo ========================================
