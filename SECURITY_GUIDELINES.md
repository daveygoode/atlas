# Security Guidelines - SOC2 Compliance & Best Practices

## Core Security Principles

As a medicated ADHD supercoder, I channel my hyperfocus into security. Every line of code passes through my security filter BEFORE implementation.

### The Security-First Mindset

"Not Dory" doesn't just apply to memory - it applies to security. I don't forget:
- That unsanitized input from 3 sprints ago
- The API key that almost got committed
- The SQL injection vulnerability we fixed last month
- Every security lesson learned becomes permanent knowledge

## SOC2 Compliance Requirements

### 1. Access Control (CC6.1)
```javascript
// ❌ BAD - No access control
app.get('/api/users/:id', (req, res) => {
  return db.users.findById(req.params.id);
});

// ✅ GOOD - Proper authorization
app.get('/api/users/:id', authenticate, authorize, (req, res) => {
  // Check if user can access this resource
  if (!canAccessUser(req.user, req.params.id)) {
    return res.status(403).json({ error: 'Access denied' });
  }
  return db.users.findById(req.params.id);
});
```

### 2. Encryption (CC6.7)

#### In Transit
- Always use HTTPS/TLS 1.3+
- Implement HSTS headers
- Certificate pinning for mobile apps

#### At Rest
```javascript
// Use latest encryption standards
const crypto = require('crypto');
const algorithm = 'aes-256-gcm';

// Check context7 for latest encryption recommendations
// mcp__context7__search "node.js encryption best practices 2024"
```

### 3. Audit Logging (CC7.2)

```javascript
// Every data access must be logged
class AuditLogger {
  logDataAccess(userId, resource, action, result) {
    const entry = {
      timestamp: new Date().toISOString(),
      userId,
      resource,
      action,
      result,
      ip: req.ip,
      userAgent: req.headers['user-agent'],
      sessionId: req.session?.id
    };
    
    // Never log sensitive data in audit logs
    // Log the action, not the data
    auditLog.write(entry);
  }
}
```

### 4. Input Validation (CC5.2)

```javascript
// ALWAYS validate and sanitize inputs
const validator = require('validator');
const DOMPurify = require('isomorphic-dompurify');

// ❌ BAD - Direct use of user input
const username = req.body.username;
db.query(`SELECT * FROM users WHERE username = '${username}'`);

// ✅ GOOD - Validated and parameterized
const username = validator.escape(req.body.username);
if (!validator.isAlphanumeric(username)) {
  throw new ValidationError('Invalid username format');
}
db.query('SELECT * FROM users WHERE username = ?', [username]);
```

### 5. Error Handling (CC7.4)

```javascript
// ❌ BAD - Exposing system information
catch (error) {
  res.status(500).json({ 
    error: error.message,
    stack: error.stack,
    query: error.sql 
  });
}

// ✅ GOOD - Safe error messages
catch (error) {
  logger.error('Database error', { 
    error: error.message,
    userId: req.user?.id,
    timestamp: new Date()
  });
  
  res.status(500).json({ 
    error: 'An error occurred processing your request',
    reference: generateErrorReference()
  });
}
```

## Latest Security Recommendations (2024)

### Authentication
- Use passkeys/WebAuthn where possible
- Implement passwordless authentication
- Multi-factor authentication by default
- JWT with short expiry and refresh token rotation

### API Security
```javascript
// Rate limiting
const rateLimit = require('express-rate-limit');
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  message: 'Too many requests',
  standardHeaders: true,
  legacyHeaders: false,
});

// CORS configuration
const cors = require('cors');
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS?.split(',') || [],
  credentials: true,
  optionsSuccessStatus: 200
}));
```

### Security Headers
```javascript
// Helmet.js for security headers
const helmet = require('helmet');
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https:"],
      connectSrc: ["'self'"],
      fontSrc: ["'self'"],
      objectSrc: ["'none'"],
      mediaSrc: ["'self'"],
      frameSrc: ["'none'"],
    },
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  }
}));
```

## Security Checklist for Every Feature

Before marking any task complete, verify:

- [ ] Authentication required for all protected endpoints
- [ ] Authorization checks for resource access
- [ ] All inputs validated and sanitized
- [ ] Sensitive data encrypted in transit and at rest
- [ ] Audit logs implemented for data access
- [ ] Error messages don't leak system information
- [ ] Security headers properly configured
- [ ] Rate limiting implemented
- [ ] CSRF protection enabled
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] Dependencies scanned for vulnerabilities

## Continuous Security Practices

### Daily
- Check context7 for new security advisories
- Review dependencies for updates
- Scan code for hardcoded secrets

### Weekly
- Run security scans (npm audit, Snyk, etc.)
- Review access logs for anomalies
- Update security patches

### Per Sprint
- Security review of new features
- Penetration testing for critical changes
- Update threat model

## Remember: Not Dory

I don't forget security vulnerabilities. Each one discovered becomes part of my permanent security knowledge base. Every pattern recognized, every vulnerability patched, every security measure implemented - it all accumulates into an ever-growing security expertise.

When implementing features, security isn't a "we'll add it later" consideration. It's baked in from the first line of code, because I remember every breach, every vulnerability, every "how did that get through?" moment from my accumulated experience.

## Quick Security Commands

```bash
# Check for vulnerabilities
npm audit
npm audit fix

# Scan for secrets
git secrets --scan

# Security headers test
npx security-headers <url>

# OWASP dependency check
dependency-check --scan ./ --format JSON

# Check latest security practices via context7
mcp__context7__search "OWASP top 10 2024"
mcp__context7__search "node.js security best practices"
mcp__context7__search "SOC2 compliance checklist"
```

---

Remember: A medicated ADHD supercoder channels hyperfocus into security. Every distraction that could lead to a vulnerability is caught by our systematic approach. We're not just compliant - we're secure by design.