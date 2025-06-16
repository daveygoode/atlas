#!/bin/bash
# ATLAS Quick Install Script

echo "🚀 ATLAS Quick Installer"
echo "========================"

# Check if we're already in the atlas directory
if [ -f "IDENTITY.md" ] && [ -f "PROFESSIONAL_INSTRUCTION.md" ]; then
    echo "❌ Error: You appear to be running this from within the ATLAS directory."
    echo "Please run this from your project directory instead."
    exit 1
fi

# Check if .atlas already exists
if [ -d ".atlas" ]; then
    echo "❌ Error: .atlas directory already exists."
    echo "To reinstall, please remove it first: rm -rf .atlas"
    exit 1
fi

# Check if we're in a git repository
if [ -d ".git" ]; then
    echo "✅ Git repository detected"
else
    echo "⚠️  Warning: Not in a git repository. ATLAS works best with git."
fi

# Clone ATLAS
echo "📦 Cloning ATLAS repository..."
git clone https://github.com/daveygoode/atlas.git .atlas

# Check for existing CLAUDE.md
if [ -f "CLAUDE.md" ]; then
    echo "📄 Existing CLAUDE.md found"
    echo "Choose an option:"
    echo "1) Migrate existing project (preserves your CLAUDE.md)"
    echo "2) Fresh install (overwrites CLAUDE.md)"
    echo "3) Cancel"
    read -p "Enter choice (1-3): " choice
    
    case $choice in
        1)
            echo "🔄 Running migration..."
            python .atlas/scripts/migrate_existing_project.py
            ;;
        2)
            echo "📦 Running fresh install..."
            python .atlas/scripts/setup_new_project.py
            ;;
        3)
            echo "❌ Installation cancelled"
            rm -rf .atlas
            exit 0
            ;;
        *)
            echo "❌ Invalid choice"
            rm -rf .atlas
            exit 1
            ;;
    esac
else
    echo "📦 No existing CLAUDE.md found. Running fresh install..."
    python .atlas/scripts/setup_new_project.py
fi

echo ""
echo "✨ ATLAS installation complete!"
echo ""
echo "Next steps:"
echo "1. Edit SHORT_IMPORTANT_MEMORY.md with your project details"
echo "2. Start your first session:"
echo "   python scripts/save_session.py -c \"ATLAS setup complete\" -n \"Begin development\""
echo ""
echo "For more information, see .atlas/README.md"