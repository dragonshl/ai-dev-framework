# Contributing to AI Dev Framework

Thank you for your interest in contributing to the Layered Intelligent Development Framework! This document provides guidelines and information for contributors.

## 🎯 Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)
- [Documentation](#documentation)

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/ai-dev-framework.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Commit and push your changes
6. Submit a pull request

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected vs actual behavior**
- **Screenshots** if applicable
- **Environment details** (OS, Python version, etc.)
- **Additional context** that might help

**Example:**
```markdown
**Bug**: Task decomposer fails with large requirements files

**Steps to Reproduce:**
1. Create a requirements file with 1000+ lines
2. Run: python framework/orchestrator.py large_requirements.md
3. See error: MemoryError in task_decomposer.py

**Expected:** Should handle large files gracefully
**Actual:** Crashes with MemoryError

**Environment:**
- OS: Ubuntu 22.04
- Python: 3.9.16
- Version: v1.0.0
```

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- **Use case**: Why is this needed?
- **Proposed solution**: How should it work?
- **Alternatives considered**: Other approaches you've thought about
- **Impact**: Who will benefit from this?

### Pull Requests

1. **Update documentation** if you're changing functionality
2. **Add tests** for new features
3. **Ensure all tests pass** before submitting
4. **Follow coding standards** (see below)
5. **Update CHANGELOG.md** if applicable

## Development Setup

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Git

### Installation

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ai-dev-framework.git
cd ai-dev-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest pytest-cov black flake8 mypy
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=framework --cov-report=html

# Run specific test file
pytest tests/test_orchestrator.py
```

## Coding Standards

### Python Style Guide

We follow [PEP 8](https://peps.python.org/pep-0008/) with these specifics:

- **Line length**: 127 characters maximum
- **Indentation**: 4 spaces (no tabs)
- **Imports**: Grouped and sorted
  ```python
  # Standard library
  import os
  import sys
  
  # Third-party
  import numpy as np
  
  # Local application
  from framework.orchestrator import AIDevOrchestrator
  ```

- **Type hints**: Required for all functions
  ```python
  def process_task(task_id: str, config: dict) -> bool:
      """Process a single task.
      
      Args:
          task_id: Unique identifier for the task
          config: Configuration dictionary
      
      Returns:
          True if successful, False otherwise
      """
      pass
  ```

### Naming Conventions

- **Variables/functions**: snake_case
- **Classes**: PascalCase
- **Constants**: UPPER_CASE
- **Private methods**: _leading_underscore

### Code Quality Tools

```bash
# Format code with black
black framework/

# Check style with flake8
flake8 framework/

# Type checking with mypy
mypy framework/
```

## Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, semicolons, etc)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```bash
feat(orchestrator): add parallel task execution support

fix(agent-scope): resolve memory leak in PlannerAgent

docs(readme): update installation instructions

refactor(meta-harness): simplify experience database queries

test(workflow): add integration tests for CE workflow
```

## Pull Request Process

1. **Create PR from your fork** to the main repository
2. **Fill out the PR template** completely
3. **Link related issues** using keywords (closes #123, fixes #456)
4. **Request reviews** from maintainers
5. **Address review comments** promptly
6. **Keep PR focused** - one feature/fix per PR
7. **Update your branch** if master has changed:
   ```bash
   git fetch upstream
   git rebase upstream/master
   ```

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Code is commented where necessary
- [ ] Documentation updated
- [ ] Tests added and passing
- [ ] No merge conflicts
- [ ] Commit messages are clear

## Testing

### Writing Tests

```python
import pytest
from framework.meta_harness.task_decomposer import TaskDecomposer

class TestTaskDecomposer:
    def test_decompose_simple_requirement(self):
        """Test decomposition of simple requirement."""
        decomposer = TaskDecomposer()
        tasks = decomposer.decompose("Create a hello world API")
        
        assert len(tasks) > 0
        assert all(isinstance(t, dict) for t in tasks)
    
    @pytest.mark.asyncio
    async def test_decompose_complex_requirement(self):
        """Test decomposition with complex requirements."""
        # Test implementation
        pass
```

### Test Coverage

- Aim for **>85% code coverage**
- Test both success and failure paths
- Include edge cases
- Mock external dependencies

## Documentation

### Code Comments

- Use docstrings for all public functions/classes
- Explain **why**, not just **what**
- Include examples for complex logic

```python
def calculate_priority(task: dict, urgency: float) -> float:
    """Calculate task priority based on multiple factors.
    
    Uses weighted scoring algorithm considering:
    - Task complexity (40%)
    - Deadline proximity (35%)
    - Resource availability (25%)
    
    Args:
        task: Task dictionary with complexity score
        urgency: Urgency factor (0.0 to 1.0)
    
    Returns:
        Priority score (0.0 to 10.0, higher = more urgent)
    
    Example:
        >>> calculate_priority({"complexity": 0.8}, 0.9)
        7.2
    """
    pass
```

### README Updates

When adding features, update:
- Feature list in README.md
- Usage examples
- Configuration options
- API documentation

## 🏷️ Issue Labels

Understanding labels helps you find issues to work on:

- `bug`: Something isn't working
- `enhancement`: New feature or improvement
- `documentation`: Documentation improvements
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention needed
- `high priority`: Needs immediate attention
- `question`: Further information requested

## 💬 Getting Help

- **Questions?** Open a discussion or ask in issues
- **Stuck?** Tag maintainers in your PR
- **Community?** Join our Discord/Slack (link coming soon)

## 🎖️ Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Special mentions for significant contributions

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to AI Dev Framework! 🚀
