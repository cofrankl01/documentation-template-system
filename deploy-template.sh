#!/bin/bash

# Quick deployment script for Claude documentation template
# Usage: ./deploy-template.sh /path/to/your/project

if [ $# -eq 0 ]; then
    echo "Usage: $0 /path/to/your/project"
    echo "Example: $0 ~/projects/my-algorithm"
    exit 1
fi

PROJECT_PATH="$1"
TEMPLATE_PATH="$(dirname "$0")"

echo "🚀 Deploying Claude documentation template to: $PROJECT_PATH"
echo "================================================"

# Create docs directory if it doesn't exist
mkdir -p "$PROJECT_PATH/docs"

# Copy template files
echo "📁 Copying template files..."
cp -r "$TEMPLATE_PATH/claude" "$PROJECT_PATH/docs/"
cp "$TEMPLATE_PATH/setup_claude_docs.py" "$PROJECT_PATH/docs/"

# Navigate to project
cd "$PROJECT_PATH/docs" || exit

# Make setup script executable
chmod +x setup_claude_docs.py

echo "✅ Template files copied successfully!"
echo ""
echo "📋 Next steps:"
echo "1. cd $PROJECT_PATH/docs"
echo "2. python setup_claude_docs.py"
echo "3. Answer the prompts to customize for your project"
echo ""
echo "🎯 Quick start your first session with:"
echo '   "Please read docs/claude/ALWAYS_LOAD.md and docs/claude/current-sprint.md"'
