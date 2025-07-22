# Claude Code Best Practices - [PROJECT_NAME]

## 📋 How to Customize This Template
1. Replace all placeholders in square brackets [LIKE THIS] with project-specific values
2. Remove any sections that don't apply to your project
3. Add project-specific sections as needed
4. Update examples to match your technology stack
5. Customize naming conventions to match your organization's standards

### Common Placeholders:
- `[PROJECT_NAME]`: Your project's official name
- `[project-name]`: Lowercase, hyphenated version for directories
- `[FEATURE]`: Feature or module abbreviation (e.g., USER, AUTH, CALC)
- `[database]`: Your database technology (e.g., bigquery, postgres, mongo)
- `[primary_identifier]`: Your main entity ID field (e.g., user_id, sku, order_id)

## 🎯 Project Overview
**Project**: [PROJECT_NAME]  
**Description**: [Brief description of project purpose and main functionality]  
**Technology Stack**: [List main technologies]  
**Deployment Platform**: [Cloud provider/platform]  
**Database/Storage**: [Database technology]  

## 📁 Project Structure (MANDATORY)
```
[project-name]/
├── src/                              ← Production code ONLY
│   ├── controllers/                  ← Main orchestration logic
│   │   └── [feature]_controller.py
│   ├── pipelines/                    ← Data processing pipelines
│   │   └── [process]_pipeline.py
│   ├── calculators/                  ← Deterministic calculations
│   │   └── calculate_[metric].py
│   ├── triggers/                     ← Entry point programs
│   │   └── trigger_[process].py
│   ├── utils/                        ← Reusable utilities
│   │   ├── log_writer.py
│   │   ├── [database]_helpers.py
│   │   └── id_generator.py
│   └── models/                       ← ML models (if applicable)
├── tests/                            ← All test files
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── experiments/                      ← Research & temporary code
│   ├── sandbox/                      ← Quick tests, throwaway code
│   ├── YYYY-MM-DD-[description]/     ← Dated research folders
│   └── archive/                      ← Old experiments
├── config/                           ← Configuration files
│   ├── settings.yaml
│   ├── [environment].yaml
│   └── credentials/
├── docs/                             ← Documentation
│   ├── technical/
│   ├── claude/                       ← Claude-specific docs
│   └── [project-docs]/
├── scripts/                          ← One-off utility scripts & runners
│   ├── [utility]_script.py
│   └── run_[process].py
├── data/                             ← Data files (if applicable)
│   ├── inputs/
│   ├── outputs/
│   └── cache/
├── deployment/                       ← Deployment configuration
│   ├── Dockerfile
│   ├── requirements.txt
│   └── [deployment-config].yaml
└── .gitignore
```

## 🚨 CRITICAL RULES for Claude Code

### ❌ NEVER Do These Things:
- Don't create files in src/ during experimentation
- Don't use generic names like: temp.py, test.py, debug.py, new_version.py
- Don't duplicate existing production files (e.g., don't create [file]_v2.py)
- Don't modify production code when experimenting - copy to experiments/ first
- Don't create files in the root directory unless it's configuration
- Don't mix production code with utility scripts

### ✅ ALWAYS Do These Things:
- Ask which directory before creating new files if uncertain
- Use descriptive, dated names for experiments
- Put test files in tests/ directory with test_ prefix
- Use experiments/sandbox/ for quick throwaway code
- Follow the import structure when updating code
- Keep production code in src/, utilities in scripts/

## 📝 File Naming Conventions

### Production Code (src/):
- `[feature]_controller.py` ✅
- `calculate_[metric].py` ✅
- `[process]_pipeline.py` ✅

### Test Code (tests/):
- `test_[feature].py` ✅
- `test_[module]_integration.py` ✅
- `test_[function_name].py` ✅

### Experimental Code (experiments/):
- `experiments/2025-01-21-[feature]-optimization/[descriptive_name].py` ✅
- `experiments/sandbox/quick_[test_name].py` ✅
- `research_[topic].py` ✅

### Scripts (scripts/):
- `run_[process].py` ✅ (runner scripts)
- `check_[status].py` ✅ (monitoring scripts)
- `cleanup_[target].py` ✅ (maintenance scripts)

## 🔄 Workflow Guidelines

### Starting New Features:
**USER**: "I want to implement [new feature description]"  
**CLAUDE**: Creates files in experiments/YYYY-MM-DD-[feature-name]/  
           Does NOT modify src/[module]/[existing-file].py

### Making Production Changes:
**USER**: "The experiment worked, update production code"  
**CLAUDE**: Updates src/[module]/[file].py  
           Archives experiment files to experiments/archive/  
           Updates any affected imports

### Quick Testing:
**USER**: "I need to quickly test this [feature] edge case"  
**CLAUDE**: Creates file in experiments/sandbox/  
           Uses descriptive name like test_[feature]_edge_cases.py

## 📦 Import Structure

### Standard Import Pattern:
```python
# Standard library imports (alphabetically)
import json
import os
from datetime import datetime
from pathlib import Path

# Third-party imports (alphabetically)
import pandas as pd
from google.cloud import [service]

# Internal imports - use full paths from src/
from src.utils.log_writer import LogWriter
from src.calculators.[module] import [function]
from src.controllers.[module] import [class]
```

