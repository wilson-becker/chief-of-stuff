# Menu Command Instructions

## Menu Command Formats
- **Default menu:** `menu` (show all 7 options, no sync)
- **Targeted menu:** `menu -tasks`, `menu -projects`, `menu -pt`, `menu -slack`, `menu -calendar`, `menu -github`, `menu -google`, `menu -reading`
- **Sync + menu:** `menu -sync` (run full sync first, then show menu)
- **Sync + targeted:** `menu -sync -tasks` (sync first, then show just tasks)
- **Combined views:** `menu -pt` (projects + tasks), `menu -sync -pt` (sync + projects + tasks)

## Supported Arguments
- `-projects` or `-p` → Show only projects (option 1)
- `-tasks` or `-t` → Show only tasks (option 2)
- `-pt` → Show both projects and tasks in combined output
- `-slack` or `-s` → Show only Slack digest (option 3)
- `-calendar` or `-c` → Show only upcoming meetings (option 4)
- `-github` or `-g` → Show only GitHub digest (option 5)
- `-google` or `-e` → Show only Google digest (option 6)
- `-reading` or `-r` → Show only reading list (option 7)
- `-sync` → Run full sync first, then show menu/options

## When User Says `menu` (no args)
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
- **Format with critical items first:**
  1. **🚨 Critical Items (Next 2 Days)** - Any project action items due within 48 hours
  2. **📊 All Projects** - Full project list with status, priority, stakeholders, recent context, next actions
- Present each project with:
  - Status indicator (🟡 In Progress, 🟢 Complete, etc.)
  - Priority level
  - Key people involved
  - Recent context (last 2-3 items)
  - Next action items with due dates
- Clean, scannable format

### Option 2: List all Tasks
- Read tasks.md in full
- **Format with critical items first:**
  1. **🚨 Critical Items (Next 2 Days)** - Any tasks due within 48 hours
  2. **📋 All Tasks** - Group by priority: 🔴 Urgent → 🟡 High → 🟢 Medium → ⚪ Low
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

## Execution Flow
**For `menu` (no args):**
- Present all 7 options immediately (no sync)
- Wait for user to choose an option (1-7)

**For `menu -[option]` (targeted):**
- Execute the specific option immediately (no sync)
- Present the results directly
- For `-pt`: Execute combined projects+tasks format:
  1. **🚨 Critical Items (Next 2 Days)** - Any project actions or tasks due within 48 hours
  2. **📊 Projects** - All active projects with context
  3. **📋 Tasks** - All tasks grouped by priority

**For `menu -sync`:**
- Run full sync first (follow sync.md instructions)
- Then present all 7 options
- Wait for user to choose

**For `menu -sync -[option]`:**
- Run full sync first
- Then execute the specific option immediately
- Present the results directly
- For `-sync -pt`: Sync first, then show combined format:
  1. **🚨 Critical Items (Next 2 Days)** 
  2. **📊 Projects** 
  3. **📋 Tasks**

## After Presenting Menu
Wait for user to choose an option (1-7) or ask follow-up questions. Do not assume what they want to work on.
