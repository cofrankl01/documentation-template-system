#!/usr/bin/env python3
"""
Enhanced setup script for Claude documentation
Generates project-specific best practices and validates setup
"""

import os
import json
from datetime import datetime
from pathlib import Path

def get_essential_info():
    """Collect only the essential project information"""
    
    print("🚀 Claude Documentation Quick Setup")
    print("=" * 50)
    print("Just answer a few quick questions...\n")
    
    info = {}
    
    # Essential questions only
    info['PROJECT_NAME'] = input("Project name: ")
    
    # Project type selection
    print("\nSelect project type:")
    print("1. Data Pipeline / ETL")
    print("2. Web Application")
    print("3. Machine Learning")
    print("4. API Service")
    print("5. Other")
    
    project_types = {
        '1': 'data-pipeline',
        '2': 'web-application', 
        '3': 'ml-model',
        '4': 'api-service',
        '5': 'other'
    }
    
    type_choice = input("Select (1-5): ")
    info['PROJECT_TYPE'] = project_types.get(type_choice, 'other')
    info['ALGORITHM_TYPE'] = input("What type of system/algorithm? (e.g., keyword-analysis, pricing, inventory): ")
    info['CURRENT_TASK_DESCRIPTION'] = input("What are you working on first? ")
    
    # Auto-generate from essentials
    info['project-name'] = info['PROJECT_NAME'].lower().replace(' ', '-')
    info['ALGORITHM_NAME'] = info['ALGORITHM_TYPE'].replace('-', ' ').title()
    info['START_DATE'] = datetime.now().strftime('%Y-%m-%d')
    info['SPRINT_DATES'] = f"{datetime.now().strftime('%B %d')} - {(datetime.now().replace(day=28)).strftime('%B %d, %Y')}"
    
    # Smart defaults
    info['PRIMARY_IDS'] = "TBD - will identify during development"
    info['CURRENT_FILE'] = f"scripts/main_{info['ALGORITHM_TYPE'].replace('-', '_')}.py"
    info['OUTPUT_LOCATION'] = "TBD - will determine based on requirements"
    info['TEST_IDENTIFIER'] = "TBD - will set up test cases"
    info['TEAM_NAME'] = "Development Team"
    
    # BigQuery defaults (can be updated later)
    algo_prefix = ''.join([word[0] for word in info['ALGORITHM_TYPE'].split('-')])[:3]
    info['TABLE_PREFIX'] = algo_prefix
    info['OUTPUT_DATASET'] = "TBD_Dataset"
    info['OUTPUT_TABLE'] = f"{info['OUTPUT_DATASET']}.{algo_prefix}_output"
    
    # Documentation paths
    info['MAIN_ALGORITHM_DOC'] = f"Algorithm Details: `reference/{info['ALGORITHM_TYPE']}-guide.md`"
    info['ALGORITHM_FILE'] = f"{info['ALGORITHM_TYPE']}-guide.md"
    info['IMPLEMENTATION_GUIDE'] = f"reference/{info['ALGORITHM_TYPE']}-implementation.md"
    
    # Examples based on algorithm type
    info['PRODUCTION_EXAMPLE'] = f"process_{info['ALGORITHM_TYPE'].replace('-', '_')}.py"
    info['SCRIPT_EXAMPLE'] = f"run_{info['ALGORITHM_TYPE'].replace('-', '_')}.py"
    info['TEST_EXAMPLE'] = info['ALGORITHM_TYPE'].replace('-', '_')
    info['EXPERIMENT_EXAMPLE'] = f"{info['ALGORITHM_TYPE']}-optimization"
    info['FUNCTION_EXAMPLE'] = f"process_{info['ALGORITHM_TYPE'].replace('-', '_')}"
    info['PRIMARY_ID'] = "identifier"
    info['ID_DESCRIPTION'] = "Primary identifier"
    info['MAIN_SCRIPT_PATH'] = info['CURRENT_FILE']
    
    # Current focus
    info['CURRENT_FOCUS_DESCRIPTION'] = info['CURRENT_TASK_DESCRIPTION']
    
    # Sprint placeholders - these get updated as work progresses
    info['CHANGE_1'] = "Set up initial project structure"
    info['CHANGE_2'] = "Create core processing logic"
    info['CHANGE_3'] = "Add documentation"
    info['NEXT_STEP_1'] = "Define data requirements"
    info['NEXT_STEP_2'] = "Implement initial version"
    info['NEXT_STEP_3'] = "Test with sample data"
    info['DATE_1'] = datetime.now().strftime('%Y-%m-%d')
    info['DECISION_1'] = "Chose implementation approach"
    info['DATE_2'] = "TBD"
    info['DECISION_2'] = "TBD"
    info['PREVIOUS_SPRINT'] = "initial-setup.md"
    
    return info

def show_summary(info):
    """Show what will be created"""
    print("\n📋 Setup Summary:")
    print(f"   Project: {info['PROJECT_NAME']}")
    print(f"   Type: {info['PROJECT_TYPE']}")
    print(f"   Algorithm: {info['ALGORITHM_TYPE']}")
    print(f"   Focus: {info['CURRENT_TASK_DESCRIPTION']}")
    print("\n✅ Everything else will use smart defaults that can be updated later.")
    
    response = input("\nProceed with setup? (y/n): ")
    return response.lower() == 'y'

