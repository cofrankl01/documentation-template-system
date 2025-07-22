# {{PROJECT_NAME}} - Quick Reference

## 🚨 Critical Rules
1. **Git commits**: ALWAYS use `./git-pushlog origin main`
2. **File locations**: Follow structure, ask only if uncertain
3. **Experiments**: Date-stamp folders (YYYY-MM-DD-topic)

## 📁 Directory Structure
```
{{PROJECT_NAME}}/
├── src/                    # Production ONLY
├── scripts/               # Utilities
├── experiments/           # Research & testing
│   └── YYYY-MM-DD-topic/
├── tests/                 # Test files (test_*.py)
└── docs/                  # Documentation
```

## 📝 Naming Conventions
- Production: `{{PRODUCTION_EXAMPLE}}`
- Scripts: `{{SCRIPT_EXAMPLE}}`
- Tests: `test_{{TEST_EXAMPLE}}`
- Experiments: `2025-MM-DD-{{EXPERIMENT_EXAMPLE}}/`

## 💻 Code Standards
```python
def {{FUNCTION_EXAMPLE}}({{PRIMARY_ID}}: str, process_run_id: str) -> dict:
    """Docstring required
    
    Args:
        {{PRIMARY_ID}}: {{ID_DESCRIPTION}}
        process_run_id: For traceability
    
    Returns:
        dict: Structured results
    """
    # Type hints required
    # Include error handling
```

## 🗄️ BigQuery Tables
- `{{TABLE_PREFIX}}_lifecycle_*` - Lifecycle tracking
- `{{TABLE_PREFIX}}_sim_*` - Simulation logs
- `{{TABLE_PREFIX}}_dec_*` - Decision logs
- `{{OUTPUT_DATASET}}.*` - Output tables

## 📊 Current Project
- **Algorithm**: {{ALGORITHM_NAME}}
- **Main script**: `{{MAIN_SCRIPT_PATH}}`
- **Output**: `{{OUTPUT_TABLE}}`

## 🔗 Full Documentation
Need more detail? Load:
- Project best practices: `/docs/{{PROJECT_NAME}}-bestpractices.md`
- Full template: `/docs/bestpractices-general-template.md`
