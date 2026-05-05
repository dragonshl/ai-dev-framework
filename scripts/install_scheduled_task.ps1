# Install GitHub Monitor as Windows Scheduled Task
# Creates two daily tasks: 12:00 PM and 12:00 AM

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "GitHub Monitor - Scheduled Task Installer" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$monitorScript = Join-Path $scriptPath "run_github_monitor.bat"
$taskName1 = "GitHub-Monitor-Noon"
$taskName2 = "GitHub-Monitor-Midnight"

Write-Host "Installing scheduled tasks..." -ForegroundColor Yellow
Write-Host ""

# Remove existing tasks if they exist
Write-Host "Removing existing tasks (if any)..." -ForegroundColor Gray
schtasks /delete /tn "$taskName1" /f 2>$null
schtasks /delete /tn "$taskName2" /f 2>$null

# Create noon task (12:00 PM)
Write-Host "Creating noon task (12:00 PM)..." -ForegroundColor Green
schtasks /create /tn "$taskName1" /tr "$monitorScript" /sc daily /st 12:00 /rl highest /f

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Noon task created successfully" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to create noon task" -ForegroundColor Red
}

Write-Host ""

# Create midnight task (12:00 AM)
Write-Host "Creating midnight task (12:00 AM)..." -ForegroundColor Green
schtasks /create /tn "$taskName2" /tr "$monitorScript" /sc daily /st 00:00 /rl highest /f

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Midnight task created successfully" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to create midnight task" -ForegroundColor Red
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Installation Complete!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Scheduled Tasks:" -ForegroundColor Yellow
Write-Host "  • $taskName1 - Runs daily at 12:00 PM" -ForegroundColor White
Write-Host "  • $taskName2 - Runs daily at 12:00 AM" -ForegroundColor White
Write-Host ""
Write-Host "Reports will be saved to:" -ForegroundColor Yellow
Write-Host "  $($scriptPath)\github-monitor-reports\" -ForegroundColor White
Write-Host ""
Write-Host "To view tasks:" -ForegroundColor Yellow
Write-Host "  schtasks /query | findstr GitHub" -ForegroundColor Gray
Write-Host ""
Write-Host "To remove tasks:" -ForegroundColor Yellow
Write-Host "  schtasks /delete /tn `"$taskName1`" /f" -ForegroundColor Gray
Write-Host "  schtasks /delete /tn `"$taskName2`" /f" -ForegroundColor Gray
Write-Host ""
