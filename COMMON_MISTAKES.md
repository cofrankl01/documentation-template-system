# Common Template Mistakes to Avoid

## 1. Using Another Project's Best Practices
**Problem**: Copying bestpractices.md from another project without customization  
**Symptoms**: References to wrong project names, incorrect technology stack, mismatched examples  
**Solution**: Always generate fresh from template and customize for your specific project

## 2. Not Customizing Placeholders
**Problem**: Leaving [PLACEHOLDER] or {{PLACEHOLDER}} text in documents  
**Symptoms**: Claude gets confused about project specifics, generic instructions remain  
**Solution**: 
- Search for `[` and `{{` brackets after setup
- Run the validation script
- Review all generated documents

## 3. Wrong Directory Usage
**Problem**: Putting production code in scripts/ directory  
**Symptoms**: Controllers, pipelines, and core logic mixed with utility scripts  
**Solution**: 
- Use the decision tree in best practices
- `src/` = production code
- `scripts/` = utilities and runners
- When in doubt, ask!

## 4. Skipping the Best Practices Document
**Problem**: Only loading ALWAYS_LOAD.md and current-sprint.md  
**Symptoms**: Claude doesn't know project structure, creates files in wrong places  
**Solution**: Always include project-specific best practices in startup prompt:
```
Please read:
1. docs/claude/ALWAYS_LOAD.md
2. docs/[project-name]-bestpractices.md
3. docs/claude/current-sprint.md
```

## 5. Not Running Verification
**Problem**: Assuming setup completed correctly without checking  
**Symptoms**: Structural issues discovered later, imports fail  
**Solution**: Always run `python scripts/verify_structure.py` after setup

## 6. Generic Project Information
**Problem**: Using vague descriptions like "my project" or "data processing"  
**Symptoms**: Generated documentation lacks specificity  
**Solution**: Provide specific, descriptive names and purposes during setup

## 7. Ignoring Project Type
**Problem**: Not selecting appropriate project type during setup  
**Symptoms**: Wrong examples and structure for your project  
**Solution**: Choose the closest match:
- Data Pipeline / ETL
- Web Application
- Machine Learning
- API Service
- Other (customize heavily)

## 8. Hardcoding Paths
**Problem**: Using absolute paths in documentation  
**Symptoms**: Documentation breaks when shared or moved  
**Solution**: Always use relative paths from project root

## 9. Not Updating Sprint Documents
**Problem**: Leaving template sprint information unchanged  
**Symptoms**: Claude works on wrong tasks, outdated information  
**Solution**: Update current-sprint.md before each session

## 10. Mixing Template and Project Files
**Problem**: Keeping template files in project directory  
**Symptoms**: Confusion about which files to edit  
**Solution**: 
- Delete template files after setup
- Only keep generated, customized files
- Store templates separately

## Prevention Checklist

Before starting with Claude, verify:
- [ ] All placeholders replaced in documentation
- [ ] Best practices document customized for project
- [ ] Directory structure matches documentation
- [ ] Verification script runs successfully
- [ ] Startup prompt includes all three documents
- [ ] Current sprint information is up to date

## If Things Go Wrong

1. **Run verification**: `python scripts/verify_structure.py`
2. **Check for placeholders**: Search for `[` and `{{` in all .md files
3. **Review best practices**: Ensure it matches your project
4. **Reorganize if needed**: Move files to correct directories
5. **Update imports**: Fix any broken import statements
6. **Document changes**: Update best practices to reflect reality

Remember: The template is a starting point, not a rigid structure. Customize it to fit your project's needs!
