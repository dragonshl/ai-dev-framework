# GitHub Repository Monitor

Automated monitoring system that checks the AI Dev Framework repository twice daily for issues, pull requests, and updates.

## 📋 Features

- ✅ **Twice Daily Checks**: Runs at 12:00 PM (noon) and 12:00 AM (midnight)
- ✅ **Issue Tracking**: Monitors open and closed issues
- ✅ **Pull Request Monitoring**: Tracks PR status and merges
- ✅ **Commit History**: Reviews recent commits (last 7 days)
- ✅ **Repository Statistics**: Stars, forks, watchers count
- ✅ **Automated Reports**: Generates JSON and text reports
- ✅ **Alert System**: Exit codes indicate if issues need attention

## 🚀 Installation

### Step 1: Install Scheduled Tasks

Open PowerShell as **Administrator** and run:

```powershell
cd C:\Users\songhl\dashboard\ai-dev-framework\scripts
.\install_scheduled_task.ps1
```

This will create two Windows Scheduled Tasks:
- `GitHub-Monitor-Noon` - Runs daily at 12:00 PM
- `GitHub-Monitor-Midnight` - Runs daily at 12:00 AM

### Step 2: Verify Installation

```powershell
schtasks /query | findstr GitHub
```

You should see both tasks listed with "Ready" status.

## 📊 Usage

### Manual Run

To run the monitor manually:

```bash
cd C:\Users\songhl\dashboard\ai-dev-framework\scripts
python github_monitor.py
```

Or use the batch file:

```bash
run_github_monitor.bat
```

### View Latest Report

Reports are saved to `github-monitor-reports/` directory:

- `latest.json` - Most recent report in JSON format
- `latest.txt` - Most recent report in readable text format
- `report_YYYYMMDD_HHMMSS.json` - Historical reports
- `report_YYYYMMDD_HHMMSS.txt` - Historical reports

### View Report in Terminal

```bash
type github-monitor-reports\latest.txt
```

## 🔧 Configuration

### Environment Variables

The monitor uses these environment variables (optional):

- `GITHUB_TOKEN` - GitHub Personal Access Token (defaults to embedded token)

To use a different token:

```bash
set GITHUB_TOKEN=your_new_token_here
python github_monitor.py
```

### Modify Schedule

To change the schedule times:

1. Remove existing tasks:
   ```powershell
   .\uninstall_scheduled_task.ps1
   ```

2. Edit `install_scheduled_task.ps1` and modify the `/st` parameter:
   - `/st 12:00` - Change noon time
   - `/st 00:00` - Change midnight time

3. Reinstall:
   ```powershell
   .\install_scheduled_task.ps1
   ```

## 📈 Report Contents

Each report includes:

1. **Repository Statistics**
   - Star count
   - Fork count
   - Open issues count
   - Watcher count

2. **Issues Summary**
   - Issue number and title
   - Author
   - Labels
   - Creation/update dates
   - Direct links

3. **Pull Requests Summary**
   - PR number and title
   - Author
   - Merge status
   - Creation/update dates
   - Direct links

4. **Recent Commits**
   - Commit SHA (short)
   - Commit message
   - Author
   - Date
   - Direct links

5. **Summary Text**
   - Human-readable overview
   - Key metrics
   - Recent activity highlights

## 🛠️ Management Commands

### View Scheduled Tasks

```powershell
schtasks /query | findstr GitHub
```

### View Task Details

```powershell
schtasks /query /tn "GitHub-Monitor-Noon" /v /fo list
schtasks /query /tn "GitHub-Monitor-Midnight" /v /fo list
```

### Run Task Manually

```powershell
schtasks /run /tn "GitHub-Monitor-Noon"
schtasks /run /tn "GitHub-Monitor-Midnight"
```

### Disable Task (without deleting)

```powershell
schtasks /change /tn "GitHub-Monitor-Noon" /disable
schtasks /change /tn "GitHub-Monitor-Midnight" /disable
```

### Enable Task

```powershell
schtasks /change /tn "GitHub-Monitor-Noon" /enable
schtasks /change /tn "GitHub-Monitor-Midnight" /enable
```

### Uninstall Tasks

```powershell
.\uninstall_scheduled_task.ps1
```

## 🔍 Troubleshooting

### Task Not Running

1. Check task status:
   ```powershell
   schtasks /query /tn "GitHub-Monitor-Noon" /v /fo list
   ```

2. Check last run result:
   - Look for "Last Result" field
   - `0` = Success
   - `1` = Issues found (expected behavior)
   - Other codes = Error

3. Check Windows Event Viewer:
   - Open Event Viewer
   - Navigate to: Application and Services Logs → Microsoft → Windows → TaskScheduler → Operational

### Python Not Found

Ensure Python is in your PATH:

```powershell
where python
```

If not found, update the batch file to use full Python path:

```batch
C:\Python39\python.exe github_monitor.py
```

### Permission Denied

Run PowerShell as Administrator when installing/uninstalling tasks.

### Network Errors

The monitor requires internet access. Check:
- Firewall settings
- Proxy configuration
- GitHub API status: https://www.githubstatus.com/

## 📝 Example Output

```
============================================================
🚀 Starting GitHub Repository Monitor
============================================================

📊 Fetching repository statistics...
   ✅ Stars: 42
   ✅ Forks: 8
   ✅ Open Issues: 3

📋 Fetching open issues...
   ✅ Found 3 open issues

🔀 Fetching open pull requests...
   ✅ Found 1 open pull requests

📝 Fetching commits from last 7 days...
   ✅ Found 5 commits in last 7 days

💾 JSON report saved: github-monitor-reports/report_20260428_120000.json
💾 Text report saved: github-monitor-reports/report_20260428_120000.txt

GitHub Monitor Report - 2026-04-28 12:00:00
============================================================
Repository: dragonshl/ai-dev-framework

📈 Repository Statistics:
   • Stars: 42
   • Forks: 8
   • Open Issues: 3

📋 Issues Summary:
   • Total issues checked: 3
   Recent Issues:
     - #1: Feature request: Add TypeScript support (by user123)
     - #2: Bug: CI pipeline failing on Python 3.11 (by contributor)
     - #3: Documentation update needed (by maintainer)

🔀 Pull Requests Summary:
   • Total PRs checked: 1
   Recent PRs:
     - #4: Add new agent module [OPEN]

📝 Recent Activity:
   • Commits in last 7 days: 5
   Latest Commits:
     - a424ce6: Add GitHub workflows, issue templates
     - 6a64062: Initial commit: Layered Intelligent Development Framework

============================================================
Report saved to: github-monitor-reports/

✅ Monitoring complete!

⚠️  Alert: 3 open issues found!
```

## 🎯 Best Practices

1. **Check Reports Daily**: Review `latest.txt` each morning
2. **Respond to Issues Promptly**: Address new issues within 24 hours
3. **Monitor Trends**: Track star/fork growth over time
4. **Archive Old Reports**: Move old reports to archive folder monthly
5. **Update Token**: Rotate GitHub token every 90 days for security

## 🔐 Security Notes

- The script uses a GitHub Personal Access Token
- Store tokens securely (consider using Windows Credential Manager)
- Rotate tokens regularly
- Never commit tokens to version control
- Use minimum required scopes for the token (repo scope is sufficient)

## 📞 Support

For issues or questions:
- Check the report files in `github-monitor-reports/`
- Review Windows Task Scheduler logs
- Verify network connectivity to GitHub API
- Ensure Python and required packages are installed

## 📄 License

Part of the AI Dev Framework project - MIT License
