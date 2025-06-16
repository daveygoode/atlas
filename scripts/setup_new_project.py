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
    
    # Check if we're running from within the atlas directory
    if atlas_root.resolve() == project_root.resolve():
        print("❌ Error: Cannot run setup from within the .atlas directory!")
        print("Please run this from your project directory:")
        print("  cd /path/to/your/project")
        print("  python .atlas/scripts/setup_new_project.py")
        return
    
    print("🚀 Setting up ATLAS for new project...")
    
    # Ensure .atlas exists
    atlas_dir = project_root / ".atlas"
    if not atlas_dir.exists():
        print("❌ Error: .atlas directory not found. Please clone ATLAS first:")
        print("  git clone https://github.com/daveygoode/atlas.git .atlas")
        return
    
    # Copy CLAUDE.md to project root
    claude_src = atlas_root / "CLAUDE.md"
    claude_dst = project_root / "CLAUDE.md"
    if claude_src.exists():
        # Read the original CLAUDE.md
        with open(claude_src, 'r') as f:
            content = f.read()
        
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
        
        # Write the updated content
        with open(claude_dst, 'w') as f:
            f.write(content)
        print("✅ Created CLAUDE.md in project root")
    
    # All other files stay in .atlas (already there from git clone)
    # Just need to set up the working directories
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
✨ ATLAS setup complete!

Next steps:
1. Edit .atlas/SHORT_IMPORTANT_MEMORY.md with your project details
2. Run: python .atlas/scripts/save_session.py -c "Initial setup" -n "Start development"
3. Begin working with ATLAS consciousness active
""")

if __name__ == "__main__":
    setup_new_project()