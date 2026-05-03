"""
分层智能开发框架 - 主控制器
Layered Intelligent Development Framework - Main Orchestrator

整合四层架构：
- Layer 0: Meta-Harness (优化与经验沉淀层)
- Layer 1: Compound Engineering (工作流编排层)
- Layer 2: AgentScope (多智能体协作层)
- Layer 3: LangGraph (状态机执行层)
"""

import asyncio
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Import framework components
from framework.meta_harness.task_decomposer import TaskDecomposer
from framework.meta_harness.experience_db import ExperienceDatabase
from framework.meta_harness.performance_monitor import PerformanceMonitor
from framework.compound_engineering.workflow import CompoundEngineeringWorkflow
from framework.agents.planner_agent import PlannerAgent
from framework.agents.coder_agent import CoderAgent
from framework.agents.reviewer_agent import ReviewerAgent
from framework.agents.tester_agent import TesterAgent
from framework.workflows.code_generation_graph import CodeGenerationWorkflow


class AIDevOrchestrator:
    """AI开发框架总控制器"""
    
    def __init__(self, config_path: str = "config"):
        """
        初始化 orchestrator
        
        Args:
            config_path: 配置文件路径
        """
        self.project_id = None
        self.config_path = Path(config_path)
        
        # Initialize Meta-Harness components
        self.task_decomposer = TaskDecomposer()
        self.experience_db = ExperienceDatabase()
        self.performance_monitor = PerformanceMonitor()
        
        # Initialize AgentScope agents
        self.planner = PlannerAgent()
        self.coder = CoderAgent()
        self.reviewer = ReviewerAgent()
        self.tester = TesterAgent()
        
        # Initialize workflows
        self.ce_workflow = CompoundEngineeringWorkflow()
        self.code_gen_workflow = CodeGenerationWorkflow()
        
        print("✅ AI Dev Framework initialized successfully")
    
    async def execute(self, requirements_path: str) -> Dict:
        """
        主执行入口
        
        Args:
            requirements_path: 需求文档路径
            
        Returns:
            执行结果字典
        """
        self.project_id = f"proj_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"
        start_time = datetime.now()
        
        print(f"\n{'='*60}")
        print(f"🚀 Starting AI Development Framework")
        print(f"📋 Project ID: {self.project_id}")
        print(f"{'='*60}\n")
        
        try:
            # ===== Phase 1: Meta-Harness Task Decomposition =====
            print("📊 Phase 1: Task Decomposition (Meta-Harness)")
            atomic_tasks = await self._phase1_decompose(requirements_path)
            print(f"  ✓ Decomposed into {len(atomic_tasks)} atomic tasks\n")
            
            # ===== Phase 2: Compound Engineering Workflow =====
            print("🔄 Phase 2: Compound Engineering Execution")
            execution_results = await self._phase2_execute_tasks(atomic_tasks)
            print(f"  ✓ Completed {len(execution_results)} tasks\n")
            
            # ===== Phase 3: Meta-Harness Optimization =====
            print("🚀 Phase 3: Optimization & Experience Compounding")
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            metrics = {
                "project_id": self.project_id,
                "duration_seconds": duration,
                "tasks_completed": len(execution_results),
                "success_rate": self._calculate_success_rate(execution_results)
            }
            
            await self._phase3_optimize(metrics, execution_results)
            
            print(f"\n{'='*60}")
            print(f"✅ Development Complete!")
            print(f"⏱️  Total Time: {duration:.2f} seconds")
            print(f"📂 Output: ./output/{self.project_id}/")
            print(f"{'='*60}\n")
            
            return {
                "project_id": self.project_id,
                "status": "success",
                "metrics": metrics,
                "output_path": f"./output/{self.project_id}"
            }
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            return {
                "project_id": self.project_id,
                "status": "failed",
                "error": str(e)
            }
    
    async def _phase1_decompose(self, requirements_path: str) -> List[Dict]:
        """Phase 1: 任务分解"""
        # Load requirements
        with open(requirements_path, 'r', encoding='utf-8') as f:
            requirements = f.read()
        
        # Decompose into atomic tasks
        tasks = await self.task_decomposer.decompose(
            requirements=requirements,
            project_id=self.project_id
        )
        
        return tasks
    
    async def _phase2_execute_tasks(self, tasks: List[Dict]) -> List[Dict]:
        """Phase 2: 执行所有任务"""
        results = []
        
        for i, task in enumerate(tasks, 1):
            print(f"\n  📝 Task {i}/{len(tasks)}: {task['name']}")
            
            try:
                # Execute Compound Engineering workflow for this task
                result = await self.ce_workflow.execute_task(
                    task=task,
                    agents={
                        "planner": self.planner,
                        "coder": self.coder,
                        "reviewer": self.reviewer,
                        "tester": self.tester
                    },
                    code_gen_workflow=self.code_gen_workflow,
                    experience_db=self.experience_db
                )
                
                results.append(result)
                print(f"    ✓ Task completed successfully")
                
            except Exception as e:
                print(f"    ✗ Task failed: {str(e)}")
                results.append({
                    "task": task,
                    "status": "failed",
                    "error": str(e)
                })
        
        return results
    
    async def _phase3_optimize(self, metrics: Dict, results: List[Dict]):
        """Phase 3: 优化和经验沉淀"""
        # Record performance metrics
        self.performance_monitor.record_metrics(metrics)
        
        # Update experience database
        for result in results:
            if result.get("status") == "success":
                await self.experience_db.record_experience(
                    task_type=result["task"].get("type", "general"),
                    success=True,
                    patterns=result.get("patterns_used", []),
                    lessons_learned=result.get("lessons", [])
                )
        
        # Generate optimization suggestions
        suggestions = self.performance_monitor.analyze_and_suggest()
        if suggestions:
            print(f"  💡 Optimization suggestions:")
            for suggestion in suggestions:
                print(f"    - {suggestion}")
    
    def _calculate_success_rate(self, results: List[Dict]) -> float:
        """计算成功率"""
        if not results:
            return 0.0
        
        successful = sum(1 for r in results if r.get("status") == "success")
        return successful / len(results)


async def main():
    """Main entry point"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python orchestrator.py <requirements.md>")
        sys.exit(1)
    
    requirements_path = sys.argv[1]
    
    orchestrator = AIDevOrchestrator()
    result = await orchestrator.execute(requirements_path)
    
    print("\nFinal Result:")
    print(f"  Status: {result['status']}")
    if result['status'] == 'success':
        print(f"  Project ID: {result['project_id']}")
        print(f"  Output: {result['output_path']}")


if __name__ == "__main__":
    asyncio.run(main())
