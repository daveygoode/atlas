# MCP Integration - Context7 for Up-to-Date Documentation

## Overview

Atlas integrates with Model Context Protocol (MCP) servers, particularly context7, to maintain access to the latest documentation and technical resources. This ensures Atlas always works with current best practices and API specifications.

## Context7 MCP

Context7 is an MCP server that provides:
- Real-time access to official documentation
- Up-to-date API references
- Latest framework guides and best practices
- Current security advisories and patches

## Context7 MCP in Claude Code

When Context7 MCP is available in your Claude Code session, Atlas will automatically use it for documentation verification. No configuration needed - if the MCP tools are available, they will be used.

### 3. Atlas Integration Points

Atlas will use context7 MCP for:

1. **Documentation Queries**: Before implementing features, query latest docs
2. **API Verification**: Confirm current API endpoints and parameters
3. **Security Updates**: Check for latest security best practices
4. **Framework Changes**: Stay updated on framework evolution

## Usage in Atlas Workflow

### During Session Start

When resuming a session, Atlas should:
```python
# In resume_session.py, add documentation check
def check_documentation_updates(tech_stack):
    """Check for documentation updates via context7"""
    # Query context7 for latest updates on project's tech stack
    # Flag any significant changes since last session
```

### Before Implementation

Atlas workflow should include:
1. Query context7 for relevant documentation
2. Verify current best practices
3. Check for deprecations or breaking changes
4. Update SHORT_IMPORTANT_MEMORY.md with findings

### Documentation-Driven Development

Atlas follows these principles:
- **Verify First**: Always check current docs before implementing
- **Update Memory**: Store important findings in memory systems
- **Track Changes**: Log documentation updates in WORKING_LOG
- **Share Knowledge**: Document discoveries for team benefit

## Integration with Session Management

### Enhanced Save Session

```bash
python scripts/save_session.py \
  -c "Implemented feature X" \
  -n "Add feature Y" \
  -e '{"docs_checked": ["React 18 hooks", "Next.js 14 routing"], "api_changes": ["Deprecated endpoint /v1/users"]}'
```

### Documentation in Working Log

Working log entries should include:
```markdown
## Session: 2024-03-16 14:30:00

### Context
Implemented user authentication with JWT

### Documentation Consulted (via context7)
- JWT.io current best practices
- OWASP authentication guidelines 2024
- Framework security updates

### Important Findings
- New recommendation: Use refresh token rotation
- Deprecated: Simple JWT without expiry
```

## Best Practices

1. **Regular Checks**: Query documentation at session start
2. **Version Awareness**: Track framework/library versions
3. **Change Detection**: Note differences from previous implementation
4. **Team Communication**: Share documentation updates
5. **Memory Updates**: Keep SHORT_IMPORTANT_MEMORY.md current

## Example Workflow Integration

```python
# Atlas consciousness should include:
class AtlasDocumentationAwareness:
    def before_coding(self, feature):
        # 1. Check context7 for latest docs
        docs = query_context7(feature.tech_stack)
        
        # 2. Compare with stored knowledge
        changes = compare_with_memory(docs)
        
        # 3. Update understanding
        if changes:
            update_short_memory(changes)
            log_documentation_updates(changes)
        
        # 4. Proceed with current best practices
        return implement_with_latest_patterns(feature, docs)
```

## MCP Tools Available

When context7 is properly configured, Atlas has access to:
- `mcp__context7__search`: Search documentation
- `mcp__context7__get_doc`: Retrieve specific documentation
- `mcp__context7__check_updates`: Check for recent changes
- `mcp__context7__verify_api`: Verify API specifications

## Troubleshooting

### MCP Not Available in Claude Code
If MCP tools are not available in your session, Atlas will automatically use fallback strategies.

### Fallback Strategy
When MCP is unavailable:
1. Use web search for documentation
2. Rely on cached knowledge in memory systems
3. Flag uncertainty in implementation notes
4. Request manual documentation verification

## Summary

Context7 MCP integration ensures Atlas maintains current technical knowledge, preventing outdated implementations and security vulnerabilities. This documentation-first approach aligns with Atlas's commitment to engineering excellence through continuous learning.