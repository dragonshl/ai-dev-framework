"""
Meta-Harness Layer - Task Decomposer
任务分解器 - 将复杂需求分解为原子任务
"""

import json
from typing import Dict, List
from datetime import datetime


class TaskDecomposer:
    """任务分解器 - Meta-Harness核心组件"""
    
    def __init__(self):
        self.max_task_lines = 100  # 每个任务不超过100行代码
    
    async def decompose(self, requirements: str, project_id: str) -> List[Dict]:
        """
        将需求分解为原子任务
        
        Args:
            requirements: 需求文档内容
            project_id: 项目ID
            
        Returns:
            原子任务列表
        """
        # TODO: 集成LLM进行智能分解
        # 当前使用规则-based分解作为示例
        
        tasks = self._rule_based_decomposition(requirements)
        
        # 为每个任务添加元数据
        for i, task in enumerate(tasks):
            task["id"] = f"{project_id}_task_{i+1}"
            task["priority"] = i + 1
            task["estimated_lines"] = min(task.get("estimated_lines", 80), self.max_task_lines)
            task["status"] = "pending"
            task["created_at"] = datetime.now().isoformat()
        
        return tasks
    
    def _rule_based_decomposition(self, requirements: str) -> List[Dict]:
        """基于规则的简单分解（实际应使用LLM）"""
        
        tasks = []
        
        # 检测常见模块类型
        if "auth" in requirements.lower() or "authentication" in requirements.lower():
            tasks.append({
                "name": "User Authentication Module",
                "type": "auth",
                "description": "Implement user authentication with JWT tokens",
                "estimated_lines": 85,
                "dependencies": []
            })
        
        if "api" in requirements.lower() or "endpoint" in requirements.lower():
            tasks.append({
                "name": "REST API Endpoints",
                "type": "api",
                "description": "Create RESTful API endpoints",
                "estimated_lines": 120,
                "dependencies": ["auth"]
            })
        
        if "database" in requirements.lower() or "db" in requirements.lower():
            tasks.append({
                "name": "Database Models & Migrations",
                "type": "database",
                "description": "Define database models and migrations",
                "estimated_lines": 95,
                "dependencies": []
            })
        
        if "frontend" in requirements.lower() or "ui" in requirements.lower():
            tasks.append({
                "name": "Frontend Components",
                "type": "frontend",
                "description": "Build React/Vue frontend components",
                "estimated_lines": 150,
                "dependencies": ["api"]
            })
        
        if "test" in requirements.lower() or "testing" in requirements.lower():
            tasks.append({
                "name": "Unit & Integration Tests",
                "type": "testing",
                "description": "Write comprehensive tests",
                "estimated_lines": 100,
                "dependencies": ["api", "database"]
            })
        
        # 如果没有检测到特定模块，创建通用任务
        if not tasks:
            tasks.append({
                "name": "Core Implementation",
                "type": "general",
                "description": "Implement core functionality based on requirements",
                "estimated_lines": 100,
                "dependencies": []
            })
        
        return tasks
