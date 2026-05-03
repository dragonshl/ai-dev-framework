"""
Meta-Harness Layer - Experience Database
经验数据库 - 存储和检索开发经验
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class ExperienceDatabase:
    """经验数据库 - 记录任务执行经验和最佳实践"""
    
    def __init__(self, db_path: str = "experiences/experience_db.json"):
        self.db_path = Path(db_path)
        self.data = self._load()
    
    def _load(self) -> Dict:
        """加载经验数据库"""
        if self.db_path.exists():
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "experiences": [],
            "patterns": {},
            "statistics": {}
        }
    
    def _save(self):
        """保存经验数据库"""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
    
    async def record_experience(
        self,
        task_type: str,
        success: bool,
        patterns: List[str] = None,
        lessons_learned: List[str] = None,
        metrics: Dict = None
    ):
        """
        记录任务执行经验
        
        Args:
            task_type: 任务类型
            success: 是否成功
            patterns: 使用的代码模式
            lessons_learned: 学到的经验教训
            metrics: 性能指标
        """
        experience = {
            "timestamp": datetime.now().isoformat(),
            "task_type": task_type,
            "success": success,
            "patterns": patterns or [],
            "lessons_learned": lessons_learned or [],
            "metrics": metrics or {}
        }
        
        self.data["experiences"].append(experience)
        
        # 更新模式统计
        if patterns:
            for pattern in patterns:
                if pattern not in self.data["patterns"]:
                    self.data["patterns"][pattern] = {
                        "usage_count": 0,
                        "success_rate": 0.0,
                        "total_attempts": 0,
                        "successful_attempts": 0
                    }
                
                self.data["patterns"][pattern]["usage_count"] += 1
                self.data["patterns"][pattern]["total_attempts"] += 1
                if success:
                    self.data["patterns"][pattern]["successful_attempts"] += 1
                
                # 更新成功率
                total = self.data["patterns"][pattern]["total_attempts"]
                successful = self.data["patterns"][pattern]["successful_attempts"]
                self.data["patterns"][pattern]["success_rate"] = successful / total if total > 0 else 0.0
        
        # 更新统计信息
        if task_type not in self.data["statistics"]:
            self.data["statistics"][task_type] = {
                "total_tasks": 0,
                "successful_tasks": 0,
                "avg_success_rate": 0.0
            }
        
        self.data["statistics"][task_type]["total_tasks"] += 1
        if success:
            self.data["statistics"][task_type]["successful_tasks"] += 1
        
        total = self.data["statistics"][task_type]["total_tasks"]
        successful = self.data["statistics"][task_type]["successful_tasks"]
        self.data["statistics"][task_type]["avg_success_rate"] = successful / total if total > 0 else 0.0
        
        self._save()
    
    def get_similar_experiences(self, task_type: str, limit: int = 5) -> List[Dict]:
        """
        获取相似任务的历史经验
        
        Args:
            task_type: 任务类型
            limit: 返回数量限制
            
        Returns:
            历史经验列表
        """
        similar = [
            exp for exp in self.data["experiences"]
            if exp["task_type"] == task_type
        ]
        
        # 按时间倒序排列
        similar.sort(key=lambda x: x["timestamp"], reverse=True)
        
        return similar[:limit]
    
    def get_effective_patterns(self, task_type: str, min_success_rate: float = 0.7) -> List[Dict]:
        """
        获取高效代码模式
        
        Args:
            task_type: 任务类型
            min_success_rate: 最低成功率阈值
            
        Returns:
            高效模式列表
        """
        effective = []
        
        for pattern_name, stats in self.data["patterns"].items():
            if stats["success_rate"] >= min_success_rate and stats["usage_count"] >= 2:
                effective.append({
                    "pattern": pattern_name,
                    "success_rate": stats["success_rate"],
                    "usage_count": stats["usage_count"]
                })
        
        # 按成功率降序排列
        effective.sort(key=lambda x: x["success_rate"], reverse=True)
        
        return effective
    
    def get_statistics(self) -> Dict:
        """获取整体统计信息"""
        return self.data["statistics"]
