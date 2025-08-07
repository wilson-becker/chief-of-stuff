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
   
   **Then filter with Python:**
   ```python
   # Use utils/sync_helper.py to filter out processed messages
   from utils.sync_helper import SyncHelper
   helper = SyncHelper()
   new_messages = helper.filter_new_slack_messages(slack_results)
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

### Phase 2: Confident Updates (Silent)
Only update things you're 100% certain about:
- ✅ Calendar events → Add to relevant project prep needs
- ✅ Completed GitHub issues → Mark done in projects
- ✅ Clear task completions from Slack
- ✅ New meetings → Add to prep list
- ✅ **Mark processed messages** → Use `helper.mark_messages_processed()` to track handled items

### Phase 3: Clarification Dialog
Present unclear items for user decision:

```
🔍 **Sync found X items needing your input:**

1. **[Source]:** "[Content preview]"
   → Looks related to "[Project Name]" project?
   → Add as: A) Project context  B) New task  C) New blocker  D) Somewhere else?

2. **[Source]:** "[Content preview]"
   → Should I: A) Create new project  B) Add to existing project  C) Create task  D) Just note it?
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
- Updated [X] projects with new context
- Added [X] calendar events to prep list  
- Found [X] items needing your input (see below)
- Last synced: [timestamp]
```

## Files to Update
- Always update timestamps in projects.md and tasks.md
- Add new context to "Recent Context" sections
- Create new tasks/projects only after user confirmation
- Maintain clean formatting and consistent structure
