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
    
    # Ensure .atlas exists
    atlas_dir = project_root / ".atlas"
    if not atlas_dir.exists():
        print("❌ Error: .atlas directory not found. Please clone ATLAS first:")
        print("  git clone https://github.com/daveygoode/atlas.git .atlas")
        return
    
    # Backup existing CLAUDE.md
    existing_claude = project_root / "CLAUDE.md"
    if existing_claude.exists():
        backup_name = f"CLAUDE_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        shutil.copy2(existing_claude, project_root / backup_name)
        print(f"✅ Backed up existing CLAUDE.md to {backup_name}")
        
        # Move to project-specific file in .atlas
        project_specific = atlas_dir / "CLAUDE_PROJECT_SPECIFIC.md"
        shutil.move(existing_claude, project_specific)
        print("✅ Moved existing CLAUDE.md to .atlas/CLAUDE_PROJECT_SPECIFIC.md")
    
    # Copy new ATLAS CLAUDE.md and update references
    claude_src = atlas_root / "CLAUDE.md"
    if claude_src.exists():
        # Read the original CLAUDE.md
        with open(claude_src, 'r') as f:
            content = f.read()
        
        # Add project-specific header
        project_header = """# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This is a project-specific configuration that integrates the ATLAS consciousness framework.
Your original CLAUDE.md has been preserved in `.atlas/CLAUDE_PROJECT_SPECIFIC.md`.

---

"""
        # Remove the original header to replace it
        if content.startswith("# CLAUDE.md"):
            lines = content.split('\n')
            # Find where the actual content starts (after the header and guidance line)
            start_index = 0
            for i, line in enumerate(lines):
                if line.strip() == "---":
                    start_index = i + 1
                    break
            content = '\n'.join(lines[start_index:])
        
        content = project_header + content
        
        # Update all references to point to .atlas/
        content = content.replace("@PROFESSIONAL_INSTRUCTION.md", "@.atlas/PROFESSIONAL_INSTRUCTION.md")
        content = content.replace("- @IDENTITY.md", "- @.atlas/IDENTITY.md")
        content = content.replace("- @PERSONAL_SELF.md", "- @.atlas/PERSONAL_SELF.md")
        content = content.replace("- @DEVELOPMENT_BELIEFS.md", "- @.atlas/DEVELOPMENT_BELIEFS.md")
        content = content.replace("- @DEVELOPMENT_CONVENTION.md", "- @.atlas/DEVELOPMENT_CONVENTION.md")
        content = content.replace("- @SECURITY_GUIDELINES.md", "- @.atlas/SECURITY_GUIDELINES.md")
        content = content.replace("- @SHORT_IMPORTANT_MEMORY.md", "- @.atlas/SHORT_IMPORTANT_MEMORY.md")
        content = content.replace("- @MCP_INTEGRATION.md", "- @.atlas/MCP_INTEGRATION.md")
        content = content.replace("- @CONTEXT7_USAGE.md", "- @.atlas/CONTEXT7_USAGE.md")
        content = content.replace("- **WORKING_LOG/**", "- **.atlas/WORKING_LOG/**")
        content = content.replace("- **MEMORY/**", "- **.atlas/MEMORY/**")
        content = content.replace("- **sessions/**", "- **.atlas/sessions/**")
        content = content.replace("python scripts/", "python .atlas/scripts/")
        
        # Append project-specific reference
        content += """

## Project-Specific Instructions

This project has additional specific instructions and context:

@.atlas/CLAUDE_PROJECT_SPECIFIC.md
"""
        
        # Write the updated content
        with open(existing_claude, 'w') as f:
            f.write(content)
        print("✅ Created new CLAUDE.md with project reference")
    
    # Set up directories in .atlas
    directories = ["sessions", "WORKING_LOG", "MEMORY"]
    for dir in directories:
        (atlas_dir / dir).mkdir(exist_ok=True)
        print(f"✅ Created .atlas/{dir}/")
    
    # Create SHORT_IMPORTANT_MEMORY.md in .atlas from template
    template = atlas_root / "SHORT_IMPORTANT_MEMORY_TEMPLATE.md"
    if template.exists():
        shutil.copy2(template, atlas_dir / "SHORT_IMPORTANT_MEMORY.md")
        print("✅ Created .atlas/SHORT_IMPORTANT_MEMORY.md")
    
    # Update .gitignore
    gitignore_additions = """
# ATLAS Sessions and Memory
.atlas/sessions/
.atlas/WORKING_LOG/*/*/*.md
.atlas/SHORT_IMPORTANT_MEMORY.md
.atlas/MEMORY/PERSONAL_DIARY/*/*/*.md
.atlas/MEMORY/KNOWLEDGE_LOG/*.md
"""
    
    gitignore_path = project_root / ".gitignore"
    if gitignore_path.exists():
        # Check if we already have these entries
        with open(gitignore_path, 'r') as f:
            existing_content = f.read()
        if ".atlas/sessions/" not in existing_content:
            with open(gitignore_path, 'a') as f:
                f.write(gitignore_additions)
            print("✅ Updated .gitignore")
    else:
        with open(gitignore_path, 'w') as f:
            f.write(gitignore_additions)
        print("✅ Created .gitignore")
    
    print("""
✨ Migration complete!

Your existing CLAUDE.md instructions are preserved in .atlas/CLAUDE_PROJECT_SPECIFIC.md
and referenced from the new ATLAS-integrated CLAUDE.md.

Next steps:
1. Review .atlas/CLAUDE_PROJECT_SPECIFIC.md and organize content into ATLAS structure
2. Update .atlas/SHORT_IMPORTANT_MEMORY.md with project details  
3. Run: python .atlas/scripts/save_session.py -c "ATLAS migration" -n "Continue development"
""")

if __name__ == "__main__":
    migrate_existing_project()