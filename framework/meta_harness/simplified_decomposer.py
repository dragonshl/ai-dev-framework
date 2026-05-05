"""
Simplified Task Decomposer - LLM-based
简化任务分解器 - 基于LLM的智能分解
"""

import json
from typing import Dict, List
from datetime import datetime


class SimplifiedTaskDecomposer:
    """简化任务分解器 - 使用LLM直接分解需求"""
    
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
        # 当前使用简化的启发式方法作为示例
        
        tasks = self._heuristic_decomposition(requirements)
        
        # 为每个任务添加元数据
        for i, task in enumerate(tasks):
            task["id"] = f"{project_id}_task_{i+1}"
            task["priority"] = i + 1
            task["estimated_lines"] = min(task.get("estimated_lines", 80), self.max_task_lines)
            task["status"] = "pending"
            task["created_at"] = datetime.now().isoformat()
        
        return tasks
    
    def _heuristic_decomposition(self, requirements: str) -> List[Dict]:
        """基于启发式的简化分解（实际应使用LLM）"""
        
        tasks = []
        requirements_lower = requirements.lower()
        
        # 检测常见模块类型并创建对应任务
        module_patterns = [
            {
                "keywords": ["auth", "authentication", "login", "user"],
                "name": "User Authentication Module",
                "type": "auth",
                "description": "Implement user authentication with JWT tokens",
                "estimated_lines": 85
            },
            {
                "keywords": ["api", "endpoint", "rest", "route"],
                "name": "REST API Endpoints",
                "type": "api",
                "description": "Create RESTful API endpoints",
                "estimated_lines": 100
            },
            {
                "keywords": ["database", "db", "model", "schema"],
                "name": "Database Models & Migrations",
                "type": "database",
                "description": "Define database models and migrations",
                "estimated_lines": 90
            },
            {
                "keywords": ["frontend", "ui", "react", "vue", "component"],
                "name": "Frontend Components",
                "type": "frontend",
                "description": "Build frontend components",
                "estimated_lines": 100
            },
            {
                "keywords": ["test", "testing", "unit test", "integration"],
                "name": "Unit & Integration Tests",
                "type": "testing",
                "description": "Write comprehensive tests",
                "estimated_lines": 95
            }
        ]
        
        # 根据关键词匹配创建任务
        for pattern in module_patterns:
            if any(keyword in requirements_lower for keyword in pattern["keywords"]):
                tasks.append({
                    "name": pattern["name"],
                    "type": pattern["type"],
                    "description": pattern["description"],
                    "estimated_lines": pattern["estimated_lines"],
                    "dependencies": []
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
