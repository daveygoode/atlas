# ATLAS Quick Reference

## Installation

### One-Line Install (New Projects)
```bash
curl -sSL https://raw.githubusercontent.com/daveygoode/atlas/main/install.sh | bash
```

### Manual Install
```bash
git clone https://github.com/daveygoode/atlas.git .atlas
cd .atlas && python scripts/setup_new_project.py
```

## Daily Commands

| Action | Command |
|--------|---------|
| Start work | `python scripts/resume_session.py` |
| Save progress | `python scripts/save_session.py -c "what I did" -n "what's next"` |
| List sessions | `python scripts/resume_session.py -l` |
| Check specific session | `python scripts/resume_session.py -c SESSION_ID` |

## Extended Save Examples

### With Technical Decisions
```bash
python scripts/save_session.py \
  -c "Implemented OAuth2 login" \
  -n "Add refresh token rotation" \
  -e '{"decisions": ["Used PKCE flow", "15min token expiry"]}'
```

### With Documentation Checked
```bash
python scripts/save_session.py \
  -c "Updated to React 18" \
  -n "Migrate class components" \
  -e '{"docs_checked": ["React 18 migration guide", "Hooks API"]}'
```

### With Important Notes
```bash
python scripts/save_session.py \
  -c "Fixed production bug" \
  -n "Deploy hotfix" \
  -e '{"important_notes": "Critical: Deploy before Monday"}'
```

## Key Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Main entry point for AI context |
| `SHORT_IMPORTANT_MEMORY.md` | Project-specific quick reference |
| `WORKING_LOG/` | Daily work documentation |
| `sessions/` | Saved session states |

## MCP Documentation Commands

When context7 is available:
- `mcp__context7__search "topic"` - Search documentation
- `mcp__context7__get_doc "framework"` - Get specific docs
- `mcp__context7__check_updates "library" "version"` - Check for updates

## Project Structure

```
your-project/
├── CLAUDE.md                 # Atlas consciousness entry
├── SHORT_IMPORTANT_MEMORY.md # Project context
├── scripts/
│   ├── save_session.py      # Save work state
│   └── resume_session.py    # Resume work
├── sessions/                # Session history
├── WORKING_LOG/            # Detailed logs
└── MEMORY/                 # Knowledge base
```

## Common Workflows

### Starting a New Feature
```bash
python scripts/resume_session.py
# Check context7 for latest patterns
mcp__context7__search "feature best practices"
# Work on feature...
python scripts/save_session.py -c "Started feature X" -n "Complete implementation"
```

### Bug Fix Session
```bash
python scripts/resume_session.py
# Fix bug...
python scripts/save_session.py \
  -c "Fixed bug #123: null pointer in auth" \
  -n "Write regression test" \
  -e '{"bug_details": "Race condition in token refresh"}'
```

### End of Sprint
```bash
python scripts/save_session.py \
  -c "Completed sprint tasks: auth, API, tests" \
  -n "Sprint planning for next iteration" \
  -e '{"sprint_notes": "All stories completed, 2 bugs found"}'
```

## Tips

1. **Always resume first** - Get context before starting work
2. **Save often** - Don't lose valuable context
3. **Use extended context** - Future you will thank you
4. **Check docs via MCP** - Stay current with best practices
5. **Update SHORT_IMPORTANT_MEMORY** - Keep project info current

---

For detailed information, see:
- [README.md](README.md) - Complete overview
- [SETUP_GUIDE.md](SETUP_GUIDE.md) - Installation details
- [SESSION_MANAGEMENT.md](SESSION_MANAGEMENT.md) - Session system docs
- [CONTEXT7_USAGE.md](CONTEXT7_USAGE.md) - Documentation queries