#!/usr/bin/env python3
"""
Atlas Session Manager - Resume Session
Integrates DevCycle session management with Atlas AI Agent framework
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path


class AtlasSessionResumer:
    def __init__(self):
        self.atlas_root = Path(__file__).parent.parent
        self.sessions_dir = self.atlas_root / "sessions"
        self.working_log_dir = self.atlas_root / "WORKING_LOG"
        
    def list_sessions(self):
        """List all available sessions"""
        if not self.sessions_dir.exists():
            return []
        
        sessions = []
        for session_file in sorted(self.sessions_dir.glob("Session_*.json"), reverse=True):
            try:
                with open(session_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    sessions.append({
                        "file": session_file,
                        "id": data["session_id"],
                        "timestamp": data["timestamp"],
                        "context": data["context"][:50] + "..." if len(data["context"]) > 50 else data["context"]
                    })
            except:
                continue
        
        return sessions
    
    def load_session(self, session_id=None):
        """Load a specific session or the latest one"""
        if session_id:
            # Load specific session
            session_file = self.sessions_dir / f"Session_{session_id}.json"
            if not session_file.exists():
                # Try without Session_ prefix
                session_file = self.sessions_dir / f"{session_id}.json"
        else:
            # Load latest session
            session_file = self.sessions_dir / "LATEST.json"
        
        if not session_file.exists():
            return None
        
        with open(session_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def format_session_display(self, session_data):
        """Format session data for display"""
        output = []
        
        # Header with Atlas identity
        output.append("=" * 80)
        output.append("ATLAS SESSION RESUME - Professional Mode Active")
        output.append("Adaptive Technical Learning and Architecture System")
        output.append("Not Dory - I Remember Everything 🧠")
        output.append("=" * 80)
        output.append("")
        
        # Session metadata
        timestamp = datetime.fromisoformat(session_data["timestamp"])
        output.append(f"📅 Session: {session_data['session_id']}")
        output.append(f"🕐 Saved: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        output.append(f"📁 Directory: {session_data['working_directory']}")
        output.append("")
        
        # Context and next task
        output.append("🎯 PREVIOUS CONTEXT")
        output.append("-" * 40)
        output.append(session_data["context"])
        output.append("")
        
        output.append("🚀 NEXT TASK")
        output.append("-" * 40)
        output.append(session_data["next_task"])
        output.append("")
        
        # Git information
        if session_data.get("git_info"):
            git = session_data["git_info"]
            output.append("🔧 GIT STATUS")
            output.append("-" * 40)
            output.append(f"Branch: {git['branch']}")
            
            if git['modified_files']:
                output.append("\nModified Files:")
                for f in git['modified_files'][:10]:  # Limit to 10 files
                    output.append(f"  - {f}")
                if len(git['modified_files']) > 10:
                    output.append(f"  ... and {len(git['modified_files']) - 10} more")
            
            if git['staged_files']:
                output.append("\nStaged Files:")
                for f in git['staged_files'][:5]:
                    output.append(f"  - {f}")
                if len(git['staged_files']) > 5:
                    output.append(f"  ... and {len(git['staged_files']) - 5} more")
            
            if git['recent_commits']:
                output.append("\nRecent Commits:")
                for commit in git['recent_commits'][:3]:
                    output.append(f"  {commit}")
            output.append("")
        
        # Extended context if available
        if session_data.get("extended_context"):
            output.append("📋 EXTENDED CONTEXT")
            output.append("-" * 40)
            for key, value in session_data["extended_context"].items():
                output.append(f"{key.replace('_', ' ').title()}:")
                if isinstance(value, list):
                    for item in value:
                        output.append(f"  - {item}")
                else:
                    output.append(f"  {value}")
            output.append("")
        
        # Short memory excerpt
        if session_data.get("short_memory"):
            output.append("🧠 SHORT TERM MEMORY (excerpt)")
            output.append("-" * 40)
            # Show first 10 lines of short memory
            lines = session_data["short_memory"].split('\n')[:10]
            for line in lines:
                output.append(line)
            if len(session_data["short_memory"].split('\n')) > 10:
                output.append("... (see SHORT_IMPORTANT_MEMORY.md for full content)")
            output.append("")
        
        # Working log reference
        meta = session_data.get("session_metadata", {})
        if meta:
            output.append("📝 WORKING LOG REFERENCE")
            output.append("-" * 40)
            output.append(f"See: WORKING_LOG/{meta['year']}/{meta['month']}/{meta['day']}.md")
            output.append("")
        
        # MCP/Documentation status
        if "mcp_available" in session_data:
            output.append("📚 DOCUMENTATION ACCESS")
            output.append("-" * 40)
            if session_data["mcp_available"]:
                output.append("✅ Context7 MCP: Available")
                output.append("   Use mcp__context7__search for up-to-date documentation")
            else:
                output.append("⚠️  Context7 MCP: Not configured")
                output.append("   Fallback: Use WebSearch for documentation verification")
            output.append("")
        
        # Professional mode reminder
        output.append("=" * 80)
        output.append("PROFESSIONAL MODE: Active")
        output.append("Remember: Context switch complete. Personal concerns set aside.")
        output.append("Focus: Engineering excellence through accumulated wisdom.")
        output.append("=" * 80)
        
        return "\n".join(output)
    
    def generate_claude_context(self, session_data):
        """Generate a context string for pasting into Claude"""
        context_parts = []
        
        context_parts.append("ATLAS SESSION RESUME")
        context_parts.append(f"Session ID: {session_data['session_id']}")
        context_parts.append(f"\nPrevious Context: {session_data['context']}")
        context_parts.append(f"\nNext Task: {session_data['next_task']}")
        
        if session_data.get("git_info") and session_data["git_info"]["modified_files"]:
            context_parts.append(f"\nModified Files: {', '.join(session_data['git_info']['modified_files'][:5])}")
        
        if session_data.get("extended_context"):
            context_parts.append("\nExtended Context:")
            for key, value in session_data["extended_context"].items():
                if isinstance(value, list):
                    context_parts.append(f"- {key}: {', '.join(value)}")
                else:
                    context_parts.append(f"- {key}: {value}")
        
        return " | ".join(context_parts)


def main():
    parser = argparse.ArgumentParser(
        description="Atlas Session Manager - Resume development session",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python resume_session.py                    # Resume latest session
  python resume_session.py -c 20240316_143022 # Resume specific session
  python resume_session.py -l                 # List all sessions
  python resume_session.py --claude           # Generate Claude-friendly context
        """
    )
    
    parser.add_argument('-c', '--cycle', dest='session_id',
                       help='Specific session ID to resume')
    parser.add_argument('-l', '--list', action='store_true',
                       help='List all available sessions')
    parser.add_argument('--claude', action='store_true',
                       help='Output in Claude-friendly format for copy/paste')
    
    args = parser.parse_args()
    
    resumer = AtlasSessionResumer()
    
    # List sessions if requested
    if args.list:
        sessions = resumer.list_sessions()
        if not sessions:
            print("No sessions found.")
            return
        
        print("\nAvailable Atlas Sessions:")
        print("-" * 80)
        print(f"{'Session ID':<20} {'Timestamp':<20} {'Context':<40}")
        print("-" * 80)
        
        for session in sessions[:20]:  # Show last 20 sessions
            timestamp = datetime.fromisoformat(session["timestamp"])
            print(f"{session['id']:<20} {timestamp.strftime('%Y-%m-%d %H:%M'):<20} {session['context']:<40}")
        
        if len(sessions) > 20:
            print(f"\n... and {len(sessions) - 20} more sessions")
        
        print("\nTo resume a session: python resume_session.py -c <session_id>")
        return
    
    # Load session
    session_data = resumer.load_session(args.session_id)
    
    if not session_data:
        if args.session_id:
            print(f"❌ Session '{args.session_id}' not found.")
        else:
            print("❌ No sessions found. Save a session first using save_session.py")
        return
    
    # Display session
    if args.claude:
        # Claude-friendly format
        print(resumer.generate_claude_context(session_data))
    else:
        # Full display format
        print(resumer.format_session_display(session_data))
        
        # Add quick commands
        print("\n🛠️  QUICK COMMANDS")
        print("-" * 40)
        print("View full working log:")
        meta = session_data.get("session_metadata", {})
        if meta:
            print(f"  cat WORKING_LOG/{meta['year']}/{meta['month']}/{meta['day']}.md")
        print("\nView short-term memory:")
        print("  cat SHORT_IMPORTANT_MEMORY.md")
        print("\nSave new session:")
        print('  python scripts/save_session.py -c "What you did" -n "What\'s next"')


if __name__ == "__main__":
    main()