# Menu Command Instructions

## When User Says `menu`
Present exactly these 7 options with no additional descriptions or explanations:

```
**1.** 📊 **List all Projects**
**2.** 📋 **List all Tasks** 
**3.** 💬 **Slack digest**
**4.** 📅 **Upcoming meetings**
**5.** 🔧 **GitHub digest**
**6.** 📧 **Google Digest**
**7.** 📚 **Reading list**
```

## How Each Option Works

### Option 1: List all Projects
- Read projects.md in full
- Present each project with:
  - Status indicator (🟡 In Progress, 🟢 Complete, etc.)
  - Priority level
  - Key people involved
  - Recent context (last 2-3 items)
  - Next action items with due dates
- Clean, scannable format

### Option 2: List all Tasks  
- Read tasks.md in full
- Group by priority: 🔴 Urgent → 🟡 High → 🟢 Medium → ⚪ Low
- Show due dates prominently
- Include estimates where available
- Separate completed tasks at bottom

### Option 3: Slack Digest
- Read user-context.md to get the user's Slack username and important channels
- Use Slack MCP to check PUBLIC/TEAM channels listed in user-context.md for unread messages from the last day
- EXCLUDE private inbox channels (e.g., #wilson-inbox) - these are personal notes, not team communications
- Focus on:
  - Posts mentioning the user (use username from user-context.md)
  - Messages with actionable items
  - Important announcements or decisions
  - Links to docs/resources
- Present as: "Channel → Key Message TLDR → Link → Potential Action"

### Option 4: Upcoming Meetings
- Use Calendar MCP for next 7 days
- For each meeting show:
  - Date/time
  - Attendees
  - Meeting purpose (if available)
  - **Prep needed?** Check against projects.md for related context
- Ask: "Which meetings need prep?" rather than assuming

### Option 5: GitHub Digest
- Read user-context.md to get the user's GitHub username
- Use GitHub CLI commands with the username from user-context.md:
  ```bash
  gh issue list --assignee {github_username} --state open
  gh api notifications  
  gh pr list --author {github_username} --state open
  ```
- Present as:
  - Issues assigned to you → Priority + TLDR
  - PR reviews needed → Who's waiting
  - Recent activity → What happened
- Suggest potential actions for each item

### Option 6: Google Digest
- Use Google Workspace MCP:
  - Unread emails (work-related only)
  - Recent docs/sheets activity
  - Comments on shared files
- Focus on actionable items:
  - Emails needing response
  - Docs needing review
  - Shared files with updates
- Present with quick TLDR and suggested actions

### Option 7: Reading List
- Read reading-list.md in full
- Present as prioritized list:
  - Articles/docs with context on why important
  - Books with relevance to current role
  - Internal docs for onboarding/projects
- Group by: 🔴 Urgent reads → 🟡 High Priority → 🟢 When time allows
- Show status and estimated time for each item

## Presentation Style
- **Clean and scannable** - use emojis and formatting
- **Actionable** - always suggest next steps
- **Contextual** - connect items to existing projects when relevant
- **Concise** - summaries not full details
- **Interactive** - end with "What would you like to focus on?"

## After Presenting Menu
Wait for user to choose an option (1-7) or ask follow-up questions. Do not assume what they want to work on.
