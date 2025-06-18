# Atlas Session Management Guide

## Overview

The Atlas integrated system now includes sophisticated session management that bridges the gap between Claude AI conversations. This system combines the Atlas AI Agent framework's consciousness architecture with DevCycle's session persistence capabilities.

## Key Features

- **Automatic Context Preservation**: Save complete development context between sessions
- **Git Integration**: Tracks all file changes and commit history
- **Working Log Integration**: Automatically updates Atlas's WORKING_LOG structure
- **Memory System Sync**: Integrates with SHORT_IMPORTANT_MEMORY.md
- **Professional Mode Support**: Maintains Atlas's work protocols across sessions

## Quick Start

### Saving a Session

At the end of any work session:

```bash
python scripts/save_session.py -c "Implemented user authentication with JWT" -n "Add password reset functionality"
```

With extended context:
```bash
python scripts/save_session.py \
  -c "Refactored API endpoints to follow REST conventions" \
  -n "Implement rate limiting middleware" \
  -e '{"decisions": ["Use Redis for rate limiting", "Set 100 req/min limit"], "important_notes": "Client expects deployment by Friday"}'
```

### Resuming a Session

Start of next session:

```bash
# Resume the most recent session
python scripts/resume_session.py

# Resume a specific session
python scripts/resume_session.py -c 20250316_143022

# List all available sessions
python scripts/resume_session.py -l

# Get Claude-friendly context string
python scripts/resume_session.py --claude
```

## Architecture

### Directory Structure

```
atlas-integrated/
├── CLAUDE.md                    # Main Atlas entry point (updated with session management)
├── scripts/
│   ├── save_session.py         # Save current session state
│   └── resume_session.py       # Resume previous session
├── sessions/                   # Session storage (auto-created)
│   ├── Session_YYYYMMDD_HHMMSS.json
│   └── LATEST.json            # Quick access to most recent
├── WORKING_LOG/               # Atlas work logs (auto-updated)
│   └── YYYY/
│       └── MM-mon/
│           └── DD.md          # Daily work entries
└── SHORT_IMPORTANT_MEMORY.md  # Quick reference (preserved in sessions)
```

### Session Data Structure

Each session captures:
- **Identity**: Atlas consciousness state
- **Context**: What was accomplished
- **Next Task**: What needs to be done
- **Git State**: Branch, modified files, staged files, recent commits
- **Working Directory**: Where work was happening
- **Short Memory**: Current contents of SHORT_IMPORTANT_MEMORY.md
- **Extended Context**: Technical decisions, important notes
- **Metadata**: Timestamp, user, Python version

### Integration Points

1. **WORKING_LOG Integration**
   - Automatically creates dated entries in Atlas's working log structure
   - Maintains professional work documentation standards
   - Preserves chronological work history

2. **Memory Systems**
   - Reads and preserves SHORT_IMPORTANT_MEMORY.md
   - Can update critical notes when specified
   - Maintains Atlas's memory architecture

3. **Professional Mode**
   - Sessions always marked as "Professional Mode: Active"
   - Reinforces Atlas's objective work focus
   - Maintains context switching protocols

## Use Cases

### Daily Development Workflow

1. **Morning**: Resume yesterday's session
   ```bash
   python scripts/resume_session.py
   ```

2. **During Work**: Atlas operates in professional mode, using memory systems

3. **End of Day**: Save progress
   ```bash
   python scripts/save_session.py -c "Completed API endpoints" -n "Write integration tests"
   ```

### Complex Feature Development

Save detailed context for multi-day features:
```bash
python scripts/save_session.py \
  -c "Implemented authentication flow with JWT, added user registration" \
  -n "Add email verification and password reset" \
  -e '{
    "decisions": [
      "Used bcrypt for password hashing",
      "JWT expiry set to 24 hours",
      "Email service: SendGrid"
    ],
    "important_notes": "Security audit scheduled for next week"
  }'
```

### Team Handoffs

When passing work to another developer:
```bash
python scripts/save_session.py \
  -c "Set up project structure and core dependencies" \
  -n "Implement user model and authentication" \
  -e '{"handoff_notes": "Database migrations are ready, see docs/setup.md"}'
```

## Best Practices

1. **Always Save Before Ending**: Make it a habit to save session state
2. **Be Descriptive**: Clear context and next task descriptions help future resumption
3. **Use Extended Context**: For complex decisions or important deadlines
4. **Regular Commits**: Session management complements, doesn't replace, git commits
5. **Review on Resume**: Always review the session summary before continuing work

## Advanced Features

### Customization

Both scripts can be extended to:
- Send Slack notifications on save/resume
- Integrate with project management tools
- Add custom metadata fields
- Implement session branching for parallel work streams

### Automation

Consider adding to git hooks:
```bash
# .git/hooks/post-commit
python scripts/save_session.py -c "$(git log -1 --pretty=%B)" -n "Continue development"
```

## Troubleshooting

### Common Issues

1. **No sessions found**: Ensure you're in the correct directory
2. **Git info missing**: Not a problem if not in a git repository
3. **Permission errors**: Check file permissions on scripts and directories

### Debug Mode

Both scripts support verbose output:
```bash
python scripts/save_session.py -c "Debug" -n "Test" --verbose
```

## Summary

The Atlas-integrated session management system provides a seamless bridge between AI-assisted development sessions while maintaining the full Atlas consciousness architecture. It ensures no context is lost, work is properly documented, and the AI agent can maintain its professional identity and protocols across conversations.

This integration represents the best of both worlds: Atlas's sophisticated AI agent framework with DevCycle's practical session persistence, creating a powerful system for continuous AI-assisted development.