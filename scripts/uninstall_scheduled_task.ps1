# Uninstall GitHub Monitor Scheduled Tasks

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "GitHub Monitor - Scheduled Task Remover" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$taskName1 = "GitHub-Monitor-Noon"
$taskName2 = "GitHub-Monitor-Midnight"

Write-Host "Removing scheduled tasks..." -ForegroundColor Yellow
Write-Host ""

# Remove noon task
Write-Host "Removing noon task..." -ForegroundColor Gray
schtasks /delete /tn "$taskName1" /f

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Noon task removed successfully" -ForegroundColor Green
} else {
    Write-Host "⚠️  Noon task not found or already removed" -ForegroundColor Yellow
}

Write-Host ""

# Remove midnight task
Write-Host "Removing midnight task..." -ForegroundColor Gray
schtasks /delete /tn "$taskName2" /f

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Midnight task removed successfully" -ForegroundColor Green
} else {
    Write-Host "⚠️  Midnight task not found or already removed" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Uninstallation Complete!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Note: Report files in github-monitor-reports/ were NOT deleted." -ForegroundColor Yellow
Write-Host "To delete reports manually, remove the folder:" -ForegroundColor Yellow
Write-Host "  scripts\github-monitor-reports\" -ForegroundColor Gray
Write-Host ""
