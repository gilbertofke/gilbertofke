import os
import re
from datetime import datetime, timedelta
from github import Github

def get_weekly_stats():
    """Get weekly statistics from GitHub API"""
    token = os.getenv('GITHUB_TOKEN')
    g = Github(token)
    user = g.get_user('gilbertofke')
    
    # Get date range for the past week
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    # Count contributions
    contributions = 0
    for repo in user.get_repos():
        commits = repo.get_commits(since=start_date, until=end_date)
        contributions += commits.totalCount
    
    # Count active AI projects
    ai_projects = 0
    for repo in user.get_repos():
        if repo.description and any(keyword in repo.description.lower() for keyword in ['ai', 'ml', 'machine learning', 'artificial intelligence']):
            if repo.updated_at > start_date:
                ai_projects += 1
    
    # Estimate coding time (this is a simplified estimation)
    coding_hours = contributions * 1.5  # Rough estimate: 1.5 hours per contribution
    
    return {
        'coding_hours': min(coding_hours, 60),  # Cap at 60 hours
        'ai_projects': ai_projects,
        'contributions': contributions
    }

def update_readme(stats):
    """Update the README.md with new statistics"""
    with open('README.md', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update metrics
    content = re.sub(
        r'!\[Coding Time\]\(https://img\.shields\.io/badge/Weekly_Coding-\d+_hrs-66C4A7\)',
        f'![Coding Time](https://img.shields.io/badge/Weekly_Coding-{stats["coding_hours"]}_hrs-66C4A7)',
        content
    )
    content = re.sub(
        r'!\[AI Projects\]\(https://img\.shields\.io/badge/Active_AI_Projects-\d+-9C27B0\)',
        f'![AI Projects](https://img.shields.io/badge/Active_AI_Projects-{stats["ai_projects"]}-9C27B0)',
        content
    )
    content = re.sub(
        r'!\[Contributions\]\(https://img\.shields\.io/badge/Weekly_Contributions-\d+-66C4A7\)',
        f'![Contributions](https://img.shields.io/badge/Weekly_Contributions-{stats["contributions"]}-66C4A7)',
        content
    )
    
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == '__main__':
    stats = get_weekly_stats()
    update_readme(stats) 