# Simplified AI Development Framework

## 🎯 Overview

This is a **simplified 2-layer architecture** version of the Layered Intelligent Development Framework, optimized for faster development and easier maintenance.

### Architecture Comparison

| Aspect | Original (4-Layer) | Simplified (2-Layer) |
|--------|-------------------|---------------------|
| **Layers** | 4 layers | 2 layers |
| **Components** | 10+ components | 5 core components |
| **Workflow Steps** | 5 steps per task | 3 steps per task |
| **Agent Abstraction** | Separate AgentScope layer | Direct LLM integration |
| **Complexity** | High | Medium |
| **Lines of Code** | ~2,500+ | ~1,200 (estimated) |

## 🏗️ Simplified Architecture

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

## 📦 Components

### Layer 1: Orchestrator

1. **SimplifiedTaskDecomposer** (`framework/meta_harness/simplified_decomposer.py`)
   - Breaks requirements into atomic tasks
   - Heuristic-based decomposition (LLM integration ready)
   - Reduced from 105 lines to 110 lines with cleaner logic

2. **ExperienceDatabase** (`framework/meta_harness/experience_db.py`)
   - Stores historical patterns and lessons learned
   - Retrieves similar experiences for new tasks
   - Unchanged from original (fully functional)

3. **PerformanceMonitor** (`framework/meta_harness/performance_monitor.py`)
   - Tracks execution metrics
   - Provides optimization suggestions
   - Unchanged from original (fully functional)

4. **SimplifiedCEWorkflow** (`framework/compound_engineering/simplified_workflow.py`)
   - 3-step workflow: plan → execute → archive
   - Merged brainstorm into planning phase
   - Combined review and compounding into archive phase
   - Reduced from 235 lines to 162 lines

### Layer 2: LLM Executor

5. **SimplifiedCodeGenerationWorkflow** (`framework/workflows/simplified_graph.py`)
   - Direct LLM integration in LangGraph nodes
   - Merged Planner + Coder into `plan_and_generate` node
   - Merged Reviewer + Tester into `review_and_test` node
   - Reduced from 4 nodes to 3 nodes
   - Eliminated AgentScope abstraction layer

## 🚀 Quick Start

### Run Simplified Framework

```bash
# Install dependencies
pip install -r requirements.txt

# Run with example requirements using simplified orchestrator
python framework/simplified_orchestrator.py examples/requirements_auth_system.md
```

### Expected Output

```
============================================================
🚀 Starting Simplified AI Development Framework
📋 Project ID: proj_20260505_143022_a1b2c3
🏗️  Architecture: 2-Layer (Orchestrator + LLM Executor)
============================================================

📊 Phase 1: Task Decomposition
  ✓ Decomposed into 5 atomic tasks

🔄 Phase 2: Task Execution (3-step workflow)

  📝 Task 1/5: User Authentication Module
    ✓ Task completed successfully

  📝 Task 2/5: REST API Endpoints
    ✓ Task completed successfully

  ...

🚀 Phase 3: Optimization & Experience Compounding
  💡 Optimization suggestions:
    - Average execution time is 35s. Performance is good!

============================================================
✅ Development Complete!
⏱️  Total Time: 185.23 seconds
📂 Output: ./output/proj_20260505_143022_a1b2c3/
============================================================
```

## 📊 Workflow Comparison

### Original 5-Step Workflow
1. `/ce:brainstorm` - Explore approaches
2. `/ce:plan` - Detailed planning
3. `/ce:work` - Code generation (LangGraph + Agents)
4. `/ce:review` - Quality review
5. `/ce:compound` - Archive solution

### Simplified 3-Step Workflow
1. `/ce:plan` - Planning (includes brainstorming)
2. `/ce:execute` - Execution (LangGraph with direct LLM)
3. `/ce:archive` - Archiving (includes review + compounding)

**Benefits:**
- 40% fewer workflow steps
- Faster execution
- Simpler mental model
- Easier debugging

## 🔧 Key Simplifications

### 1. Merged Layers 2 & 3
**Before:** Separate AgentScope layer + LangGraph execution  
**After:** Direct LLM calls within LangGraph nodes

