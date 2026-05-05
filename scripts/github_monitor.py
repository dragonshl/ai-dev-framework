#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Repository Monitor - Automated Issue & Update Checker
Checks ai-dev-framework repository twice daily for new issues, PRs, and updates.
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Configuration
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    print("⚠️  Warning: GITHUB_TOKEN environment variable not set")
    print("   Please set it using: set GITHUB_TOKEN=your_token_here")
    print("   Or create a .env file with GITHUB_TOKEN=your_token_here")
    sys.exit(1)
REPO_OWNER = 'dragonshl'
REPO_NAME = 'ai-dev-framework'
GITHUB_API = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}'
REPORT_DIR = Path(__file__).parent / 'github-monitor-reports'

# Ensure report directory exists
REPORT_DIR.mkdir(exist_ok=True)


class GitHubMonitor:
    """Monitor GitHub repository for issues, PRs, and updates."""
    
    def __init__(self):
        self.headers = {
            'Authorization': f'token {GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.report_data = {
            'timestamp': datetime.now().isoformat(),
            'repository': f'{REPO_OWNER}/{REPO_NAME}',
            'checks_performed': [],
            'issues': [],
            'pull_requests': [],
            'recent_commits': [],
            'stargazers_count': 0,
            'forks_count': 0,
            'summary': ''
        }
    
    def fetch_issues(self, state='open'):
        """Fetch open or closed issues from repository."""
        print(f"📋 Fetching {state} issues...")
        url = f'{GITHUB_API}/issues'
        params = {'state': state, 'per_page': 50}
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            issues = response.json()
            
            # Filter out pull requests (GitHub API returns both in /issues)
            issues = [issue for issue in issues if 'pull_request' not in issue]
            
            self.report_data['issues'].extend([
                {
                    'number': issue['number'],
                    'title': issue['title'],
                    'state': issue['state'],
                    'created_at': issue['created_at'],
                    'updated_at': issue['updated_at'],
                    'author': issue['user']['login'] if issue['user'] else 'Unknown',
                    'labels': [label['name'] for label in issue.get('labels', [])],
                    'url': issue['html_url']
                }
                for issue in issues[:10]  # Limit to 10 most recent
            ])
            
            print(f"   ✅ Found {len(issues)} {state} issues")
            return issues
            
        except Exception as e:
            print(f"   ❌ Error fetching issues: {e}")
            return []
    
    def fetch_pull_requests(self, state='open'):
        """Fetch pull requests from repository."""
        print(f"🔀 Fetching {state} pull requests...")
        url = f'{GITHUB_API}/pulls'
        params = {'state': state, 'per_page': 50}
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            prs = response.json()
            
            self.report_data['pull_requests'].extend([
                {
                    'number': pr['number'],
                    'title': pr['title'],
                    'state': pr['state'],
                    'created_at': pr['created_at'],
                    'updated_at': pr['updated_at'],
                    'author': pr['user']['login'] if pr['user'] else 'Unknown',
                    'merged': pr.get('merged', False),
                    'url': pr['html_url']
                }
                for pr in prs[:10]  # Limit to 10 most recent
            ])
            
            print(f"   ✅ Found {len(prs)} {state} pull requests")
            return prs
            
        except Exception as e:
            print(f"   ❌ Error fetching pull requests: {e}")
            return []
    
    def fetch_recent_commits(self, days=7):
        """Fetch recent commits from repository."""
        print(f"📝 Fetching commits from last {days} days...")
        since_date = (datetime.now() - timedelta(days=days)).isoformat()
        url = f'{GITHUB_API}/commits'
        params = {'since': since_date, 'per_page': 20}
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            commits = response.json()
            
            self.report_data['recent_commits'].extend([
                {
                    'sha': commit['sha'][:8],
                    'message': commit['commit']['message'].split('\n')[0],
                    'author': commit['commit']['author']['name'],
                    'date': commit['commit']['author']['date'],
                    'url': commit['html_url']
                }
                for commit in commits[:10]  # Limit to 10 most recent
            ])
            
            print(f"   ✅ Found {len(commits)} commits in last {days} days")
            return commits
            
        except Exception as e:
            print(f"   ❌ Error fetching commits: {e}")
            return []
    
    def fetch_repository_stats(self):
        """Fetch repository statistics."""
        print("📊 Fetching repository statistics...")
        url = GITHUB_API
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            repo_data = response.json()
            
            self.report_data['stargazers_count'] = repo_data.get('stargazers_count', 0)
            self.report_data['forks_count'] = repo_data.get('forks_count', 0)
            self.report_data['open_issues_count'] = repo_data.get('open_issues_count', 0)
            self.report_data['watchers_count'] = repo_data.get('watchers_count', 0)
            
            print(f"   ✅ Stars: {repo_data.get('stargazers_count', 0)}")
            print(f"   ✅ Forks: {repo_data.get('forks_count', 0)}")
            print(f"   ✅ Open Issues: {repo_data.get('open_issues_count', 0)}")
            
            return repo_data
            
        except Exception as e:
            print(f"   ❌ Error fetching stats: {e}")
            return {}
    
    def generate_summary(self):
        """Generate a summary of the monitoring results."""
        issues = len(self.report_data['issues'])
        prs = len(self.report_data['pull_requests'])
        commits = len(self.report_data['recent_commits'])
        stars = self.report_data['stargazers_count']
        forks = self.report_data['forks_count']
        
        summary_lines = [
            f"GitHub Monitor Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "=" * 60,
            f"Repository: {REPO_OWNER}/{REPO_NAME}",
            "",
            "📈 Repository Statistics:",
            f"   • Stars: {stars}",
            f"   • Forks: {forks}",
            f"   • Open Issues: {self.report_data.get('open_issues_count', 0)}",
            "",
            "📋 Issues Summary:",
            f"   • Total issues checked: {issues}",
        ]
        
        if issues > 0:
            summary_lines.append("   Recent Issues:")
            for issue in self.report_data['issues'][:5]:
                summary_lines.append(f"     - #{issue['number']}: {issue['title']} (by {issue['author']})")
        
        summary_lines.extend([
            "",
            "🔀 Pull Requests Summary:",
            f"   • Total PRs checked: {prs}",
        ])
        
        if prs > 0:
            summary_lines.append("   Recent PRs:")
            for pr in self.report_data['pull_requests'][:5]:
                status = "MERGED" if pr['merged'] else "OPEN"
                summary_lines.append(f"     - #{pr['number']}: {pr['title']} [{status}]")
        
        summary_lines.extend([
            "",
            "📝 Recent Activity:",
            f"   • Commits in last 7 days: {commits}",
        ])
        
        if commits > 0:
            summary_lines.append("   Latest Commits:")
            for commit in self.report_data['recent_commits'][:5]:
                summary_lines.append(f"     - {commit['sha']}: {commit['message']}")
        
        summary_lines.extend([
            "",
            "=" * 60,
            "Report saved to: github-monitor-reports/",
        ])
        
        self.report_data['summary'] = '\n'.join(summary_lines)
        return self.report_data['summary']
    
    def save_report(self):
        """Save report to JSON and text files."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Save JSON report
        json_file = REPORT_DIR / f'report_{timestamp}.json'
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(self.report_data, f, indent=2, ensure_ascii=False)
        print(f"\n💾 JSON report saved: {json_file}")
        
        # Save text report
        txt_file = REPORT_DIR / f'report_{timestamp}.txt'
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(self.report_data['summary'])
        print(f"💾 Text report saved: {txt_file}")
        
        # Save latest report as "latest.json" for easy access
        latest_json = REPORT_DIR / 'latest.json'
        with open(latest_json, 'w', encoding='utf-8') as f:
            json.dump(self.report_data, f, indent=2, ensure_ascii=False)
        
        # Save latest report as "latest.txt" for easy access
        latest_txt = REPORT_DIR / 'latest.txt'
        with open(latest_txt, 'w', encoding='utf-8') as f:
            f.write(self.report_data['summary'])
        
        return json_file, txt_file
    
    def run_full_check(self):
        """Run complete monitoring check."""
        print("\n" + "="*60)
        print("🚀 Starting GitHub Repository Monitor")
        print("="*60 + "\n")
        
        # Perform all checks
        self.fetch_repository_stats()
        self.fetch_issues(state='open')
        self.fetch_pull_requests(state='open')
        self.fetch_recent_commits(days=7)
        
        # Generate and save report
        summary = self.generate_summary()
        json_file, txt_file = self.save_report()
        
        print("\n" + summary)
        print("\n✅ Monitoring complete!")
        
        return self.report_data


def main():
    """Main entry point."""
    monitor = GitHubMonitor()
    report = monitor.run_full_check()
    
    # Exit with appropriate code
    if report['issues']:
        print(f"\n⚠️  Alert: {len(report['issues'])} open issues found!")
        sys.exit(1)
    else:
        print("\n✨ All clear - no open issues!")
        sys.exit(0)


if __name__ == '__main__':
    main()
