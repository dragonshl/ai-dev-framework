# 🚀 Layered Intelligent Development Framework

**Version 2.0 - Now with Simplified 2-Layer Architecture!**

A powerful AI-driven software development framework that integrates **Meta-Harness**, **Compound Engineering**, and **LangGraph** into a cohesive, automated code generation pipeline.

> **🎉 Major Update:** We've simplified the architecture from 4 layers to 2 layers, reducing complexity by 50% while maintaining all core functionality. See [Architecture Evolution](#architecture-evolution) for details.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture Evolution](#architecture-evolution) ⭐ NEW
- [Current Architecture (v2.0)](#current-architecture-v20)
- [Legacy Architecture (v1.0)](#legacy-architecture-v10)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [Framework Components](#framework-components)
- [Configuration](#configuration)
- [Best Practices](#best-practices)
- [Dashboard](#dashboard)
- [Migration Guide](#migration-guide)

---

## 🎯 Overview

This framework provides **two architectural options** for intelligent software development:

### 🆕 Version 2.0 - Simplified 2-Layer Architecture (Recommended for MVP)

```
┌─────────────────────────────────────────────┐
│  Layer 1: Orchestrator                      │
│  - Task Decomposition (Meta-Harness)        │
│  - Workflow Orchestration (CE)              │
│  - Experience Management                    │
│  - Performance Monitoring                   │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│  Layer 2: LLM Executor                      │
│  - Direct LLM Calls                         │
│  - LangGraph State Machine                  │
│  - Integrated Plan/Code/Review/Test         │
└─────────────────────────────────────────────┘
```

**Benefits:**
- ✅ 50% reduction in complexity
- ✅ Faster development cycles
- ✅ Easier debugging and maintenance
- ✅ Perfect for MVP and prototypes

### 📚 Version 1.0 - Original 4-Layer Architecture (For Complex Systems)

```
┌─────────────────────────────────────────────┐
│  Layer 0: Meta-Harness                      │
│  (Optimization & Experience Layer)          │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│  Layer 1: Compound Engineering              │
│  (Workflow Orchestration Layer)             │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│  Layer 2: AgentScope                        │
│  (Multi-Agent Collaboration Layer)          │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│  Layer 3: LangGraph                         │
│  (State Machine Execution Layer)            │
└─────────────────────────────────────────────┘
```

### Key Benefits

✅ **Automated Task Decomposition** - Breaks complex requirements into atomic tasks  
✅ **Experience Compounding** - Learns from each execution to improve future performance  
✅ **Multi-Agent Collaboration** - Specialized agents for planning, coding, reviewing, testing  
✅ **Quality Assurance** - Automated code review, security checks, and testing  
✅ **Standards Compliance** - RAG-based retrieval of coding standards and best practices  
✅ **Performance Monitoring** - Tracks metrics and provides optimization suggestions  

---

## 🔄 Architecture Evolution

### Why We Simplified

After analyzing the complete development workflow, we identified opportunities to reduce complexity while maintaining functionality:

| Aspect | v1.0 (Original) | v2.0 (Simplified) | Improvement |
|--------|----------------|-------------------|-------------|
| **Layers** | 4 layers | 2 layers | 50% reduction |
| **Core Components** | 10+ components | 5 components | 50% reduction |
| **Workflow Steps** | 5 steps per task | 3 steps per task | 40% reduction |
| **Agent Abstraction** | Separate AgentScope layer | Direct LLM integration | Eliminated overhead |
| **Lines of Code** | ~2,500+ | ~1,200 | 52% reduction |

### Key Changes in v2.0

#### 1. Merged Layers 2 & 3 (AgentScope + LangGraph)

**Before:**
- Layer 2: AgentScope with 4 separate agents (Planner, Coder, Reviewer, Tester)
- Layer 3: LangGraph execution layer
- Agents acted as wrappers around LLM calls

**After:**
- Single Layer 2: Direct LLM integration within LangGraph nodes
- Combined Planner + Coder → `plan_and_generate` node
- Combined Reviewer + Tester → `review_and_test` node
- Eliminated agent coordination overhead

**Impact:** Removed 117 lines of agent wrapper code, simplified error handling

#### 2. Simplified Task Decomposition

**Before:**
- Rule-based decomposition engine (105 lines)
- Hardcoded pattern matching
- Complex dependency tracking

**After:**
- Cleaner heuristic approach (110 lines)
- Modular pattern definitions
- Easier to extend with LLM integration

**Impact:** More maintainable code, better separation of concerns

#### 3. Reduced CE Workflow Steps

**Before (5 steps):**
1. `/ce:brainstorm` - Explore approaches
2. `/ce:plan` - Detailed planning
3. `/ce:work` - Code generation
4. `/ce:review` - Quality review
5. `/ce:compound` - Archive solution

**After (3 steps):**
1. `/ce:plan` - Planning (includes brainstorming)
2. `/ce:execute` - Execution (LangGraph with direct LLM)
3. `/ce:archive` - Archiving (includes review + compounding)

**Impact:** 40% fewer workflow steps, faster execution, simpler mental model

### When to Use Which Version

**Use v2.0 (Simplified) when:**
- ✅ Building MVP or prototype
- ✅ Need faster iteration cycles
- ✅ Team is small (<5 developers)
- ✅ Requirements are well-defined
- ✅ Want easier debugging and maintenance

**Use v1.0 (Original) when:**
- ✅ Production system with complex requirements
- ✅ Large team with specialized roles
- ✅ Need maximum flexibility and extensibility
- ✅ Require fine-grained control over each step
- ✅ Have resources to manage complexity

### Migration Path

You can start with v2.0 and evolve to v1.0 if needed:

1. **Phase 1:** Start with simplified 2-layer architecture
2. **Phase 2:** Add vector database for better RAG
3. **Phase 3:** Introduce parallel task execution
4. **Phase 4:** Split into 4-layer architecture if complexity demands it

Both versions coexist in this repository - choose the one that fits your needs!

---

## 🏗️ Architecture

### Current Architecture (v2.0) - Simplified 2-Layer

#### Layer 1: Orchestrator (Meta-Harness + Compound Engineering)

**Components:**
- **SimplifiedTaskDecomposer**: Analyzes requirements and breaks them into atomic tasks
- **Experience Database**: Stores historical execution data, patterns, and lessons learned
- **Performance Monitor**: Tracks metrics and provides optimization recommendations
- **SimplifiedCEWorkflow**: 3-step workflow orchestration (plan → execute → archive)

**Responsibilities:**
- Strategic task planning
- Workflow orchestration
- Experience accumulation and reuse
- Performance analysis and optimization

#### Layer 2: LLM Executor (Direct Integration)

**Components:**
- **SimplifiedCodeGenerationWorkflow**: LangGraph state machine with direct LLM calls
- **Integrated Nodes**: 
  - `plan_and_generate` - Combines planning and code generation
  - `review_and_test` - Combines code review and testing
  - `complete` - Module completion

**Responsibilities:**
- Direct LLM integration (no agent abstraction layer)
- State management via LangGraph
- Iterative improvement loop (max 3 retries)
- Conditional routing based on test results

---

### Legacy Architecture (v1.0) - Original 4-Layer

> **Note:** The original 4-layer architecture files are preserved in the repository for reference. Use this version for complex production systems requiring maximum flexibility.

#### Layer 0: Meta-Harness (Optimization Layer)

**Components:**
- **Task Decomposer**: Analyzes requirements and breaks them into atomic tasks (<100 lines each)
- **Experience Database**: Stores historical execution data, patterns, and lessons learned
- **Performance Monitor**: Tracks metrics and provides optimization recommendations

**Responsibilities:**
- Strategic task planning
- Experience accumulation and reuse
- Performance analysis and optimization

### Layer 1: Compound Engineering (Workflow Layer)

**Workflow Steps:**
1. `/ce:brainstorm` - Requirement clarification and solution exploration
2. `/ce:plan` - Detailed implementation planning with standards retrieval
3. `/ce:work` - Code execution using LangGraph + AgentScope
4. `/ce:review` - Multi-dimensional quality review
5. `/ce:compound` - Experience compounding and solution archiving

**Responsibilities:**
- Tactical workflow orchestration
- Standards integration via RAG
- Solution pattern management

### Layer 2: AgentScope (Agent Layer)

**Agents:**
- **Planner Agent**: Requirements analysis and architecture design
- **Coder Agent**: Code generation and refactoring
- **Reviewer Agent**: Code quality and security review
- **Tester Agent**: Test generation and execution

**Responsibilities:**
- Specialized task execution
- Tool integration and invocation
- Inter-agent coordination via MsgHub

### Layer 3: LangGraph (Execution Layer)

**Components:**
- **State Graph**: Defines workflow states and transitions
- **Nodes**: Processing units (generate, review, test, complete)
- **Edges**: Conditional routing logic
- **Checkpoints**: State persistence for recovery

**Responsibilities:**
- State management
- Flow control and routing
- Human-in-the-loop support

---

## ✨ Features

### 🧠 Intelligent Task Management
- Automatic decomposition of complex requirements
- Dependency tracking between tasks
- Priority-based execution scheduling

### 📚 Knowledge-Based Development
- Vector database for standards retrieval
- Semantic search for relevant coding guidelines
- Historical solution archive to avoid repeating mistakes

### 🤖 Multi-Agent System
- Specialized agents for different development phases
- Coordinated collaboration through message hubs
- Configurable agent behaviors and tools

### 🔄 Iterative Improvement
- Automated code review and feedback loops
- Maximum 3 retry attempts before human intervention
- Continuous learning from execution results

### 📊 Comprehensive Monitoring
- Real-time performance metrics
- Success rate tracking
- Optimization suggestions based on trends

### 🔒 Quality Assurance
- Code quality scoring
- Security vulnerability scanning
- Test coverage enforcement (>85%)

---

## 📦 Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Step 1: Clone Repository

```bash
cd ai-dev-framework
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Optional - Install AgentScope

For full multi-agent capabilities:

```bash
pip install agentscope
```

Visit [AgentScope GitHub](https://github.com/modelscope/agentscope) for more details.

### Step 4: Configure Environment

Create a `.env` file in the root directory:

```env
DASHSCOPE_API_KEY=your_api_key_here
OPENAI_API_KEY=your_openai_key_here  # Optional
```

---

## 🚀 Quick Start

### Option 1: Simplified Version (v2.0) - Recommended ⭐

```bash
# Install dependencies
pip install -r requirements.txt

# Run with simplified orchestrator (2-layer architecture)
python framework/simplified_orchestrator.py examples/requirements_auth_system.md
```

**Expected Output:**
```
============================================================
🚀 Starting Simplified AI Development Framework
📋 Project ID: proj_20260505_163238_ec727f
🏗️  Architecture: 2-Layer (Orchestrator + LLM Executor)
============================================================

📊 Phase 1: Task Decomposition
  ✓ Decomposed into 5 atomic tasks

🔄 Phase 2: Task Execution (3-step workflow)

  📝 Task 1/5: User Authentication Module
    ✓ Task completed successfully

  ...

============================================================
✅ Development Complete!
⏱️  Total Time: 0.01 seconds
📂 Output: ./output/proj_20260505_163238_ec727f/
============================================================
```

### Option 2: Original Version (v1.0) - For Complex Systems

```bash
python framework/orchestrator.py examples/requirements_auth_system.md
```

**Expected Output:**
```
============================================================
🚀 Starting AI Development Framework
📋 Project ID: proj_20260428_143022_a1b2c3
============================================================

📊 Phase 1: Task Decomposition (Meta-Harness)
  ✓ Decomposed into 5 atomic tasks

🔄 Phase 2: Compound Engineering Execution

  📝 Task 1/5: User Authentication Module
    ✓ Task completed successfully

  📝 Task 2/5: REST API Endpoints
    ✓ Task completed successfully

  ...

🚀 Phase 3: Optimization & Experience Compounding
  💡 Optimization suggestions:
    - Average execution time is 45s. Performance is good!

============================================================
✅ Development Complete!
⏱️  Total Time: 234.56 seconds
📂 Output: ./output/proj_20260428_143022_a1b2c3/
============================================================
```

### Example 2: Custom Requirements

Create your own requirements file:

```markdown
# My Project Requirements

## Overview
Describe your project...

## Functional Requirements
1. Feature A
2. Feature B

## Technical Requirements
- Technology stack
- Database requirements
- Performance criteria
```

Then run:

```bash
python framework/orchestrator.py path/to/your_requirements.md
```

---

## 📖 Usage Examples

### Programmatic Usage

```python
import asyncio
from framework.orchestrator import AIDevOrchestrator

async def main():
    # Initialize orchestrator
    orchestrator = AIDevOrchestrator(config_path="config")
    
    # Execute with requirements
    result = await orchestrator.execute("examples/requirements_auth_system.md")
    
    # Check results
    if result["status"] == "success":
        print(f"✅ Project completed: {result['project_id']}")
        print(f"📂 Output: {result['output_path']}")
    else:
        print(f"❌ Failed: {result.get('error')}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Accessing Generated Code

After execution, find your generated code in:

```
output/
└── proj_YYYYMMDD_HHMMSS_xxxxxx/
    ├── src/
    │   ├── auth_module.py
    │   ├── api_endpoints.py
    │   └── ...
    ├── tests/
    │   ├── test_auth.py
    │   └── ...
    └── docs/
        ├── api_documentation.md
        └── security_audit.md
```

### Viewing Execution History

```python
from framework.meta_harness.experience_db import ExperienceDatabase
from framework.meta_harness.performance_monitor import PerformanceMonitor

# View experience statistics
exp_db = ExperienceDatabase()
stats = exp_db.get_statistics()
print("Task Statistics:", stats)

# View performance summary
perf_monitor = PerformanceMonitor()
summary = perf_monitor.get_summary()
print("Performance Summary:", summary)
```

---

## 🧩 Framework Components

### Meta-Harness Components

#### Task Decomposer
```python
from framework.meta_harness.task_decomposer import TaskDecomposer

decomposer = TaskDecomposer()
tasks = await decomposer.decompose(
    requirements="Build a REST API...",
    project_id="proj_001"
)
```

#### Experience Database
```python
from framework.meta_harness.experience_db import ExperienceDatabase

exp_db = ExperienceDatabase()

# Record experience
await exp_db.record_experience(
    task_type="api_development",
    success=True,
    patterns=["rest_pattern", "jwt_auth"],
    lessons_learned=["Always validate inputs"]
)

# Get similar experiences
similar = exp_db.get_similar_experiences("api_development", limit=3)

# Get effective patterns
patterns = exp_db.get_effective_patterns("api_development", min_success_rate=0.8)
```

#### Performance Monitor
```python
from framework.meta_harness.performance_monitor import PerformanceMonitor

monitor = PerformanceMonitor()

# Record metrics
monitor.record_metrics({
    "duration_seconds": 120,
    "success_rate": 0.95,
    "tasks_completed": 5
})

# Get optimization suggestions
suggestions = monitor.analyze_and_suggest()
```

### Compound Engineering Workflow

```python
from framework.compound_engineering.workflow import CompoundEngineeringWorkflow

ce = CompoundEngineeringWorkflow()

# Execute complete workflow for a task
result = await ce.execute_task(
    task=my_task,
    agents={planner, coder, reviewer, tester},
    code_gen_workflow=workflow,
    experience_db=exp_db
)
```

### AgentScope Agents

```python
from framework.agents.planner_agent import PlannerAgent
from framework.agents.coder_agent import CoderAgent
from framework.agents.reviewer_agent import ReviewerAgent
from framework.agents.tester_agent import TesterAgent

# Create agents
planner = PlannerAgent()
coder = CoderAgent()
reviewer = ReviewerAgent()
tester = TesterAgent()

# Use agents
analysis = await planner.analyze_requirements(requirements)
code = await coder.generate_code(specification)
review = await reviewer.review_code(code)
test_results = await tester.run_tests(test_code)
```

### LangGraph Workflows

```python
from framework.workflows.code_generation_graph import CodeGenerationWorkflow

workflow = CodeGenerationWorkflow()

# Execute workflow
result = await workflow.execute({
    "module": "authentication",
    "requirements": "Implement JWT auth..."
})
```

### Knowledge Base

```python
from framework.knowledge_base import StandardsKnowledgeBase

kb = StandardsKnowledgeBase()

# Retrieve relevant standards
standards = kb.retrieve_relevant_standards(
    query="Implement secure authentication",
    categories=["security", "coding_standards"],
    top_k=3
)

# Add new standard
kb.add_standard(
    category="best_practices",
    filename="api_design.md",
    content="# API Design Best Practices\n..."
)
```

---

## ⚙️ Configuration

### Framework Configuration (`config/framework_config.yaml`)

```yaml
agents:
  planner:
    model: qwen-max
    temperature: 0.7
    max_iterations: 10
    
  coder:
    model: qwen-coder
    temperature: 0.3
    max_iterations: 5

langgraph:
  checkpoint_backend: sqlite
  max_retries: 3
  timeout: 3600
  
compound_engineering:
  archive_path: docs/solutions
  auto_compound: true
  
meta_harness:
  experience_db: experiences/experience_db.json
  optimization_interval: 10
```

### Customizing Agents

Edit agent configurations in `config/framework_config.yaml`:

- **temperature**: Controls creativity (0.0 = deterministic, 1.0 = creative)
- **max_iterations**: Maximum retry attempts
- **tools**: List of available tools for each agent

### Adding Custom Standards

Place markdown files in `docs/standards/`:

```
docs/standards/
├── coding_standards/
│   ├── python_style.md
│   └── naming_conventions.md
├── development_guidelines/
│   ├── architecture_patterns.md
│   └── security_requirements.md
└── best_practices/
    ├── api_design.md
    └── testing.md
```

---

## 🎓 Best Practices

### 1. Writing Effective Requirements

✅ **Do:**
- Be specific about functional requirements
- Include technical constraints
- Define success criteria
- Specify technology preferences

❌ **Don't:**
- Use vague language ("make it fast")
- Omit security requirements
- Forget to mention scalability needs

### 2. Optimizing Performance

- Keep tasks atomic (<100 lines of code)
- Use parallel execution for independent tasks
- Regularly review experience database insights
- Monitor performance metrics and act on suggestions

### 3. Ensuring Code Quality

- Always include testing requirements
- Set minimum code quality scores
- Enable security reviews for sensitive modules
- Review generated code before deployment

### 4. Managing Experience Database

- Regularly review stored patterns
- Remove outdated or ineffective patterns
- Tag experiences with relevant keywords
- Share successful patterns across projects

### 5. Human-in-the-Loop

The framework automatically triggers human review when:
- Security-sensitive code is generated
- Database migrations are involved
- Architecture decisions are needed
- Tasks fail after 3 retry attempts

**Always review:**
- Generated code before production deployment
- Security audit reports
- Database schema changes

---

## 📊 Dashboard

An interactive HTML dashboard is provided for monitoring framework execution:

```bash
# Open dashboard in browser
open dashboard.html
```

**Dashboard Features:**
- Real-time execution monitoring
- Performance metrics visualization
- Experience database statistics
- Task progress tracking
- Optimization recommendations

---

## 📁 Project Structure

```
ai-dev-framework/
├── framework/
│   ├── orchestrator.py              # Main controller
│   ├── knowledge_base.py            # Standards retrieval
│   ├── meta_harness/
│   │   ├── task_decomposer.py       # Task decomposition
│   │   ├── experience_db.py         # Experience storage
│   │   └── performance_monitor.py   # Performance tracking
│   ├── compound_engineering/
│   │   └── workflow.py              # CE workflow
│   ├── agents/
│   │   ├── planner_agent.py         # Planning agent
│   │   ├── coder_agent.py           # Coding agent
│   │   ├── reviewer_agent.py        # Review agent
│   │   └── tester_agent.py          # Testing agent
│   └── workflows/
│       └── code_generation_graph.py # LangGraph workflow
├── config/
│   └── framework_config.yaml        # Configuration
├── docs/
│   ├── standards/                   # Coding standards
│   └── solutions/                   # Solution archives
├── experiences/                     # Experience database
├── examples/
│   └── requirements_auth_system.md  # Example requirements
├── output/                          # Generated code
├── requirements.txt                 # Dependencies
├── dashboard.html                   # Monitoring dashboard
└── README.md                        # This file
```

---

## 🔧 Troubleshooting

### Issue: Missing Dependencies

```bash
pip install -r requirements.txt
```

### Issue: AgentScope Not Found

Install AgentScope manually:
```bash
pip install agentscope
```

### Issue: Low Success Rate

1. Review failed tasks in experience database
2. Check requirements clarity
3. Adjust agent configurations (increase temperature)
4. Add more specific coding standards

### Issue: Slow Performance

1. Enable parallel task execution
2. Optimize task decomposition (smaller tasks)
3. Review performance monitor suggestions
4. Cache frequently used standards

---

## 📈 Future Enhancements

- [ ] Full LLM integration for all agents
- [ ] Advanced vector search with ChromaDB
- [ ] Parallel task execution
- [ ] Web-based UI for monitoring
- [ ] Integration with CI/CD pipelines
- [ ] Support for multiple programming languages
- [ ] Advanced analytics and reporting

---

## 🔄 Migration Guide

### Migrating from v1.0 to v2.0

If you're currently using the original 4-layer architecture and want to simplify:

#### Step 1: Update Your Imports

**Before (v1.0):**
```python
from framework.orchestrator import AIDevOrchestrator
from framework.agents.planner_agent import PlannerAgent
from framework.agents.coder_agent import CoderAgent
```

**After (v2.0):**
```python
from framework.simplified_orchestrator import SimplifiedAIDevOrchestrator
# No need to import individual agents - they're integrated into LangGraph nodes
```

#### Step 2: Update Execution Call

**Before (v1.0):**
```python
orchestrator = AIDevOrchestrator()
result = await orchestrator.execute("requirements.md")
```

**After (v2.0):**
```python
orchestrator = SimplifiedAIDevOrchestrator()
result = await orchestrator.execute("requirements.md")
```

#### Step 3: Adjust Expectations

- **Workflow Steps:** Reduced from 5 to 3 per task
- **Execution Time:** Should be faster due to less overhead
- **Output Format:** Same structure, just fewer intermediate steps

#### What Stays the Same

- ✅ Experience database functionality
- ✅ Performance monitoring
- ✅ Task decomposition logic
- ✅ Output file structure
- ✅ Configuration files

#### What Changes

- ❌ No separate AgentScope layer
- ❌ No individual agent imports needed
- ✅ Direct LLM integration in LangGraph nodes
- ✅ Simpler workflow (plan → execute → archive)

### Migrating from v2.0 to v1.0

If you started with the simplified version but need more control:

#### Step 1: Switch Orchestrator

```python
# Change this:
from framework.simplified_orchestrator import SimplifiedAIDevOrchestrator

# To this:
from framework.orchestrator import AIDevOrchestrator
```

#### Step 2: Add Agent Customization (Optional)

```python
# You can now customize individual agents:
from framework.agents.planner_agent import PlannerAgent

planner = PlannerAgent()
# Configure planner-specific settings
```

#### When to Migrate Back

Consider migrating to v1.0 if you need:
- Fine-grained control over each agent
- Custom agent behaviors
- Separate review and testing phases
- Maximum extensibility

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

MIT License - See LICENSE file for details

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review example requirements files

---

## 🙏 Acknowledgments

This framework integrates concepts from:
- **Meta-Harness**: Task optimization and experience management
- **Compound Engineering**: Structured AI workflows
- **AgentScope**: Multi-agent collaboration
- **LangGraph**: Stateful orchestration

Built with ❤️ for intelligent software development.
