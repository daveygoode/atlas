#!/usr/bin/env python3
"""
Update ATLAS framework to latest version
Pulls latest instructions and scripts from the ATLAS repository
"""
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
import json
import sys


class AtlasUpdater:
    def __init__(self):
        # Detect if we're running from within .atlas or from project root
        script_path = Path(__file__).resolve()
        if '.atlas' in script_path.parts:
            # Running from .atlas/scripts/
            self.atlas_dir = Path(__file__).parent.parent
            self.project_root = self.atlas_dir.parent
        else:
            # Running from copied location (old structure)
            self.project_root = Path.cwd()
            self.atlas_dir = self.project_root / ".atlas"
        
        self.backup_dir = self.atlas_dir / "backups" / datetime.now().strftime('%Y%m%d_%H%M%S')
        
    def check_git_status(self):
        """Ensure the atlas directory is clean before updating"""
        try:
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.atlas_dir,
                capture_output=True,
                text=True
            )
            if result.stdout.strip():
                print("⚠️  Warning: You have uncommitted changes in .atlas/")
                print("   Please commit or stash changes before updating.")
                response = input("   Continue anyway? (y/N): ")
                return response.lower() == 'y'
            return True
        except Exception as e:
            print(f"❌ Error checking git status: {e}")
            return False
    
    def backup_customizations(self):
        """Backup any customized files before update"""
        print("\n📦 Backing up customizations...")
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Files that might have local customizations
        files_to_backup = [
            "SHORT_IMPORTANT_MEMORY.md",
            "CLAUDE_PROJECT_SPECIFIC.md",
        ]
        
        for file in files_to_backup:
            src = self.atlas_dir / file
            if src.exists():
                dst = self.backup_dir / file
                shutil.copy2(src, dst)
                print(f"   ✅ Backed up {file}")
        
        # Backup any session data
        sessions_dir = self.atlas_dir / "sessions"
        if sessions_dir.exists() and any(sessions_dir.iterdir()):
            backup_sessions = self.backup_dir / "sessions"
            shutil.copytree(sessions_dir, backup_sessions)
            print("   ✅ Backed up session data")
    
    def pull_latest(self):
        """Pull latest changes from ATLAS repository"""
        print("\n🔄 Pulling latest ATLAS updates...")
        try:
            # First fetch to see what's new
            subprocess.run(
                ["git", "fetch", "origin", "main"],
                cwd=self.atlas_dir,
                check=True
            )
            
            # Check what files will be updated
            result = subprocess.run(
                ["git", "diff", "--name-only", "HEAD", "origin/main"],
                cwd=self.atlas_dir,
                capture_output=True,
                text=True
            )
            
            if not result.stdout.strip():
                print("   ✅ Already up to date!")
                return True
            
            print("   Files to be updated:")
            for file in result.stdout.strip().split('\n'):
                print(f"     - {file}")
            
            # Pull the changes
            subprocess.run(
                ["git", "pull", "origin", "main"],
                cwd=self.atlas_dir,
                check=True
            )
            print("   ✅ Successfully pulled latest changes")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Error pulling updates: {e}")
            return False
    
    def update_project_claude_md(self):
        """Update the project's CLAUDE.md with new structure"""
        print("\n📝 Updating project CLAUDE.md...")
        
        # Read the latest CLAUDE.md from atlas
        atlas_claude = self.atlas_dir / "CLAUDE.md"
        project_claude = self.project_root / "CLAUDE.md"
        
        if not atlas_claude.exists():
            print("   ❌ Could not find updated CLAUDE.md")
            return
        
        # Back up existing CLAUDE.md
        if project_claude.exists():
            backup_path = self.backup_dir / "CLAUDE.md"
            shutil.copy2(project_claude, backup_path)
            print(f"   ✅ Backed up existing CLAUDE.md")
        
        # Read and process the new CLAUDE.md
        with open(atlas_claude, 'r') as f:
            content = f.read()
        
        # Update paths to point to .atlas/
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
        
        # Add project-specific reference if it exists
        if (self.atlas_dir / "CLAUDE_PROJECT_SPECIFIC.md").exists():
            if "@.atlas/CLAUDE_PROJECT_SPECIFIC.md" not in content:
                content += """

## Project-Specific Instructions

This project has additional specific instructions and context:

@.atlas/CLAUDE_PROJECT_SPECIFIC.md
"""
        
        # Write updated content
        with open(project_claude, 'w') as f:
            f.write(content)
        
        print("   ✅ Updated project CLAUDE.md")
    
    def restore_customizations(self):
        """Restore backed up customizations"""
        print("\n🔄 Restoring customizations...")
        
        # Restore SHORT_IMPORTANT_MEMORY.md if it was customized
        backup_memory = self.backup_dir / "SHORT_IMPORTANT_MEMORY.md"
        if backup_memory.exists():
            shutil.copy2(backup_memory, self.atlas_dir / "SHORT_IMPORTANT_MEMORY.md")
            print("   ✅ Restored SHORT_IMPORTANT_MEMORY.md")
        
        # Restore project-specific instructions
        backup_specific = self.backup_dir / "CLAUDE_PROJECT_SPECIFIC.md"
        if backup_specific.exists():
            shutil.copy2(backup_specific, self.atlas_dir / "CLAUDE_PROJECT_SPECIFIC.md")
            print("   ✅ Restored CLAUDE_PROJECT_SPECIFIC.md")
    
    def show_changelog(self):
        """Show recent changes in ATLAS"""
        print("\n📋 Recent ATLAS updates:")
        try:
            result = subprocess.run(
                ["git", "log", "--oneline", "-10", "--pretty=format:%h %s (%cr)"],
                cwd=self.atlas_dir,
                capture_output=True,
                text=True
            )
            if result.stdout:
                for line in result.stdout.strip().split('\n'):
                    print(f"   {line}")
        except Exception:
            print("   Could not retrieve changelog")
    
    def run_update(self):
        """Main update process"""
        print("🚀 ATLAS Framework Updater")
        print("=" * 50)
        
        # Check if .atlas exists
        if not self.atlas_dir.exists():
            print("❌ Error: .atlas directory not found!")
            print("   Please run from a project with ATLAS installed.")
            return False
        
        # Check git status
        if not self.check_git_status():
            return False
        
        # Backup customizations
        self.backup_customizations()
        
        # Pull latest changes
        if not self.pull_latest():
            print("\n❌ Update failed. Your backups are in:")
            print(f"   {self.backup_dir}")
            return False
        
        # Update project files
        self.update_project_claude_md()
        
        # Restore customizations
        self.restore_customizations()
        
        # Show what's new
        self.show_changelog()
        
        print("\n✨ ATLAS update complete!")
        print(f"\nBackups saved to: {self.backup_dir}")
        print("\nNext steps:")
        print("1. Review any changes to core instructions")
        print("2. Test that your project still works as expected")
        print("3. Run: python .atlas/scripts/save_session.py -c \"Updated ATLAS framework\" -n \"Continue with latest features\"")
        
        return True


def main():
    """Run the updater"""
    updater = AtlasUpdater()
    success = updater.run_update()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()