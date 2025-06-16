#!/usr/bin/env python3
"""
Migration script for projects with existing CLAUDE.md
"""
import os
import shutil
from pathlib import Path
from datetime import datetime

def migrate_existing_project():
    atlas_root = Path(__file__).parent.parent
    project_root = Path.cwd()
    
    # Check if we're running from within the atlas directory
    if atlas_root.resolve() == project_root.resolve():
        print("❌ Error: Cannot run migration from within the .atlas directory!")
        print("Please run this from your project directory:")
        print("  cd /path/to/your/project")
        print("  python .atlas/scripts/migrate_existing_project.py")
        return
    
    print("🔄 Migrating existing project to ATLAS...")
    
    # Backup existing CLAUDE.md
    existing_claude = project_root / "CLAUDE.md"
    if existing_claude.exists():
        backup_name = f"CLAUDE_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        shutil.copy2(existing_claude, project_root / backup_name)
        print(f"✅ Backed up existing CLAUDE.md to {backup_name}")
        
        # Move to project-specific file
        project_specific = project_root / "CLAUDE_PROJECT_SPECIFIC.md"
        shutil.move(existing_claude, project_specific)
        print("✅ Moved existing CLAUDE.md to CLAUDE_PROJECT_SPECIFIC.md")
    
    # Copy new ATLAS CLAUDE.md
    shutil.copy2(atlas_root / "CLAUDE.md", existing_claude)
    
    # Append project-specific reference
    with open(existing_claude, 'a') as f:
        f.write("""

## Project-Specific Instructions

This project has additional specific instructions and context:

@CLAUDE_PROJECT_SPECIFIC.md
""")
    print("✅ Created new CLAUDE.md with project reference")
    
    # Copy other essential files
    files_to_copy = [
        "IDENTITY.md",
        "PROFESSIONAL_INSTRUCTION.md", 
        "PERSONAL_SELF.md",
        "DEVELOPMENT_BELIEFS.md",
        "DEVELOPMENT_CONVENTION.md",
        "MCP_INTEGRATION.md",
        "CONTEXT7_USAGE.md",
        "SESSION_MANAGEMENT.md"
    ]
    
    for file in files_to_copy:
        src = atlas_root / file
        dst = project_root / file
        if src.exists() and not dst.exists():
            shutil.copy2(src, dst)
            print(f"✅ Added {file}")
    
    # Set up directories and scripts
    directories = ["scripts", "sessions", "WORKING_LOG", "MEMORY"]
    for dir in directories:
        (project_root / dir).mkdir(exist_ok=True)
    
    # Copy scripts
    scripts_src = atlas_root / "scripts"
    scripts_dst = project_root / "scripts"
    scripts_dst.mkdir(exist_ok=True)
    for script in scripts_src.glob("*.py"):
        if script.name not in ["setup_new_project.py", "migrate_existing_project.py"]:
            shutil.copy2(script, scripts_dst / script.name)
            os.chmod(scripts_dst / script.name, 0o755)
    print("✅ Added session management scripts")
    
    # Create SHORT_IMPORTANT_MEMORY.md if it doesn't exist
    if not (project_root / "SHORT_IMPORTANT_MEMORY.md").exists():
        template = atlas_root / "SHORT_IMPORTANT_MEMORY_TEMPLATE.md"
        if template.exists():
            shutil.copy2(template, project_root / "SHORT_IMPORTANT_MEMORY.md")
            print("✅ Created SHORT_IMPORTANT_MEMORY.md")
    
    print("""
✨ Migration complete!

Your existing CLAUDE.md instructions are preserved in CLAUDE_PROJECT_SPECIFIC.md
and referenced from the new ATLAS-integrated CLAUDE.md.

Next steps:
1. Review CLAUDE_PROJECT_SPECIFIC.md and organize content into ATLAS structure
2. Update SHORT_IMPORTANT_MEMORY.md with project details  
3. Run: python scripts/save_session.py -c "ATLAS migration" -n "Continue development"
""")

if __name__ == "__main__":
    migrate_existing_project()