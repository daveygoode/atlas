#!/bin/bash
# ATLAS Quick Install Script

echo "🚀 ATLAS Quick Installer"
echo "========================"

# Check if we're in a git repository
if [ -d ".git" ]; then
    echo "✅ Git repository detected"
else
    echo "⚠️  Warning: Not in a git repository. ATLAS works best with git."
fi

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
            git clone https://github.com/daveygoode/atlas.git .atlas_temp
            python .atlas_temp/scripts/migrate_existing_project.py
            rm -rf .atlas_temp
            ;;
        2)
            echo "📦 Running fresh install..."
            git clone https://github.com/daveygoode/atlas.git .atlas
            cd .atlas
            python scripts/setup_new_project.py
            cd ..
            ;;
        3)
            echo "❌ Installation cancelled"
            exit 0
            ;;
        *)
            echo "❌ Invalid choice"
            exit 1
            ;;
    esac
else
    echo "📦 No existing CLAUDE.md found. Running fresh install..."
    git clone https://github.com/daveygoode/atlas.git .atlas
    cd .atlas
    python scripts/setup_new_project.py
    cd ..
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