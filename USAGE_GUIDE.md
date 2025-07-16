# How to Use This Template System

## For New Projects

### 1. Clone the Template
```bash
git clone https://github.com/cofrankl01/documentation-template-system.git
cd documentation-template-system
```

### 2. Copy to Your Project
```bash
cp -r claude your-project/docs/
cp setup_claude_docs.py your-project/docs/
cd your-project/docs
```

### 3. Run Setup
```bash
python setup_claude_docs.py
```

Answer the prompts to customize for your project:
- Project name
- Algorithm type
- Current work
- File paths
- BigQuery settings

### 4. Start Using
Begin your first Claude session:
```
"Please read docs/claude/ALWAYS_LOAD.md and docs/claude/current-sprint.md"
```

## For Existing Projects

### 1. Backup Current Docs
```bash
mv docs/claude.md docs/claude.md.backup
```

### 2. Install Template
Follow steps 2-4 above

### 3. Migrate Content
- Move active work to `current-sprint.md`
- Archive old content to `completed/`
- Update paths and references

## Template Structure

```
your-project/
└── docs/
    ├── claude/
    │   ├── ALWAYS_LOAD.md          # Critical rules (50 lines)
    │   ├── current-sprint.md       # Active work (100 lines)
    │   ├── session-handoff.md      # Session notes
    │   ├── README.md               # Navigation
    │   ├── bestpractices/
    │   │   └── quick-reference.md  # Condensed rules
    │   ├── reference/              # Detailed guides
    │   └── completed/              # Archived sprints
    └── bestpractices.md            # Full standards
```

## Customization

### Modify Templates
Edit any `.template.md` file to change the structure for all future projects.

### Add Project-Specific Docs
Place in `docs/claude/reference/`:
- Algorithm guides
- API documentation
- Schema definitions
- Implementation details

### Update Placeholders
The setup script replaces these placeholders:
- `{{PROJECT_NAME}}` - Your project name
- `{{ALGORITHM_TYPE}}` - Type of algorithm/system
- `{{PRIMARY_IDS}}` - Main identifiers (BSS, SKU, etc.)
- `{{CURRENT_TASK_DESCRIPTION}}` - What you're working on
- And many more...

## Best Practices

### Daily Use
1. Start: Load ALWAYS_LOAD.md + current-sprint.md
2. Work: Claude auto-updates sprint progress
3. End: Update session-handoff.md
4. Commit: `./git-pushlog origin main`

### Weekly Maintenance
1. Archive completed work
2. Update current sprint goals
3. Clean up old session notes

### Team Collaboration
1. Share this template system
2. Everyone uses same structure
3. Consistent documentation across projects
4. Easy handoffs between developers

## Troubleshooting

### Missing Templates
If templates are missing, clone the latest version:
```bash
git clone https://github.com/cofrankl01/documentation-template-system.git
```

### Placeholder Issues
Check `.config.json` for saved values and manually update any missed placeholders.

### Context Too Large
If Claude complains about context:
1. Archive more content to `completed/`
2. Move details to `reference/`
3. Keep current-sprint.md under 100 lines

## Examples

### For Keyword Classification
```
Project name: kwr-expansion
Algorithm type: keyword-classification
Primary IDs: BSS-92588-723
Current task: Adding click/impression metrics
```

### For Pricing System
```
Project name: dynamic-pricing
Algorithm type: pricing-optimization
Primary IDs: SKU-12345
Current task: Implementing demand elasticity
```

## Support

- Template issues: Create issue on GitHub
- Project-specific: Check your project's README
- Best practices: See `/docs/bestpractices.md`
