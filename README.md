# Claude Documentation Template System

This repository contains a standardized template for setting up Claude Code documentation across all your projects. It ensures consistent structure and best practices for AI-assisted development.

## 🚀 Quick Start

1. Clone this template to your project:
   ```bash
   git clone https://github.com/cofrankl01/documentation-template-system.git
   cd documentation-template-system
   cp -r templates your-project/docs/
   cp setup_claude_docs_enhanced.py your-project/
   cd your-project
   ```

2. Run the setup script:
   ```bash
   python setup_claude_docs_enhanced.py
   ```

3. Answer the prompts to customize for your project

4. Review and customize the generated best practices:
   ```bash
   # Edit docs/[your-project]-bestpractices.md
   ```

5. Start your first Claude session:
   ```
   "Please read:
   1. docs/claude/ALWAYS_LOAD.md
   2. docs/[your-project]-bestpractices.md
   3. docs/claude/current-sprint.md"
   ```

## 📁 Template Structure

```
documentation-template-system/
├── README.md                         # This file
├── SETUP_INSTRUCTIONS.md             # Detailed setup guide for humans
├── COMMON_MISTAKES.md                # Common pitfalls and how to avoid them
├── templates/                        # All template files
│   ├── ALWAYS_LOAD.template.md
│   ├── current-sprint.template.md
│   ├── session-handoff.template.md
│   ├── README.template.md
│   ├── bestpractices.template.md     # General template with [PLACEHOLDERS]
│   └── quick-reference.template.md
├── examples/                         # Example implementations
│   ├── bestpractices-data-pipeline.md
│   ├── bestpractices-web-app.md
│   └── bestpractices-ml-project.md
├── setup_claude_docs_enhanced.py     # Enhanced setup script
└── setup_claude_docs_simple.py       # Simple setup script
```

## 🎯 Key Features

- **Clear Templates**: All templates use obvious [PLACEHOLDERS] that must be replaced
- **Project-Specific Best Practices**: Generates customized documentation for your project
- **Structure Validation**: Includes verification scripts to ensure proper setup
- **Type-Based Customization**: Adapts to different project types (data, web, ML, etc.)
- **Mistake Prevention**: Common mistakes documentation and validation checks

## 📋 What Gets Generated

When you run the setup script, it creates:

```
your-project/
├── docs/
│   ├── claude/
│   │   ├── ALWAYS_LOAD.md           # Critical rules
│   │   ├── current-sprint.md        # Active work tracking
│   │   ├── session-handoff.md       # Session notes
│   │   ├── README.md                # Navigation
│   │   ├── STARTUP_INSTRUCTIONS.md  # How to start Claude sessions
│   │   └── .config.json             # Setup configuration
│   └── [project-name]-bestpractices.md  # PROJECT-SPECIFIC guidelines
├── scripts/
│   └── verify_structure.py          # Validates project structure
└── [proper directory structure based on project type]
```

## ⚠️ Important: Always Customize!

The setup process generates templates with placeholders. You MUST:

1. **Review the generated best practices document**
2. **Remove sections that don't apply**
3. **Add project-specific guidelines**
4. **Update examples to match your project**
5. **Run the verification script**

## 🔍 Validation and Health Checks

After setup, the system provides:

- **Placeholder Detection**: Warns about any remaining [PLACEHOLDERS]
- **Structure Verification**: `python scripts/verify_structure.py`
- **Setup Health Check**: Confirms all components are properly configured
- **Common Mistakes Guide**: Reference for avoiding pitfalls

## 🤝 Contributing

To improve the template system:
1. Make changes in this repository
2. Test thoroughly with different project types
3. Update examples and documentation
4. Submit PR with clear description of improvements

## 📚 Documentation

- **For Setup**: Read `SETUP_INSTRUCTIONS.md`
- **For Mistakes**: Read `COMMON_MISTAKES.md`
- **For Examples**: Check the `examples/` directory

## 🚨 Most Common Mistake

**Never use another project's bestpractices.md directly!** Always generate fresh from the template and customize for your specific project. This was the root cause of the issues that led to creating this improved system.

---

For questions or improvements, contact @cofrankl01