**Impact:**
- Eliminated 4 agent wrapper classes (~117 lines)
- Reduced coordination overhead
- Simpler error handling

### 2. Simplified Task Decomposition
**Before:** Rule-based engine with hardcoded patterns (105 lines)  
**After:** Cleaner heuristic approach with pattern matching (110 lines)

**Impact:**
- More maintainable code structure
- Easier to extend with LLM integration
- Better separation of concerns

### 3. Reduced CE Workflow Steps
**Before:** 5 distinct steps  
**After:** 3 consolidated steps

**Impact:**
- 40% reduction in workflow complexity
- Faster task completion
- Less state management overhead

### 4. Deferred Advanced Features
The following features remain available but are optional for MVP:
- Vector database integration (currently file-based)
- Advanced RAG retrieval
- Parallel task execution

These can be added incrementally after core functionality works reliably.

## 📁 File Structure

```
ai-dev-framework/
├── framework/
│   ├── simplified_orchestrator.py      # NEW: Simplified main controller
│   ├── orchestrator.py                 # Original (kept for reference)
│   ├── knowledge_base.py               # Original (optional)
│   ├── meta_harness/
│   │   ├── simplified_decomposer.py    # NEW: Simplified task decomposer
│   │   ├── task_decomposer.py          # Original (kept for reference)
│   │   ├── experience_db.py            # Unchanged
│   │   └── performance_monitor.py      # Unchanged
│   ├── compound_engineering/
│   │   ├── simplified_workflow.py      # NEW: 3-step workflow
│   │   └── workflow.py                 # Original (kept for reference)
│   ├── agents/                         # Original (not used in simplified)
│   │   ├── planner_agent.py
│   │   ├── coder_agent.py
│   │   ├── reviewer_agent.py
│   │   └── tester_agent.py
│   └── workflows/
│       ├── simplified_graph.py         # NEW: Direct LLM integration
│       └── code_generation_graph.py    # Original (kept for reference)
├── config/
├── docs/
├── examples/
├── output/
└── requirements.txt
```

## 🎯 When to Use Which Version

### Use Simplified Version When:
- ✅ Building MVP or prototype
- ✅ Need faster iteration cycles
- ✅ Team is small (<5 developers)
- ✅ Requirements are well-defined
- ✅ Want easier debugging and maintenance

### Use Original Version When:
- ✅ Production system with complex requirements
- ✅ Large team with specialized roles
- ✅ Need maximum flexibility and extensibility
- ✅ Require fine-grained control over each step
- ✅ Have resources to manage complexity

## 🔄 Migration Path

You can start with the simplified version and migrate to the full version later:

1. **Phase 1:** Start with simplified 2-layer architecture
2. **Phase 2:** Add vector database for better RAG
3. **Phase 3:** Introduce parallel task execution
4. **Phase 4:** Split into 4-layer architecture if needed

## 📈 Performance Improvements

| Metric | Original | Simplified | Improvement |
|--------|----------|------------|-------------|
| **Components** | 10+ | 5 | 50% reduction |
| **Workflow Steps** | 5 per task | 3 per task | 40% reduction |
| **Abstraction Layers** | 4 | 2 | 50% reduction |
| **Estimated Dev Time** | Baseline | -30% | Faster delivery |
| **Learning Curve** | Steep | Moderate | Easier onboarding |

## 🛠️ Future Enhancements

Both versions support these future enhancements:
- Full LLM integration (DashScope, OpenAI, etc.)
- ChromaDB vector search
- Parallel task execution
- Web-based UI
- CI/CD integration
- Multi-language support

## 📚 Related Documentation

- [Original README](README.md) - Full 4-layer architecture documentation
- [Quick Start Guide](QUICKSTART.md) - Fast-track setup instructions
- [Workflow Analysis Dashboard](workflow_analysis_dashboard.html) - Visual comparison

## 🤝 Contributing

Contributions welcome! Please focus on:
- Keeping the simplified version truly simple
- Maintaining clear separation between layers
- Adding LLM integration examples
- Improving documentation

---

**Built with ❤️ for rapid AI-driven development**

*Version: 1.1.0 (Simplified)*  
*Date: May 5, 2026*
