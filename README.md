# Claude Documentation Template System

This repository contains a standardized template for setting up Claude Code documentation across all your projects. It ensures consistent structure and best practices for AI-assisted development.

## 🚀 Quick Start

1. Clone this template to your project:
   ```bash
   cp -r claude-docs-template/* your-project/docs/
   ```

2. Run the setup script:
   ```bash
   cd your-project/docs
   python setup_claude_docs.py
   ```

3. Answer the prompts to customize for your project

4. Start your first Claude session:
   ```
   "Please read docs/claude/ALWAYS_LOAD.md and docs/claude/current-sprint.md"
   ```

## 📁 Template Structure

```
claude-docs-template/
├── README.md                    # This file
├── setup_claude_docs.py        # Interactive setup script
├── claude/
│   ├── ALWAYS_LOAD.template.md
│   ├── current-sprint.template.md
│   ├── session-handoff.template.md
│   ├── README.template.md
│   └── bestpractices/
│       └── quick-reference.template.md
└── templates.json              # Template variable definitions
```

## 🎯 Benefits

- **Consistent Structure**: Every project follows the same documentation pattern
- **Efficient Context**: Only loads necessary files (150 lines vs 2000+)
- **Auto-Updates**: Claude automatically updates sprint progress
- **Git Integration**: Always uses custom push commands
- **Scalable**: Works for any project type or algorithm

## 📝 Customization

Each template file contains placeholders like `{{PROJECT_NAME}}` that get replaced during setup. You can modify the templates to match your organization's needs.

## 🤝 Contributing

To improve the template system:
1. Make changes in this repository
2. Test on a sample project
3. Update all active projects with the new template

For questions or improvements, contact @cofrankl01
