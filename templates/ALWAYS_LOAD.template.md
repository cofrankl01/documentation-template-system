# ALWAYS LOAD - Critical Rules for Claude Code

## 🚨 MANDATORY Git Command
**ALWAYS use**: `./git-pushlog origin main`
- Never use regular `git push`
- This triggers Notion logging

## 📁 Project: {{PROJECT_NAME}}
- Algorithm: {{ALGORITHM_TYPE}}
- Primary Identifiers: {{PRIMARY_IDS}}
- Start Date: {{START_DATE}}

## 📁 File Locations
Claude should automatically place files based on purpose:
- **Production code**: `src/`
- **Scripts** (utilities): `scripts/`
- **Experiments**: `experiments/YYYY-MM-DD-description/`
- **Quick tests**: `experiments/sandbox/`
- **Tests**: `tests/` (with test_ prefix)
- **NEVER**: Create files in root directory

*Only ask about location if genuinely uncertain*

## 📝 Sprint Updates - AUTOMATIC
When completing tasks or making progress, automatically update `current-sprint.md` to reflect:
- ✅ Completed items (strike through with ~~text~~)
- 🚧 New blockers or issues discovered
- 💡 Key decisions made
- 📋 Next steps based on what was learned
- 🔚 Session summary before ending

*Keep updates concise and focused on what changed*

## 🎯 Current Focus
See: `current-sprint.md`

## 📚 Project-Specific Docs
- {{MAIN_ALGORITHM_DOC}}
- Best Practices: `docs/{{PROJECT_NAME}}-bestpractices.md`
- BigQuery Schemas: `reference/bigquery-schemas.md`
- Full Best Practices Template: `/docs/bestpractices-general-template.md`
