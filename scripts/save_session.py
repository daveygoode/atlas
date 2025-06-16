#!/usr/bin/env python3
"""
Atlas Session Manager - Save Session
Integrates DevCycle session management with Atlas AI Agent framework
"""

import os
import sys
import json
import argparse
import subprocess
from datetime import datetime
from pathlib import Path


class AtlasSessionSaver:
    def __init__(self):
        # Detect if we're running from within .atlas or from project root
        script_path = Path(__file__).resolve()
        if '.atlas' in script_path.parts:
            # Running from .atlas/scripts/
            self.atlas_root = Path(__file__).parent.parent
            self.project_root = self.atlas_root.parent
        else:
            # Running from copied location (old structure)
            self.project_root = Path.cwd()
            self.atlas_root = self.project_root / ".atlas"
        
        self.working_log_dir = self.atlas_root / "WORKING_LOG"
        self.sessions_dir = self.atlas_root / "sessions"
        self.sessions_dir.mkdir(exist_ok=True)
        
        # Get current date components for working log
        now = datetime.now()
        self.year = now.strftime("%Y")
        self.month = now.strftime("%m-%b").lower()
        self.day = now.strftime("%d")
        
    def get_git_info(self):
        """Gather git repository information"""
        try:
            # Check if we're in a git repo
            subprocess.run(["git", "rev-parse", "--git-dir"], 
                         check=True, capture_output=True)
            
            # Get current branch
            branch = subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                text=True
            ).strip()
            
            # Get modified files
            modified_files = subprocess.check_output(
                ["git", "diff", "--name-only"],
                text=True
            ).strip().split('\n')
            
            # Get staged files
            staged_files = subprocess.check_output(
                ["git", "diff", "--cached", "--name-only"],
                text=True
            ).strip().split('\n')
            
            # Get last 5 commits
            commits = subprocess.check_output(
                ["git", "log", "--oneline", "-5"],
                text=True
            ).strip().split('\n')
            
            # Get git status summary
            status = subprocess.check_output(
                ["git", "status", "--short"],
                text=True
            ).strip()
            
            return {
                "branch": branch,
                "modified_files": [f for f in modified_files if f],
                "staged_files": [f for f in staged_files if f],
                "recent_commits": commits,
                "status_summary": status
            }
        except subprocess.CalledProcessError:
            return None
    
    def read_short_memory(self):
        """Read SHORT_IMPORTANT_MEMORY.md if it exists"""
        memory_file = self.atlas_root / "SHORT_IMPORTANT_MEMORY.md"
        if memory_file.exists():
            return memory_file.read_text(encoding='utf-8')
        return None
    
    def check_mcp_availability(self):
        """Check if MCP tools are available (context7 specifically)"""
        # In Claude Code, MCP availability is determined by the session
        # This is a placeholder that Atlas will use to check actual availability
        # during runtime by attempting to use the MCP tools
        return "Check during runtime"
    
    def create_working_log_entry(self, context, next_task):
        """Create entry in Atlas WORKING_LOG structure"""
        log_dir = self.working_log_dir / self.year / self.month
        log_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = log_dir / f"{self.day}.md"
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        entry = f"""
## Session: {timestamp}

### Context
{context}

### Next Task
{next_task}

### Session Details
- Saved at: {timestamp}
- Working Directory: {os.getcwd()}
- Python Version: {sys.version.split()[0]}

---
"""
        
        # Append to existing file or create new
        if log_file.exists():
            existing_content = log_file.read_text(encoding='utf-8')
            log_file.write_text(existing_content + "\n" + entry, encoding='utf-8')
        else:
            # Create file with header
            header = f"""# Working Log - {self.day} {self.month.split('-')[1].title()} {self.year}

> Atlas Engineering Session Log
> Professional Mode: Active

---
"""
            log_file.write_text(header + entry, encoding='utf-8')
    
    def save_session(self, context, next_task, extended_context=None):
        """Save current session state"""
        timestamp = datetime.now()
        session_id = timestamp.strftime("%Y%m%d_%H%M%S")
        
        # Gather all session data
        session_data = {
            "session_id": session_id,
            "timestamp": timestamp.isoformat(),
            "atlas_identity": "ATLAS - Adaptive Technical Learning and Architecture System",
            "context": context,
            "next_task": next_task,
            "extended_context": extended_context,
            "working_directory": os.getcwd(),
            "python_version": sys.version,
            "git_info": self.get_git_info(),
            "short_memory": self.read_short_memory(),
            "professional_mode": True,
            "mcp_available": self.check_mcp_availability(),
            "session_metadata": {
                "year": self.year,
                "month": self.month,
                "day": self.day,
                "user": os.getenv("USER", "unknown")
            }
        }
        
        # Save session file
        session_file = self.sessions_dir / f"Session_{session_id}.json"
        with open(session_file, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, indent=2, ensure_ascii=False)
        
        # Update LATEST.json
        latest_file = self.sessions_dir / "LATEST.json"
        with open(latest_file, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, indent=2, ensure_ascii=False)
        
        # Create working log entry
        self.create_working_log_entry(context, next_task)
        
        # Update SHORT_IMPORTANT_MEMORY if needed
        if extended_context and "important_notes" in extended_context:
            self.update_short_memory(extended_context["important_notes"])
        
        return session_file, session_data
    
    def update_short_memory(self, new_notes):
        """Append important notes to SHORT_IMPORTANT_MEMORY.md"""
        memory_file = self.atlas_root / "SHORT_IMPORTANT_MEMORY.md"
        
        if memory_file.exists():
            content = memory_file.read_text(encoding='utf-8')
            # Find the Critical Notes section
            if "## Critical Notes" in content:
                # Append to existing notes
                parts = content.split("## Critical Notes")
                updated_content = (
                    parts[0] + 
                    "## Critical Notes" + 
                    parts[1].rstrip() + 
                    f"\n- {datetime.now().strftime('%Y-%m-%d')}: {new_notes}\n"
                )
                memory_file.write_text(updated_content, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(
        description="Atlas Session Manager - Save current development session",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python save_session.py -c "Implemented user authentication" -n "Add password reset"
  python save_session.py -c "Fixed API bugs" -n "Write tests" -e '{"decisions": ["Use JWT tokens"]}'
        """
    )
    
    parser.add_argument('-c', '--context', required=True,
                       help='What was accomplished in this session')
    parser.add_argument('-n', '--next', required=True, dest='next_task',
                       help='What needs to be done next')
    parser.add_argument('-e', '--extended', type=str,
                       help='Extended context as JSON (technical decisions, important notes)')
    
    args = parser.parse_args()
    
    # Parse extended context if provided
    extended_context = None
    if args.extended:
        try:
            extended_context = json.loads(args.extended)
        except json.JSONDecodeError:
            print("⚠️  Warning: Invalid JSON in extended context, ignoring")
    
    # Save session
    saver = AtlasSessionSaver()
    session_file, session_data = saver.save_session(
        args.context, 
        args.next_task, 
        extended_context
    )
    
    # Display confirmation
    print(f"""
✅ Atlas Session Saved Successfully!

📁 Session ID: {session_data['session_id']}
📂 Saved to: {session_file.relative_to(saver.atlas_root)}
📝 Working Log: WORKING_LOG/{saver.year}/{saver.month}/{saver.day}.md

Context: {args.context}
Next Task: {args.next_task}

Professional Mode: Active
Identity: ATLAS - Engineering Excellence Through Experience

To resume this session:
  python scripts/resume_session.py
""")
    
    # Show git status if available
    if session_data['git_info']:
        print(f"\nGit Branch: {session_data['git_info']['branch']}")
        if session_data['git_info']['modified_files']:
            print(f"Modified Files: {len(session_data['git_info']['modified_files'])}")


if __name__ == "__main__":
    main()