def process_template(template_path, output_path, replacements):
    """Process a template file with replacements"""
    
    with open(template_path, 'r') as f:
        content = f.read()
    
    # Replace all placeholders
    for key, value in replacements.items():
        placeholder = f"{{{{{key}}}}}"
        content = content.replace(placeholder, value)
    
    # Ensure directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write processed file
    with open(output_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Created: {output_path}")

def validate_no_placeholders(file_path):
    """Check for remaining placeholders"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    if '{{' in content or '[[' in content:
        print(f"⚠️  Warning: {file_path} may contain unprocessed placeholders")
        return False
    return True

def create_verify_structure_script():
    """Create the structure verification script"""
    script_content = '''#!/usr/bin/env python3
"""
Verify project structure follows best practices
"""

import os
import sys

def verify_project_structure():
    """Verify project follows the documented structure"""
    
    issues = []
    
    # Check required directories exist
    required_dirs = ['src/', 'scripts/', 'experiments/', 'tests/', 'docs/claude/']
    for dir_name in required_dirs:
        if not os.path.exists(dir_name):
            issues.append(f"Missing required directory: {dir_name}")
    
    # Check for misplaced production code
    if os.path.exists('scripts/'):
        for file in os.listdir('scripts/'):
            if file.endswith('.py'):
                # Check for production code patterns
                if 'controller' in file or 'pipeline' in file or 'system' in file:
                    issues.append(f"Possible production code in scripts/: {file}")
    
    # Check for files in root that shouldn't be there
    root_files = os.listdir('.')
    for file in root_files:
        if file.endswith('.py') and file not in ['setup.py', 'setup_claude_docs.py']:
            issues.append(f"Python file in root directory: {file}")
    
    # Check imports are working
    sys.path.insert(0, os.path.dirname(__file__))
    
    # Report results
    if issues:
        print("❌ Structure Issues Found:")
        for issue in issues:
            print(f"   - {issue}")
        return False
    else:
        print("✅ Project structure looks good!")
        return True

if __name__ == "__main__":
    verify_project_structure()
'''
    
    script_path = Path('scripts/verify_structure.py')
    script_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    # Make executable on Unix-like systems
    try:
        os.chmod(script_path, 0o755)
    except:
        pass
    
    return script_path

def setup_claude_docs():
    """Main setup function"""
    
    # Get essential info only
    project_info = get_essential_info()
    
    # Confirm before proceeding
    if not show_summary(project_info):
        print("Setup cancelled.")
        return
    
    print("\n📁 Setting up documentation structure...")
    
    # Define template mappings
    templates = [
        ('templates/ALWAYS_LOAD.template.md', 'docs/claude/ALWAYS_LOAD.md'),
        ('templates/current-sprint.template.md', 'docs/claude/current-sprint.md'),
        ('templates/session-handoff.template.md', 'docs/claude/session-handoff.md'),
        ('templates/README.template.md', 'docs/claude/README.md'),
        ('templates/bestpractices.template.md', f'docs/{project_info["project-name"]}-bestpractices.md'),
        ('templates/quick-reference.template.md', 'docs/claude/bestpractices/quick-reference.md'),
    ]
    
    # Process each template
    processed_files = []
    for template_file, output_file in templates:
        template_path = Path(template_file)
        output_path = Path(output_file)
        
        if template_path.exists():
            process_template(template_path, output_path, project_info)
            processed_files.append(output_path)
        else:
            print(f"⚠️  Template not found: {template_path}")
    
    # Create empty directories
    directories = [
        'src/controllers',
        'src/pipelines',
        'src/utils',
        'scripts/',
        'tests/unit',
        'tests/integration',
        'experiments/sandbox',
        'docs/claude/reference',
        'docs/claude/completed',
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {directory}")
    
    # Save configuration for future reference
    config_path = Path('docs/claude/.config.json')
    with open(config_path, 'w') as f:
        json.dump(project_info, f, indent=2)
    print(f"✅ Saved configuration: {config_path}")
    
    # Create verification script
    verify_script = create_verify_structure_script()
    print(f"✅ Created verification script: {verify_script}")
    
    # Validate processed files
    print("\n🔍 Validating setup...")
    all_valid = True
    for file_path in processed_files:
        if not validate_no_placeholders(file_path):
            all_valid = False
    
    if all_valid:
        print("✅ All files processed successfully!")
    
    # Create startup instructions
    startup_file = Path('docs/claude/STARTUP_INSTRUCTIONS.md')
    with open(startup_file, 'w') as f:
        f.write(f"""# Claude Session Startup Instructions

Always start your Claude sessions with this prompt:

```
Please read:
1. docs/claude/ALWAYS_LOAD.md
2. docs/{project_info['project-name']}-bestpractices.md
3. docs/claude/current-sprint.md
```

This ensures Claude has all the necessary context for your project.
""")
    
    print(f"✅ Created startup instructions: {startup_file}")
    
    print("\n" + "=" * 50)
    print("✅ Claude documentation setup complete!")
    print("\n📋 Next steps:")
    print(f"1. Review and customize: docs/{project_info['project-name']}-bestpractices.md")
    print("2. Run verification: python scripts/verify_structure.py")
    print("3. Start your Claude session with the prompt in STARTUP_INSTRUCTIONS.md")
    print("4. Remember to commit with: ./git-pushlog origin main")
    
    # Final health check
    print("\n🔍 Template Health Check:")
    print("✓ Project-specific best practices created")
    print("✓ Directory structure created")
    print("✓ Verification script added")
    print("\n⚠️  Remember to:")
    print("- Review and customize the best practices document")
    print("- Remove any sections that don't apply to your project")
    print("- Add project-specific guidelines as needed")

if __name__ == "__main__":
    setup_claude_docs()