### In Test Files:
```python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.calculators.[module] import [function]
```

## 🗃️ Database & Logging Standards

### Table Naming Convention:
- `[prefix]_[entity]_[purpose]` for main tables
- `sim_[feature]_[action]_log` for simulation logs  
- `proc_[feature]_[status]` for process tracking
- `tmp_[purpose]` for temporary tables
- `arch_[table]_[date]` for archived tables

### ID Generation Pattern:
```python
# Use consistent ID formats
process_run_id = f"PROC-[FEATURE]-{identifier}-{date}-v{version}"
batch_id = f"BATCH-[FEATURE]-{identifier}-{date}"
run_id = f"RUN-[FEATURE]-{identifier}-{timestamp}"
```

### Required Logging Fields:
```python
required_fields = {
    '[primary_identifier]': 'STRING',     # Main entity ID
    'process_name': 'STRING', 
    'process_run_id': 'STRING',
    'timestamp': 'TIMESTAMP',
    'status': 'STRING',
    'feature_vector': 'STRING',           # JSON of inputs
    'input_hash': 'STRING',               # For reproducibility
    'error_message': 'STRING',            # For debugging
}
```

## 🧪 Testing Guidelines

### Unit Tests:
- Test individual functions
- Use mock data from tests/fixtures/
- Name: `test_[function_name].py`
- Coverage target: [80%+]

### Integration Tests:
- Test full workflows
- Use test database/environment
- Name: `test_[workflow]_integration.py`

### Test Structure:
```python
def test_[function]_[scenario]():
    """Test [function] handles [scenario] correctly."""
    # Arrange
    test_data = load_fixture('test_data.json')
    
    # Act
    result = function_under_test(test_data)
    
    # Assert
    assert result['status'] == 'expected_value'
```

## 🚀 Deployment Guidelines

### Environment Requirements:
- All production code must work in containerized environment
- Use environment variables for configuration
- Handle authentication via service accounts/credentials
- Include proper error handling and logging

### Development Workflow:
1. **Local Development**: Test on local machine first
2. **Experiment Phase**: Use experiments/ directory
3. **Code Review**: Ensure follows standards
4. **Production Update**: Move to src/ when stable
5. **Testing**: Run full test suite
6. **Deployment**: [Project-specific deployment command]

## 📋 Code Quality Standards

### Error Handling:
```python
try:
    result = risky_operation()
    logger.log_success(f"Operation completed: {result}")
    return result
except SpecificError as e:
    logger.log_error(f"Expected error: {str(e)}")
    # Handle gracefully
except Exception as e:
    logger.log_error(f"Unexpected error in [function]: {str(e)}")
    raise
```

### Function Documentation:
```python
def process_data(identifier: str, config: dict) -> dict:
    """
    Process data for the given identifier.
    
    Args:
        identifier: Unique identifier for the entity
        config: Configuration dictionary with processing parameters
        
    Returns:
        dict: Processed results with keys:
            - status: 'success' or 'failure'
            - data: Processed data
            - metadata: Processing metadata
        
    Raises:
        ValueError: If identifier is invalid
        ProcessingError: If processing fails
    """
```

### Code Style:
- Use type hints for function parameters and returns
- Include comprehensive docstrings
- Follow [PEP 8] style guide
- Maximum line length: 100 characters
- Use meaningful variable names

## 🧹 Maintenance Guidelines

### Regular Cleanup:
```bash
# Archive old experiments (monthly)
python scripts/archive_old_experiments.py

# Clean temporary files
python scripts/cleanup_temp_files.py
```

### Review Schedule:
- **Weekly**: Review experiments/ folder
- **Monthly**: Archive completed experiments
- **Quarterly**: Update documentation
- **Before Major Releases**: Full code audit

## 🔍 Decision Tree for File Placement

Ask yourself:

1. **"Is this production code or experimental?"**
   - Production → src/
   - Experimental → experiments/

2. **"How long will this code be needed?"**
   - Permanent → src/
   - Research → experiments/YYYY-MM-DD-[topic]/
   - Quick test → experiments/sandbox/

3. **"Is this a reusable component or one-off script?"**
   - Reusable → src/utils/
   - One-off → scripts/

4. **"Does this test a specific function or full workflow?"**
   - Function → tests/unit/
   - Workflow → tests/integration/

## 🔧 Optional Sections (Include as Needed)

### API Standards
[Include if project has APIs]

### Frontend Guidelines
[Include for full-stack projects]

### Data Pipeline Standards
[Include for data-heavy projects]

### Security Guidelines
[Include security-specific requirements]

### Performance Standards
[Include performance benchmarks and requirements]

## 📞 When in Doubt

**ALWAYS ASK**: "Which directory should I put this file in?" before creating it.  
**FOLLOW THE STRUCTURE**: Never create files outside the defined structure.  
**KEEP IT CLEAN**: Mention when experimental files should be cleaned up.

---

**Last Updated**: [YYYY-MM-DD]  
**Project**: [PROJECT_NAME]  
**Repository**: [repository-url]  
**Maintained By**: [team/person]
