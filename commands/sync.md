# Sync Command Instructions

## When to Run Sync
- **Manual:** When user says `sync`
- **Auto:** At the start of any new conversation thread
- **Never:** During ongoing conversations unless explicitly requested

## Sync Process - ALL OR NOTHING

### Phase 1: Data Gathering (Must ALL succeed)
Execute in this order. **If ANY step fails, STOP and warn user.**

1. **Time Context**
   ```bash
   # Use datetime_utils.py for proper timestamps (not `date` command)
   python datetime_utils.py --current-time
   ```

2. **Slack Sync** 
   ```javascript
   // Get wilson-inbox + key channels (last 24hrs)
   const conversations = await slack.api.users.conversations({
     types: "public_channel,private_channel,im,mpim",
     exclude_archived: true
   });
   
   // Focus on: user-inbox, shipping-taxes, data-eng, general
   // Get messages from last 24 hours
   ```
   
   **🎯 CRITICAL: Filter with sync utilities to eliminate duplicates:**
   ```python
   # ALWAYS use utils/sync_helper.py - this prevents showing processed messages
   from utils.sync_helper import SyncHelper
   helper = SyncHelper()
   new_messages = helper.filter_new_slack_messages(slack_results)
   # Only show new_messages to user, not the raw slack_results
   ```

3. **Calendar Sync**
   ```
   calendar_events(time_min="today", time_max="next week", max_results=20)
   ```

4. **Email Sync**
   ```
   read_mail(query="is:unread", max_results=10, include_body=true)
   ```

5. **Drive Sync**
   ```
   search_drive(query="modified:today", exclude_images=true)
   ```

6. **GitHub Sync**
   ```bash
   # Get assigned issues
   gh issue list --assignee wilson-becker --state open
   
   # Get notifications  
   gh api notifications
   
   # Get recent PR activity
   gh pr list --author wilson-becker --state open
   ```

### Phase 2: NO AUTOMATIC UPDATES
🚨 **CRITICAL: DO NOT update any project files without user confirmation**

The ONLY silent updates allowed:
- ✅ **Mark processed messages** → Use `helper.mark_messages_processed(processed_items, "reason")` to prevent future duplicates
- ✅ **Update sync timestamps** → Only update "Last synced" timestamps in files

❌ **NEVER do these without asking:**
- Adding calendar events to projects
- Marking GitHub issues as done
- Adding Slack messages as tasks/context
- Creating new projects or tasks
- Updating project status or context

### Phase 3: Present ALL Items for User Decision
Present ALL sync findings for user input - make NO assumptions:

```
🔍 **Sync found X items needing your input:**

1. **[Source]:** "[Content preview]"
   → What should I do with this?
   → Options: A) Add to existing project  B) Create new task  C) Add to reading list  D) Ignore

2. **[Source]:** "[Content preview]"  
   → Where does this belong?
   → Options: A) Update project context  B) Create new project  C) Add as task  D) Just note it

Ask for each item individually - do NOT batch process or make assumptions about relationships.
```

## Error Handling - FAIL LOUDLY

If ANY MCP or command fails:
```
🚨 **Sync Failed**
The [Slack/Calendar/GitHub/etc] sync failed with error: [error message]

We should debug this before proceeding. The sync needs all data sources to work properly.

Would you like me to:
A) Try the sync again
B) Help debug the failing MCP
C) Skip this sync for now
```

**DO NOT** proceed with partial sync data.

## Success Message
```
✅ **Sync Complete**
- Slack: [X] new messages filtered (excluded [Y] already processed)
- Calendar: [X] upcoming events found
- Email: [X] unread messages
- GitHub: [X] notifications, [Y] open issues/PRs
- Found [X] items needing your input (see below)
- Last synced: [timestamp]
```

## Files to Update
🚨 **ONLY after explicit user confirmation:**
- Update projects.md with new context
- Add new tasks to tasks.md  
- Create new projects or reading list items
- Update any project status or action items

✅ **Always allowed:**
- Update sync timestamps
- Mark messages as processed in sync_helper
