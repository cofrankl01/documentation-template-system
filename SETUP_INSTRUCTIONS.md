# Setup Instructions for Documentation Template System

This document is for **human users** who want to use this template system to set up Claude documentation for their projects.

## 🚀 Quick Start

### For New Projects

1. **Clone the Template**
   ```bash
   git clone https://github.com/cofrankl01/documentation-template-system.git
   cd documentation-template-system
   ```

2. **Copy to Your Project**
   ```bash
   cp -r templates your-project/docs/
   cp setup_claude_docs_simple.py your-project/
   cd your-project
   ```

3. **Run Setup**
   ```bash
   python setup_claude_docs_simple.py
   ```

4. **Customize Generated Documentation**
   - Review `docs/[your-project]-bestpractices.md`
   - Remove sections that don't apply
   - Update examples to match your project
   - Search for any remaining placeholders

5. **Verify Structure**
   ```bash
   python scripts/verify_structure.py
   ```

6. **Start Your First Claude Session**
   ```
   "Please read:
   1. docs/claude/ALWAYS_LOAD.md
   2. docs/[your-project]-bestpractices.md
   3. docs/claude/current-sprint.md"
   ```

### For Existing Projects

1. **Backup Current Docs**
   ```bash
   mv docs/claude.md docs/claude.md.backup
   ```

2. **Install Template**
   Follow steps 2-6 above

3. **Migrate Content**
   - Move active work to `current-sprint.md`
   - Archive old content to `completed/`
   - Update paths and references

## 📋 What Gets Created

```
your-project/
└── docs/
    ├── claude/
    │   ├── ALWAYS_LOAD.md          # Critical rules (50 lines)
    │   ├── current-sprint.md       # Active work (100 lines)
    │   ├── session-handoff.md      # Session notes
    │   ├── README.md               # Navigation
    │   └── .config.json            # Setup configuration
    ├── [project-name]-bestpractices.md  # Project-specific guidelines
    └── scripts/
        └── verify_structure.py      # Structure validation tool
```

## ⚠️ Important Notes

- **Always customize** the generated best practices document
- **Never skip** the placeholder replacement step
- **Verify** your structure matches the documentation
- **Update** documentation as your project evolves

## 🔧 Customization Guide

### Required Customizations
1. Project name and description
2. Technology stack and tools
3. Directory structure examples
4. Naming conventions
5. Workflow guidelines

### Optional Sections to Add
- API standards
- Security guidelines
- Performance requirements
- Deployment procedures

## 📞 Support

- Template issues: Create issue on GitHub
- Documentation questions: Check examples/ directory
- Best practices: See generated bestpractices document
