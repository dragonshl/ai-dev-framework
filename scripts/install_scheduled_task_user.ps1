# Install GitHub Monitor as Windows Scheduled Task (No Admin Required)
# Creates two daily tasks: 12:00 PM and 12:00 AM

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "GitHub Monitor - Scheduled Task Installer" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$monitorScript = Join-Path $scriptPath "run_github_monitor.bat"
$taskName1 = "GitHub-Monitor-Noon"
$taskName2 = "GitHub-Monitor-Midnight"

Write-Host "Installing scheduled tasks (user context)..." -ForegroundColor Yellow
Write-Host ""

try {
    # Create Task Scheduler COM object
    $scheduler = New-Object -ComObject Schedule.Service
    $scheduler.Connect()
    
    # Get root folder
    $rootFolder = $scheduler.GetFolder("\")
    
    # Function to create task
    function Create-Task {
        param($taskName, $startTime)
        
        Write-Host "Creating task: $taskName at $startTime..." -ForegroundColor Gray
        
        # Create task definition
        $taskDefinition = $scheduler.NewTask(0)
        
        # Set registration info
        $taskDefinition.RegistrationInfo.Description = "GitHub Repository Monitor - $taskName"
        $taskDefinition.RegistrationInfo.Author = [Environment]::UserName
        
        # Set settings
        $taskDefinition.Settings.Enabled = $true
        $taskDefinition.Settings.StartWhenAvailable = $true
        $taskDefinition.Settings.DisallowStartIfOnBatteries = $false
        $taskDefinition.Settings.StopIfGoingOnBatteries = $false
        
        # Create trigger (daily)
        $trigger = $taskDefinition.Triggers.Create(1)  # 1 = TASK_TRIGGER_DAILY
        $trigger.StartBoundary = (Get-Date).ToString("yyyy-MM-dd") + "T" + $startTime + ":00"
        $trigger.DaysInterval = 1
        
        # Create action
        $action = $taskDefinition.Actions.Create(0)  # 0 = TASK_ACTION_EXEC
        $action.Path = $monitorScript
        $action.WorkingDirectory = $scriptPath
        
        # Register task
        $rootFolder.RegisterTaskDefinition(
            $taskName,
            $taskDefinition,
            6,  # TASK_CREATE_OR_UPDATE
            $null,  # User (null = current user)
            $null,  # Password
            3  # TASK_LOGON_INTERACTIVE_TOKEN
        )
        
        Write-Host "✅ Task '$taskName' created successfully" -ForegroundColor Green
    }
    
    # Create both tasks
    Create-Task $taskName1 "12:00:00"
    Write-Host ""
    Create-Task $taskName2 "00:00:00"
    
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
    Write-Host "  $scriptPath\github-monitor-reports\" -ForegroundColor White
    Write-Host ""
    Write-Host "To verify installation:" -ForegroundColor Yellow
    Write-Host "  schtasks /query | findstr GitHub" -ForegroundColor Gray
    Write-Host ""
    
} catch {
    Write-Host ""
    Write-Host "❌ Error creating tasks: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "This method requires Windows Task Scheduler access." -ForegroundColor Yellow
    Write-Host "Try running PowerShell as Administrator instead." -ForegroundColor Yellow
    exit 1
}
