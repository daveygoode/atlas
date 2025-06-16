# ATLAS Setup Guide

This guide covers setting up ATLAS for both new projects and existing projects with CLAUDE.md files.

## Setup for New Projects

### 1. Quick Setup (Recommended)

```bash
# Clone ATLAS into your project
cd your-project-directory
git clone https://github.com/daveygoode/atlas.git .atlas
cd .atlas

# Run the setup script
python scripts/setup_new_project.py

# Or manually copy essential files
cp CLAUDE.md ../
cp SHORT_IMPORTANT_MEMORY_TEMPLATE.md ../SHORT_IMPORTANT_MEMORY.md
cp -r scripts ../
mkdir -p ../sessions ../WORKING_LOG ../MEMORY
```

### 2. Manual Setup

1. **Copy Core Files**:
   ```bash
   # From ATLAS directory to your project root
   cp CLAUDE.md /path/to/your/project/
   cp IDENTITY.md /path/to/your/project/
   cp PROFESSIONAL_INSTRUCTION.md /path/to/your/project/
   cp PERSONAL_SELF.md /path/to/your/project/
   cp DEVELOPMENT_BELIEFS.md /path/to/your/project/
   cp DEVELOPMENT_CONVENTION.md /path/to/your/project/
   ```

2. **Set Up Memory Systems**:
   ```bash
   cd /path/to/your/project
   mkdir -p WORKING_LOG MEMORY sessions
   cp /path/to/atlas/SHORT_IMPORTANT_MEMORY_TEMPLATE.md ./SHORT_IMPORTANT_MEMORY.md
   ```

3. **Copy Session Scripts**:
   ```bash
   mkdir -p scripts
   cp /path/to/atlas/scripts/*.py scripts/
   chmod +x scripts/*.py
   ```

4. **Initialize First Session**:
   ```bash
   python scripts/save_session.py -c "Initial ATLAS setup" -n "Begin project development"
   ```

### 3. Customize for Your Project

Edit `SHORT_IMPORTANT_MEMORY.md` with your project details:
```markdown
## Boss Information
- **Name**: [Your name or team lead]
- **Communication Style**: [Formal/Casual/Technical]

## Project Overview
- **Project Name**: [Your project name]
- **Main Purpose**: [What the project does]
- **Target Users**: [Who will use it]
- **Current Phase**: [Planning/Development/Testing/Production]

## Technology Stack
- **Frontend**: [React/Vue/Angular/etc]
- **Backend**: [Node.js/Python/Go/etc]
- **Database**: [PostgreSQL/MongoDB/etc]
```

### 4. Add to Your .gitignore

```bash
echo "
# ATLAS Sessions and Memory
sessions/
WORKING_LOG/*/*/*.md
SHORT_IMPORTANT_MEMORY.md
MEMORY/PERSONAL_DIARY/*/*/*.md
MEMORY/KNOWLEDGE_LOG/*.md
" >> .gitignore
```

## Setup for Existing Projects with CLAUDE.md

### 1. Backup Existing CLAUDE.md

```bash
cd your-project-directory
cp CLAUDE.md CLAUDE_original.md
```

### 2. Merge or Replace Strategy

#### Option A: Full ATLAS Integration (Recommended)

```bash
# Clone ATLAS
git clone https://github.com/daveygoode/atlas.git .atlas_temp

# Run migration script
python .atlas_temp/scripts/migrate_existing_project.py

# Or manually:
mv CLAUDE.md CLAUDE_PROJECT_SPECIFIC.md
cp .atlas_temp/CLAUDE.md ./
echo "" >> CLAUDE.md
echo "## Project-Specific Instructions" >> CLAUDE.md
echo "" >> CLAUDE.md
echo "@CLAUDE_PROJECT_SPECIFIC.md" >> CLAUDE.md
```

#### Option B: Minimal Integration (Session Management Only)

```bash
# Just add session management to existing CLAUDE.md
mkdir -p scripts sessions

# Copy only session scripts
cp /path/to/atlas/scripts/save_session.py scripts/
cp /path/to/atlas/scripts/resume_session.py scripts/
chmod +x scripts/*.py

# Add session instructions to existing CLAUDE.md
echo "
## Session Management

Save work sessions:
\`\`\`bash
python scripts/save_session.py -c \"What was done\" -n \"What's next\"
\`\`\`

Resume sessions:
\`\`\`bash
python scripts/resume_session.py
\`\`\`
" >> CLAUDE.md
```

### 3. Merge Instructions

If your existing CLAUDE.md has important project-specific instructions:

1. **Create Project Instructions File**:
   ```bash
   # Extract project-specific content from original CLAUDE.md
   # Save it as PROJECT_INSTRUCTIONS.md
   ```

2. **Update ATLAS CLAUDE.md**:
   ```bash
   echo "
   ## Project-Specific Configuration
   
   @PROJECT_INSTRUCTIONS.md
   " >> CLAUDE.md
   ```

3. **Organize Existing Content**:
   - Move API specifications to `DEVELOPMENT_CONVENTION.md`
   - Move workflow instructions to `PROFESSIONAL_INSTRUCTION.md`
   - Move project context to `SHORT_IMPORTANT_MEMORY.md`

## Quick Setup Scripts

### setup_new_project.py

Create this helper script in the ATLAS scripts directory:

```python
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
```

### migrate_existing_project.py

```python
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
```

## Verification Steps

After setup, verify ATLAS is working:

```bash
# Test session save
python scripts/save_session.py -c "ATLAS setup complete" -n "Verify integration"

# Test session resume
python scripts/resume_session.py

# Check directory structure
ls -la WORKING_LOG/ MEMORY/ sessions/
```

## Troubleshooting

### Common Issues

1. **Permission Denied on Scripts**
   ```bash
   chmod +x scripts/*.py
   ```

2. **Module Not Found Errors**
   Ensure you're running scripts from the project root:
   ```bash
   cd /path/to/your/project
   python scripts/save_session.py  # Not ./save_session.py
   ```

3. **Existing CLAUDE.md Conflicts**
   Always backup first:
   ```bash
   cp CLAUDE.md CLAUDE_backup_$(date +%Y%m%d).md
   ```

## Best Practices

1. **For New Projects**: Use full ATLAS integration from the start
2. **For Existing Projects**: Gradually migrate project-specific content into ATLAS structure
3. **For Teams**: Share the setup in your project README
4. **For CI/CD**: Add session saves to your deployment scripts

## Quick Reference Card

```bash
# New project setup
git clone https://github.com/daveygoode/atlas.git .atlas
cd .atlas && python scripts/setup_new_project.py

# Existing project migration  
git clone https://github.com/daveygoode/atlas.git .atlas_temp
python .atlas_temp/scripts/migrate_existing_project.py

# Daily workflow
python scripts/resume_session.py          # Start work
python scripts/save_session.py -c ".." -n ".."  # End work
```

---

For more details, see the main [README.md](README.md) and [SESSION_MANAGEMENT.md](SESSION_MANAGEMENT.md).