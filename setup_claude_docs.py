#!/usr/bin/env python3
"""
Interactive setup script for Claude documentation
Customizes templates for your specific project
"""

import os
import json
import shutil
from datetime import datetime
from pathlib import Path

def get_project_info():
    """Collect project-specific information from user"""
    
    print("🚀 Claude Documentation Setup")
    print("=" * 50)
    print("This will customize the documentation templates for your project.\n")
    
    info = {}
    
    # Basic project info
    info['PROJECT_NAME'] = input("Project name: ")
    info['ALGORITHM_TYPE'] = input("Algorithm/system type (e.g., keyword-classification, pricing-optimization): ")
    info['ALGORITHM_NAME'] = input("Algorithm display name (e.g., Keyword Classification V2): ")
    info['PRIMARY_IDS'] = input("Primary identifiers (e.g., BSS-12345-678, SKU-ABC): ")
    info['START_DATE'] = datetime.now().strftime('%Y-%m-%d')
    
    # Sprint info
    info['SPRINT_DATES'] = input("Current sprint dates (e.g., July 16-30, 2025): ")
    info['CURRENT_TASK_DESCRIPTION'] = input("What are you currently working on? ")
    
    # File paths
    info['CURRENT_FILE'] = input("Main file you're working on (e.g., scripts/process_data.py): ")
    info['OUTPUT_LOCATION'] = input("Where does output go? (e.g., BigQuery table name): ")
    info['TEST_IDENTIFIER'] = input("Test case identifier (e.g., BSS-92588-723): ")
    
    # Documentation
    info['MAIN_ALGORITHM_DOC'] = f"Algorithm Details: `reference/{info['ALGORITHM_TYPE']}-guide.md`"
    info['ALGORITHM_FILE'] = f"{info['ALGORITHM_TYPE']}-guide.md"
    info['IMPLEMENTATION_GUIDE'] = f"reference/{info['ALGORITHM_TYPE']}-implementation.md"
    
    # Team info
    info['TEAM_NAME'] = input("Team name (optional, press Enter to skip): ") or "Development Team"
    
    # BigQuery specifics
    print("\n📊 BigQuery Configuration")
    info['TABLE_PREFIX'] = input("Table prefix (e.g., pp, kwr): ")
    info['OUTPUT_DATASET'] = input("Output dataset (e.g., OF_Dataset): ")
    info['OUTPUT_TABLE'] = f"{info['OUTPUT_DATASET']}.{info['TABLE_PREFIX']}_{info['ALGORITHM_TYPE'].replace('-', '_')}"
    
    # Examples for templates
    info['PRODUCTION_EXAMPLE'] = f"calculate_{info['ALGORITHM_TYPE'].replace('-', '_')}.py"
    info['SCRIPT_EXAMPLE'] = f"run_{info['ALGORITHM_TYPE'].replace('-', '_')}.py"
    info['TEST_EXAMPLE'] = info['ALGORITHM_TYPE'].replace('-', '_')
    info['EXPERIMENT_EXAMPLE'] = f"{info['ALGORITHM_TYPE']}-improvement"
    info['FUNCTION_EXAMPLE'] = f"process_{info['ALGORITHM_TYPE'].replace('-', '_')}"
    info['PRIMARY_ID'] = info['PRIMARY_IDS'].split('-')[0].lower() if '-' in info['PRIMARY_IDS'] else 'identifier'
    info['ID_DESCRIPTION'] = f"{info['PRIMARY_ID'].upper()} identifier"
    info['MAIN_SCRIPT_PATH'] = info['CURRENT_FILE']
    
    # Current focus
    info['CURRENT_FOCUS_DESCRIPTION'] = info['CURRENT_TASK_DESCRIPTION']
    
    # Sprint placeholders
    info['CHANGE_1'] = "Update data processing logic"
    info['CHANGE_2'] = "Add validation checks"
    info['CHANGE_3'] = "Update documentation"
    info['NEXT_STEP_1'] = "Complete implementation"
    info['NEXT_STEP_2'] = "Run tests"
    info['NEXT_STEP_3'] = "Deploy to production"
    info['DATE_1'] = datetime.now().strftime('%Y-%m-%d')
    info['DECISION_1'] = "Decided on implementation approach"
    info['DATE_2'] = "TBD"
    info['DECISION_2'] = "TBD"
    info['PREVIOUS_SPRINT'] = f"{datetime.now().strftime('%Y-%m')}-sprint1.md"
    
    return info

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

def setup_claude_docs():
    """Main setup function"""
    
    # Get project info
    project_info = get_project_info()
    
    print("\n📁 Setting up documentation structure...")
    
    # Define template mappings
    templates = [
        ('claude/ALWAYS_LOAD.template.md', 'docs/claude/ALWAYS_LOAD.md'),
        ('claude/current-sprint.template.md', 'docs/claude/current-sprint.md'),
        ('claude/session-handoff.template.md', 'docs/claude/session-handoff.md'),
        ('claude/README.template.md', 'docs/claude/README.md'),
        ('claude/bestpractices/quick-reference.template.md', 'docs/claude/bestpractices/quick-reference.md'),
    ]
    
    # Process each template
    for template_file, output_file in templates:
        template_path = Path(template_file)
        output_path = Path(output_file)
        
        if template_path.exists():
            process_template(template_path, output_path, project_info)
        else:
            print(f"⚠️  Template not found: {template_path}")
    
    # Create empty directories
    directories = [
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
    
    print("\n" + "=" * 50)
    print("✅ Claude documentation setup complete!")
    print("\n📋 Next steps:")
    print("1. Review and customize the generated files")
    print("2. Add your algorithm-specific documentation to docs/claude/reference/")
    print("3. Start your first Claude session with:")
    print('   "Please read docs/claude/ALWAYS_LOAD.md and docs/claude/current-sprint.md"')
    print("\n💡 Remember to commit with: ./git-pushlog origin main")

if __name__ == "__main__":
    setup_claude_docs()
