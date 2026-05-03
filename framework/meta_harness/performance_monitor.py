"""
Meta-Harness Layer - Performance Monitor
性能监控器 - 跟踪和优化框架性能
"""

import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime


class PerformanceMonitor:
    """性能监控器 - 跟踪框架执行性能"""
    
    def __init__(self, metrics_path: str = "experiences/performance_metrics.json"):
        self.metrics_path = Path(metrics_path)
        self.metrics_history = self._load()
    
    def _load(self) -> List[Dict]:
        """加载历史指标"""
        if self.metrics_path.exists():
            with open(self.metrics_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    def _save(self):
        """保存指标"""
        self.metrics_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.metrics_path, 'w', encoding='utf-8') as f:
            json.dump(self.metrics_history, f, indent=2, ensure_ascii=False)
    
    def record_metrics(self, metrics: Dict):
        """
        记录性能指标
        
        Args:
            metrics: 性能指标字典
        """
        metrics["timestamp"] = datetime.now().isoformat()
        self.metrics_history.append(metrics)
        self._save()
    
    def analyze_and_suggest(self) -> List[str]:
        """
        分析性能并提供优化建议
        
        Returns:
            优化建议列表
        """
        suggestions = []
        
        if len(self.metrics_history) < 2:
            return suggestions
        
        # 计算平均执行时间
        durations = [m.get("duration_seconds", 0) for m in self.metrics_history]
        avg_duration = sum(durations) / len(durations)
        
        # 计算平均成功率
        success_rates = [m.get("success_rate", 0) for m in self.metrics_history]
        avg_success_rate = sum(success_rates) / len(success_rates)
        
        # 生成建议
        if avg_duration > 300:  # 超过5分钟
            suggestions.append(
                f"Average execution time is {avg_duration:.0f}s. "
                f"Consider optimizing task decomposition or parallelizing tasks."
            )
        
        if avg_success_rate < 0.8:
            suggestions.append(
                f"Success rate is {avg_success_rate*100:.1f}%. "
                f"Review failed tasks and improve error handling."
            )
        
        # 检测趋势
        if len(self.metrics_history) >= 5:
            recent = self.metrics_history[-3:]
            older = self.metrics_history[:-3]
            
            recent_avg = sum(m.get("duration_seconds", 0) for m in recent) / len(recent)
            older_avg = sum(m.get("duration_seconds", 0) for m in older) / len(older)
            
            if recent_avg > older_avg * 1.2:
                suggestions.append(
                    "Execution time is increasing. Check for bottlenecks in recent changes."
                )
        
        return suggestions
    
    def get_summary(self) -> Dict:
        """获取性能摘要"""
        if not self.metrics_history:
            return {
                "total_executions": 0,
                "avg_duration": 0,
                "avg_success_rate": 0
            }
        
        durations = [m.get("duration_seconds", 0) for m in self.metrics_history]
        success_rates = [m.get("success_rate", 0) for m in self.metrics_history]
        
        return {
            "total_executions": len(self.metrics_history),
            "avg_duration": sum(durations) / len(durations),
            "avg_success_rate": sum(success_rates) / len(success_rates),
            "min_duration": min(durations),
            "max_duration": max(durations)
        }
