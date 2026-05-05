@echo off
REM Install GitHub Monitor Scheduled Tasks (with Admin privileges)
echo Requesting Administrator privileges...
echo.

powershell -Command "Start-Process powershell -Verb RunAs -ArgumentList '-ExecutionPolicy Bypass -File', '\"%~dp0install_scheduled_task.ps1\"'"

echo.
echo If a UAC prompt appeared, please click 'Yes' to continue.
echo.
pause
