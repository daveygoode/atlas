# Context7 MCP Usage Guide for Atlas

## Quick Reference

### When to Use Context7

1. **Before Starting Any Implementation**
   ```
   mcp__context7__search "React hooks best practices 2025"
   mcp__context7__search "JWT implementation security"
   ```

2. **When Using a New Library/Framework**
   ```
   mcp__context7__get_doc "nextjs app router"
   mcp__context7__get_doc "prisma transactions"
   ```

3. **Checking for Updates**
   ```
   mcp__context7__check_updates "react" "18.2.0"
   mcp__context7__check_updates "nodejs" "20.0.0"
   ```

4. **API Verification**
   ```
   mcp__context7__verify_api "stripe payment intents"
   mcp__context7__verify_api "openai chat completions"
   ```

## Integration with Atlas Workflow

### 1. Session Start Protocol

When resuming a session:
```python
# Check documentation for tech stack mentioned in session
python scripts/resume_session.py

# If session mentions React/Next.js work:
mcp__context7__check_updates "react" "current_version"
mcp__context7__check_updates "nextjs" "current_version"
```

### 2. Before Writing Code

Always verify current patterns:
```
# Example: Before implementing authentication
mcp__context7__search "jwt best practices 2025"
mcp__context7__search "oauth2 implementation guide"
mcp__context7__get_doc "passport.js strategies"
```

### 3. Working Log Documentation

Include findings in your working log:
```markdown
## Session: 2025-03-16 14:30:00

### Documentation Findings (via context7)
- JWT: Now recommended to use refresh token rotation
- React: useId() hook now preferred over manual ID generation
- Security: CSP headers should include 'strict-dynamic' for scripts
```

### 4. Updating SHORT_IMPORTANT_MEMORY

When you discover important changes:
```markdown
## Critical Notes
- 2025-03-16: React 18.3 deprecates ReactDOM.render, use createRoot
- 2025-03-16: Stripe API v2025-03-15 changes payment_intent flow
```

## Fallback When Context7 Unavailable

If MCP tools are not accessible:

1. **Use WebSearch**
   ```
   WebSearch "React 18 best practices site:react.dev"
   WebSearch "JWT implementation 2025 site:jwt.io"
   ```

2. **Verify with Official Docs**
   ```
   WebFetch https://react.dev/reference/react "current hooks api"
   WebFetch https://nextjs.org/docs "app router patterns"
   ```

3. **Document Uncertainty**
   In your code comments and logs:
   ```javascript
   // Note: Unable to verify via context7, based on last known best practices
   // TODO: Verify this implementation when MCP available
   ```

## Common Documentation Queries

### Frontend Frameworks
```
mcp__context7__search "react server components"
mcp__context7__search "vue 3 composition api"
mcp__context7__search "angular signals"
```

### Backend Patterns
```
mcp__context7__search "nodejs clustering best practices"
mcp__context7__search "express security middleware 2025"
mcp__context7__search "fastify vs express performance"
```

### Security
```
mcp__context7__search "owasp top 10 2025"
mcp__context7__search "jwt security vulnerabilities"
mcp__context7__search "cors configuration best practices"
```

### Databases
```
mcp__context7__search "postgresql jsonb performance"
mcp__context7__search "mongodb indexes best practices"
mcp__context7__search "redis caching strategies"
```

## Documentation-Driven Development Flow

1. **Query First**: Before implementing any feature
2. **Verify Assumptions**: Don't rely on outdated knowledge
3. **Document Findings**: In working logs and memory
4. **Share Knowledge**: Update team docs with discoveries
5. **Flag Uncertainties**: When verification isn't possible

## Example: Complete Feature Implementation

```bash
# 1. Start session
python scripts/resume_session.py

# 2. Check for updates
mcp__context7__check_updates "react" "18.2.0"

# 3. Research best practices
mcp__context7__search "react form validation 2025"
mcp__context7__get_doc "react-hook-form v7"

# 4. Implement with current patterns
# ... coding ...

# 5. Save session with documentation notes
python scripts/save_session.py \
  -c "Implemented form validation using react-hook-form v7" \
  -n "Add unit tests for validation logic" \
  -e '{"docs_checked": ["react-hook-form v7", "zod schema validation"], "patterns_used": ["Controller pattern for MUI integration"]}'
```

## Remember

Atlas's commitment to engineering excellence includes staying current with best practices. Context7 MCP is a tool to maintain this currency, ensuring every implementation reflects the latest standards and security requirements.