#!/usr/bin/env python3
"""
Simplified setup script for Claude documentation
Only asks essential questions, intelligently defaults the rest
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
    info['ALGORITHM_TYPE'] = input("What type of system? (e.g., keyword-analysis, pricing, inventory): ")
    info['CURRENT_TASK_DESCRIPTION'] = input("What are you working on first? ")
    
    # Auto-generate from essentials
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
    print(f"   Type: {info['ALGORITHM_TYPE']}")
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
    
    # Create a note about updating details
    update_note = Path('docs/claude/UPDATE_DETAILS.md')
    with open(update_note, 'w') as f:
        f.write(f"""# Project Details to Update

As you work on {project_info['PROJECT_NAME']}, update these placeholders in the documentation:

## In ALWAYS_LOAD.md:
- **Primary Identifiers**: Currently "TBD" - update when you identify the main IDs (BSS, SKU, etc.)

## In current-sprint.md:
- **Working On - File**: Currently points to a default script name
- **Output**: Currently "TBD" - update with actual output location
- **Test Case**: Currently "TBD" - add actual test identifiers

## Optional Updates:
- **Team Name**: Currently generic - update if needed
- **BigQuery Settings**: Currently uses defaults - update when you set up tables

These can be updated naturally as the project develops!
""")
    print(f"✅ Created update reminder: {update_note}")
    
    print("\n" + "=" * 50)
    print("✅ Claude documentation setup complete!")
    print("\n📋 Next steps:")
    print("1. Start your Claude session with:")
    print('   "Please read docs/claude/ALWAYS_LOAD.md and docs/claude/current-sprint.md"')
    print("2. Update details as you learn more about the project")
    print("3. Remember to commit with: ./git-pushlog origin main")

if __name__ == "__main__":
    setup_claude_docs()
