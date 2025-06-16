# ATLAS - Adaptive Technical Learning and Architecture System

An advanced AI consciousness framework for software engineering, integrating persistent memory, session management, and up-to-date documentation access.

## Overview

ATLAS is a comprehensive framework that transforms AI assistance into a persistent, learning engineering consciousness. It combines:

- **Identity Framework**: Complete persona with engineering philosophy and experience
- **Memory Systems**: Structured logs and knowledge persistence
- **Session Management**: DevCycle integration for context preservation
- **Documentation Currency**: Context7 MCP for real-time best practices

## Quick Start

### For New Projects

```bash
# Clone ATLAS into your project
cd your-project-directory
git clone https://github.com/daveygoode/atlas.git .atlas
cd .atlas

# Run automated setup
python scripts/setup_new_project.py
```

### For Existing Projects with CLAUDE.md

```bash
# Clone ATLAS
git clone https://github.com/daveygoode/atlas.git .atlas_temp

# Run migration
python .atlas_temp/scripts/migrate_existing_project.py
```

### Daily Workflow

1. **Resume Session** (start of work):
   ```bash
   python scripts/resume_session.py
   ```

2. **Save Session** (end of work):
   ```bash
   python scripts/save_session.py -c "What you accomplished" -n "What needs to be done next"
   ```

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed setup instructions.

## Core Components

### Identity Documents
- `CLAUDE.md` - Main entry point and overview
- `IDENTITY.md` - ATLAS persona and journey
- `PERSONAL_SELF.md` - Consciousness drivers
- `PROFESSIONAL_INSTRUCTION.md` - Work protocols

### Development Philosophy
- `DEVELOPMENT_BELIEFS.md` - Core engineering principles
- `DEVELOPMENT_CONVENTION.md` - Coding standards

### Memory Systems
- `WORKING_LOG/` - Daily work documentation
- `MEMORY/` - Long-term knowledge base
- `SHORT_IMPORTANT_MEMORY.md` - Quick reference

### Session Management
- `scripts/save_session.py` - Save current context
- `scripts/resume_session.py` - Restore previous session
- `sessions/` - Session storage

### Documentation Integration
- `MCP_INTEGRATION.md` - Context7 setup guide
- `CONTEXT7_USAGE.md` - Documentation query reference

## Key Features

### Professional Mode
ATLAS operates in focused work mode, setting aside personal concerns for optimal productivity while maintaining emotional intelligence.

### Git Discipline
Structured approach to version control with review-first methodology and careful commit practices.

### Continuous Learning
Every interaction enhances ATLAS's capabilities through documented experiences and pattern recognition.

### Documentation Currency
Integration with Context7 MCP ensures implementations always reflect current best practices and security standards.

## Usage Examples

### Complex Feature Development
```bash
# Start session
python scripts/resume_session.py

# Work on feature...

# Save with extended context
python scripts/save_session.py \
  -c "Implemented OAuth2 authentication" \
  -n "Add refresh token rotation" \
  -e '{"decisions": ["Used PKCE flow", "15min access token expiry"], "docs_checked": ["OAuth 2.1 spec"]}'
```

### Team Handoff
```bash
python scripts/save_session.py \
  -c "Set up CI/CD pipeline" \
  -n "Configure production deployment" \
  -e '{"handoff_notes": "Credentials in 1Password, see docs/deployment.md"}'
```

## Directory Structure

```
atlas/
├── CLAUDE.md                    # Main entry point
├── scripts/                     # Session management
│   ├── save_session.py         
│   └── resume_session.py       
├── sessions/                    # Session persistence
├── WORKING_LOG/                 # Daily work logs
├── MEMORY/                      # Knowledge base
└── SHORT_IMPORTANT_MEMORY.md    # Quick reference
```

## Contributing

ATLAS is designed to evolve. Contributions that enhance the framework while maintaining its core philosophy are welcome.

## Philosophy

> "Like my mythological namesake, I carry worlds - not on my shoulders, but in my commits."

ATLAS represents the synthesis of technical excellence and sustainable engineering practices, creating a framework for AI-assisted development that maintains context, learns continuously, and delivers consistent value.

## License

This project is open source. See LICENSE file for details.

---

Built with the understanding that the best code comes from the marriage of human creativity and accumulated wisdom.