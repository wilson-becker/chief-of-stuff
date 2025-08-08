# Project Context Directory

This directory contains detailed context files for projects that have grown beyond the "Recent Context" section in `projects.md`.

## When to Create Context Files

Create individual context files when:
- A project's "Recent Context" section has more than 10 entries
- The main `projects.md` file becomes too long to read easily
- A project has extensive historical context that needs to be preserved

## File Naming Convention

Use kebab-case based on the project name:
- "Shipping Invoice Reconciliation" → `shipping-invoice-reconciliation.md`
- "Label Penetration Analysis" → `label-penetration-analysis.md`
- "User Onboarding" → `user-onboarding.md`

## Context File Structure

```markdown
# [Project Name] - Full Context

**Related Project:** See main entry in `/chief/projects.md`

## Complete Context History

### [Date] - [Source]
[Full context entry with details]

### [Date] - [Source]  
[Full context entry with details]

## Key People Discovered
- **[Name]** - [Role] - [How they're involved]

## Important Links
- [Slack threads, GitHub issues, docs, etc.]

## Historical Decisions
- **[Date]:** [Decision made and rationale]

---
*Last Updated: [Date]*
```

## Integration with projects.md

When a project graduates to having its own context file:

1. **Keep recent context** (last 3-5 entries) in `projects.md`
2. **Add reference** to full context file:
   ```markdown
   ## 🔗 Related
   - **Full Context:** `/chief/context/project-name.md`
   ```
3. **Move older context** to the individual file
4. **Update both files** when new context is added via sync

This keeps `projects.md` readable while preserving complete project history.
