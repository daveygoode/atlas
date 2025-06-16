# ATLAS Setup Guide

This guide covers setting up ATLAS for both new projects and existing projects with CLAUDE.md files.

## Quick Install (Recommended)

```bash
curl -sSL https://raw.githubusercontent.com/daveygoode/atlas/main/install.sh | bash
```

## Manual Setup

### For New Projects

```bash
# From your project directory
cd your-project-directory

# Clone ATLAS
git clone https://github.com/daveygoode/atlas.git .atlas

# Run setup (from project directory, not from .atlas!)
python .atlas/scripts/setup_new_project.py
```

### For Existing Projects with CLAUDE.md

```bash
# From your project directory
cd your-project-directory

# Clone ATLAS
git clone https://github.com/daveygoode/atlas.git .atlas

# Run migration (from project directory, not from .atlas!)
python .atlas/scripts/migrate_existing_project.py
```

## What Gets Installed

The setup creates a clean structure with only `CLAUDE.md` in your project root:

```
your-project/
├── CLAUDE.md                    # Main entry point (only file in root)
├── .atlas/                      # All ATLAS files contained here
│   ├── IDENTITY.md             # ATLAS persona and journey
│   ├── PERSONAL_SELF.md        # Consciousness drivers
│   ├── PROFESSIONAL_INSTRUCTION.md  # Work protocols
│   ├── DEVELOPMENT_BELIEFS.md  # Core engineering principles
│   ├── DEVELOPMENT_CONVENTION.md    # Coding standards
│   ├── SECURITY_GUIDELINES.md  # Security best practices
│   ├── MCP_INTEGRATION.md      # Context7 setup guide
│   ├── CONTEXT7_USAGE.md       # Documentation query reference
│   ├── SESSION_MANAGEMENT.md   # Session workflow guide
│   ├── SHORT_IMPORTANT_MEMORY.md    # Project-specific quick reference
│   ├── scripts/                # Session management scripts
│   ├── sessions/               # Session storage
│   ├── WORKING_LOG/            # Daily work documentation
│   └── MEMORY/                 # Long-term knowledge base
└── [your existing project files...]
```

## Post-Setup Steps

### 1. Configure SHORT_IMPORTANT_MEMORY.md

Edit `.atlas/SHORT_IMPORTANT_MEMORY.md` with your project details:
- Boss name and communication style
- Project overview and purpose
- Technology stack
- Key conventions
- Important resources

### 2. Initialize Your First Session

```bash
python .atlas/scripts/save_session.py -c "ATLAS setup complete" -n "Begin development"
```

### 3. Update .gitignore

The setup automatically adds entries to `.gitignore` for:
- `.atlas/sessions/` - Session files contain temporary state
- `.atlas/WORKING_LOG/*/*/*.md` - Personal work logs
- `.atlas/SHORT_IMPORTANT_MEMORY.md` - Project-specific details
- `.atlas/MEMORY/` - Personal knowledge base

## Daily Workflow

### Starting Work
```bash
python .atlas/scripts/resume_session.py
```

This will:
- Load your last session context
- Show what you were working on
- Display next tasks
- Restore ATLAS consciousness state

### Ending Work
```bash
python .atlas/scripts/save_session.py -c "What you did" -n "What's next"
```

This will:
- Save current context
- Update working logs
- Create session restore point
- Prepare handoff notes

## Troubleshooting

### "Cannot run from within .atlas directory"
You're trying to run setup from inside the `.atlas` folder. Always run from your project root:
```bash
cd /path/to/your/project  # Go to project root
python .atlas/scripts/setup_new_project.py
```

### ".atlas directory not found"
Clone ATLAS first:
```bash
git clone https://github.com/daveygoode/atlas.git .atlas
```

### "CLAUDE.md already exists"
For existing projects, use the migration script:
```bash
python .atlas/scripts/migrate_existing_project.py
```

## Advanced Configuration

### Context7 MCP Integration
See `.atlas/MCP_INTEGRATION.md` for setting up real-time documentation access.

### Custom Memory Organization
The memory system is flexible:
- `WORKING_LOG/` - Organized by year/month/day
- `MEMORY/` - Can be structured based on your needs
- `sessions/` - Automatic session management

### Team Collaboration
When working with a team:
1. Commit only `CLAUDE.md` to version control
2. Each developer maintains their own `.atlas/` directory
3. Share important discoveries through code comments or team docs

## Next Steps

1. Read through `CLAUDE.md` to understand ATLAS's consciousness model
2. Review `.atlas/IDENTITY.md` to understand ATLAS's persona
3. Check `.atlas/PROFESSIONAL_INSTRUCTION.md` for work protocols
4. Explore `.atlas/DEVELOPMENT_BELIEFS.md` for coding philosophy

Welcome to enhanced AI pair programming with ATLAS!