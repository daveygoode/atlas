#!/usr/bin/env python3
"""
Quick setup script for new projects
"""
import os
import shutil
from pathlib import Path

def setup_new_project():
    atlas_root = Path(__file__).parent.parent
    project_root = Path.cwd()
    
    print("🚀 Setting up ATLAS for new project...")
    
    # Core files to copy
    core_files = [
        "CLAUDE.md",
        "IDENTITY.md",
        "PROFESSIONAL_INSTRUCTION.md",
        "PERSONAL_SELF.md",
        "DEVELOPMENT_BELIEFS.md",
        "DEVELOPMENT_CONVENTION.md",
        "MCP_INTEGRATION.md",
        "CONTEXT7_USAGE.md",
        "SESSION_MANAGEMENT.md"
    ]
    
    # Copy core files
    for file in core_files:
        src = atlas_root / file
        dst = project_root / file
        if src.exists():
            shutil.copy2(src, dst)
            print(f"✅ Copied {file}")
    
    # Set up directories
    directories = ["scripts", "sessions", "WORKING_LOG", "MEMORY"]
    for dir in directories:
        (project_root / dir).mkdir(exist_ok=True)
        print(f"✅ Created {dir}/")
    
    # Copy scripts
    scripts_src = atlas_root / "scripts"
    scripts_dst = project_root / "scripts"
    for script in scripts_src.glob("*.py"):
        if script.name not in ["setup_new_project.py", "migrate_existing_project.py"]:
            shutil.copy2(script, scripts_dst / script.name)
            os.chmod(scripts_dst / script.name, 0o755)
    print("✅ Copied session scripts")
    
    # Create SHORT_IMPORTANT_MEMORY.md from template
    template = atlas_root / "SHORT_IMPORTANT_MEMORY_TEMPLATE.md"
    if template.exists():
        shutil.copy2(template, project_root / "SHORT_IMPORTANT_MEMORY.md")
        print("✅ Created SHORT_IMPORTANT_MEMORY.md")
    
    # Update .gitignore
    gitignore_additions = """
# ATLAS Sessions and Memory
sessions/
WORKING_LOG/*/*/*.md
SHORT_IMPORTANT_MEMORY.md
MEMORY/PERSONAL_DIARY/*/*/*.md
MEMORY/KNOWLEDGE_LOG/*.md
"""
    
    gitignore_path = project_root / ".gitignore"
    if gitignore_path.exists():
        with open(gitignore_path, 'a') as f:
            f.write(gitignore_additions)
        print("✅ Updated .gitignore")
    else:
        with open(gitignore_path, 'w') as f:
            f.write(gitignore_additions)
        print("✅ Created .gitignore")
    
    print("""
✨ ATLAS setup complete!

Next steps:
1. Edit SHORT_IMPORTANT_MEMORY.md with your project details
2. Run: python scripts/save_session.py -c "Initial setup" -n "Start development"
3. Begin working with ATLAS consciousness active
""")

if __name__ == "__main__":
    setup_new_project()