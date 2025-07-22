# Claude Documentation Hub - {{PROJECT_NAME}}

## 📚 Quick Navigation

### Essential Files (Load Every Session)
1. **[ALWAYS_LOAD.md](./ALWAYS_LOAD.md)** - Critical rules and git commands
2. **[{{PROJECT_NAME}}-bestpractices.md](../{{PROJECT_NAME}}-bestpractices.md)** - Project structure and standards
3. **[current-sprint.md](./current-sprint.md)** - What we're working on now

### Session Management
- **[session-handoff.md](./session-handoff.md)** - Update at end of each session

### Reference Documentation (Load When Needed)
- **[{{ALGORITHM_NAME}} Guide](./reference/{{ALGORITHM_FILE}})** - Algorithm details
- **[BigQuery Schemas](./reference/bigquery-schemas.md)** - Database structures

### Completed Work
- **[completed/](./completed/)** - Archive of past sprints

## 🚀 How to Start a Session

```
"Please read:
1. docs/claude/ALWAYS_LOAD.md
2. docs/{{PROJECT_NAME}}-bestpractices.md
3. docs/claude/current-sprint.md"
```

## 📝 How to End a Session

1. Update `session-handoff.md` with what was done
2. Commit with: `./git-pushlog origin main`

## 🎯 Current Focus
{{CURRENT_FOCUS_DESCRIPTION}}

## 📂 Directory Structure
```
docs/claude/
├── ALWAYS_LOAD.md           # Load every session
├── current-sprint.md        # Active work
├── session-handoff.md       # Session transitions
├── README.md               # This file
├── bestpractices/          # Quick reference guides
├── reference/              # Detailed documentation
└── completed/              # Archived work
```

## 🏢 Project Information
- **Project**: {{PROJECT_NAME}}
- **Algorithm**: {{ALGORITHM_TYPE}}
- **Team**: {{TEAM_NAME}}
- **Started**: {{START_DATE}}
