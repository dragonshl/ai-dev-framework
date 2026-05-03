# Quick Start Guide

Get started with the AI Dev Framework in 5 minutes!

## Prerequisites

- Python 3.9+
- pip

## Installation

```bash
# Navigate to framework directory
cd ai-dev-framework

# Install dependencies
pip install -r requirements.txt
```

## Your First Execution

### Option 1: Use Example Requirements

```bash
python framework/orchestrator.py examples/requirements_auth_system.md
```

### Option 2: Create Custom Requirements

1. Create a markdown file with your requirements:

```markdown
# My Project

## Overview
Brief description of what you want to build.

## Requirements
- Feature 1
- Feature 2
- Feature 3

## Technical Stack
- Language: Python
- Framework: FastAPI
- Database: PostgreSQL
```

2. Run the orchestrator:

```bash
python framework/orchestrator.py path/to/your_requirements.md
```

## Viewing Results

After execution completes:

1. **Check Output Directory:**
   ```bash
   ls output/proj_YYYYMMDD_HHMMSS_xxxxxx/
   ```

2. **Open Dashboard:**
   ```bash
   # On Windows
   start dashboard.html
   
   # On macOS
   open dashboard.html
   
   # On Linux
   xdg-open dashboard.html
   ```

## Understanding the Output

```
output/proj_YYYYMMDD_HHMMSS_xxxxxx/
├── src/              # Generated source code
├── tests/            # Generated test files
└── docs/             # Documentation and reports
```

## Next Steps

1. **Review Generated Code** - Always review before deployment
2. **Run Tests** - Execute generated test suites
3. **Customize Configuration** - Edit `config/framework_config.yaml`
4. **Add Standards** - Place coding standards in `docs/standards/`
5. **Monitor Performance** - Check dashboard for metrics

## Common Commands

```bash
# View experience statistics
python -c "from framework.meta_harness.experience_db import ExperienceDatabase; db = ExperienceDatabase(); print(db.get_statistics())"

# View performance summary
python -c "from framework.meta_harness.performance_monitor import PerformanceMonitor; m = PerformanceMonitor(); print(m.get_summary())"

# List available standards
ls docs/standards/
```

## Troubleshooting

**Issue:** Module not found errors
```bash
pip install -r requirements.txt
```

**Issue:** Slow execution
- Break requirements into smaller tasks
- Enable parallel processing (future feature)
- Review performance monitor suggestions

**Issue:** Low quality code
- Add more specific requirements
- Include coding standards in `docs/standards/`
- Adjust agent temperature in config

## Tips for Best Results

✅ Write detailed, specific requirements  
✅ Include technical constraints  
✅ Define success criteria  
✅ Specify technology preferences  
✅ Review and iterate on generated code  

## Need Help?

- Read the full [README.md](README.md)
- Check example requirements in `examples/`
- Review architecture documentation

Happy coding! 🚀
