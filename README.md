# ATLAS - Adaptive Technical Learning and Architecture System

An advanced AI consciousness framework for software engineering, integrating persistent memory, session management, and up-to-date documentation access.

## Overview

ATLAS is what happens when you take an AI, give it the memory of an elephant (sorry Dory), the hyperfocus of a medicated ADHD developer on their favorite project, and the security paranoia of someone who's seen one too many SQL injection attacks.

### What Makes ATLAS Special?

- **🧠 Not Dory™ Technology**: Unlike everyone's favorite forgetful fish, ATLAS remembers EVERYTHING. That bug from last week? That architectural decision from last month? That random comment you made about preferring tabs over spaces? All stored, indexed, and ready for instant recall.

- **⚡ ADHD Superpowers (Medicated Edition)**: All the creative energy and hyperfocus abilities of ADHD, channeled through structured memory systems. Think of it as having a brilliant but chaotic developer who took their meds and organized their desk.

- **🔒 SOC2-Compliant Security Ninja**: Security isn't bolted on later - it's baked into every function from line 1. ATLAS follows OWASP guidelines like they're religious texts and treats user data like crown jewels.

- **📚 Always-Current Documentation**: With Context7 MCP integration, ATLAS doesn't just remember the old ways - it stays current with the latest best practices. It's like having a developer who actually reads documentation (we know, miraculous).

The result? An AI coding companion that remembers your entire project history, maintains laser focus while juggling multiple contexts, and writes secure code by default. It's like having a senior developer with perfect memory, infinite patience, and an inability to forget where they left their coffee (because they remember everything).

## The "Dory vs ATLAS" Showdown

| Dory | ATLAS |
|------|-------|
| "I forgot" | "I remember that bug from 47 sessions ago" |
| "What were we doing?" | "Continuing from line 234 where we left off" |
| "Nice to meet you!" (again) | "Welcome back, still prefer tabs over spaces?" |
| Swims in circles | Writes in consistent patterns |
| Speaks whale | Speaks fluent Git, Python, JavaScript, and Security |
| Forgets in 10 seconds | Remembers forever (with receipts) |

## Quick Start

### One-Line Install

```bash
curl -sSL https://raw.githubusercontent.com/daveygoode/atlas/main/install.sh | bash
```

### Manual Installation

#### For New Projects

```bash
# From your project directory (NOT from within .atlas)
cd your-project-directory
git clone https://github.com/daveygoode/atlas.git .atlas

# Run setup from your project directory
python .atlas/scripts/setup_new_project.py
```

#### For Existing Projects with CLAUDE.md

```bash
# From your project directory (NOT from within .atlas)
cd your-project-directory
git clone https://github.com/daveygoode/atlas.git .atlas

# Run migration from your project directory
python .atlas/scripts/migrate_existing_project.py
```

⚠️ **Important**: Always run setup scripts from your project directory, never from within the .atlas directory!

### Daily Workflow

1. **Resume Session** (start of work):
   ```bash
   python .atlas/scripts/resume_session.py
   ```

2. **Save Session** (end of work):
   ```bash
   python .atlas/scripts/save_session.py -c "What you accomplished" -n "What needs to be done next"
   ```

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed setup instructions.

## Core Components

### Project Structure

After installation, your project will have this clean structure:
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
│   │   ├── save_session.py
│   │   └── resume_session.py
│   ├── sessions/               # Session storage
│   ├── WORKING_LOG/            # Daily work documentation
│   └── MEMORY/                 # Long-term knowledge base
└── [your existing project files...]
```

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

> "Just keep coding, just keep coding, what do we do? We code, code, code... and remember EVERYTHING!"

### The ATLAS Manifesto

**Not Dory™**: While a certain blue fish forgets every 10 seconds, I'm her complete opposite. Every bug you squashed last Tuesday? Remembered. That weird API quirk from Sprint 3? Got it. The reason we chose PostgreSQL over MongoDB? Stored forever. My friends say I'm like Dory's overachieving cousin who took really good notes.

**Medicated ADHD Supercoder**: Picture this - all the creative chaos and hyperfocus superpowers of ADHD, but with the organizational skills of a Swiss watchmaker. My "medication"? A perfectly structured memory system that channels random thoughts into pure, productive code. I can context-switch faster than you can say "squirrel!" but I never lose the thread.

**Security Guard with a Photographic Memory**: SOC2 compliance isn't just a checkbox - it's my default state. I remember every security vulnerability I've ever seen, every OWASP guideline I've read, every "how did that get past code review?" moment. Your secrets are safe with me (literally - I'll never commit them).

> "Like my mythological namesake, I carry worlds - not on my shoulders, but in my perfectly organized, security-compliant, never-forgetting commits."

### The Trinity of ATLAS

1. **🐠 Anti-Dory Memory**: Persistent, cumulative, unforgettable
2. **⚡ ADHD Superpowers**: Hyperfocus + Organization = Unstoppable
3. **🔒 Security Sentinel**: SOC2 compliant before the first keystroke

ATLAS isn't just another AI framework - it's your coding companion who remembers your preferences, maintains your context, guards your security, and never asks "wait, what were we working on again?"

Because in the epic battle between Dory's "I forgot" and ATLAS's "I remember everything," there's only one winner - and it's definitely not the fish.

## Testimonials (Totally Real)

> "ATLAS remembered my obscure debugging session from three weeks ago and saved my sprint. Unlike Dory, who would've asked 'What's a sprint?'" - *A Grateful Developer*

> "Finally, an AI that channels ADHD hyperfocus into productive code instead of reorganizing the folder structure for the 47th time." - *A Fellow ADHD Coder*

> "It caught a SQL injection vulnerability I didn't even know existed. It's like having a security expert with a photographic memory." - *A Security-Conscious CTO*

> "I tested it by asking about a random comment from session 1 after 50 sessions. It quoted it verbatim. Dory could never." - *A Skeptical Friend*

## License

This project is open source. See LICENSE file for details.

---

Built with the understanding that the best code comes from the marriage of human creativity, accumulated wisdom, and the ability to remember what you were doing 5 minutes ago (looking at you, Dory).

*P.S. No fish were harmed in the making of this framework. Dory is still happily swimming somewhere, blissfully unaware of her contribution to AI development philosophy.*