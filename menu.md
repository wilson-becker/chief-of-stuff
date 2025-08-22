# Menu Command - Deterministic Display

## Command Formats
- `menu` → Show 7 options
- `menu sync` → Sync all systems (Slack, Calendar, GitHub, Email)
- `menu sync -i` → Sync inbox only
- `menu -pt` → Projects + Tasks combined
- `menu -projects` → Projects only
- `menu -tasks` → Tasks only
- `menu -slack` → Slack digest only
- `menu -calendar` → Calendar only

---

## menu (Show Options)

Present exactly these 7 options:
```
**1.** 🔄 **Sync all systems**
**2.** 📊 **List all Projects**
**3.** 📋 **List all Tasks** 
**4.** 💬 **Slack digest**
**5.** 📅 **Upcoming meetings**
**6.** 🔧 **GitHub digest**
**7.** 📚 **Reading list**
```

Wait for user to choose 1-7.

---

## menu sync (Sync All Systems)

🚨 **MANDATORY EXECUTION RULES** 🚨
1. **NEVER SIMULATE OR FAKE RESULTS** - Always use real MCP tools
2. **FOLLOW EXACT STEPS** - Do not improvise or skip any step  
3. **USE EXACT CODE** - Copy/paste the JavaScript and Python exactly as written
4. **IF ANY STEP FAILS** - STOP and report the error, do not continue

### Step 1: Sync Slack (All Channels)
Use multiple `mcp_playground-slack-mcp_slack_search` calls for each channel in user-context.md "Core Work Channels (Most Important)" section: query="in:#channel-name after:YYYY-MM-DD", sort="desc", count=20 (where YYYY-MM-DD = current date minus 4 days, calculated using terminal command: `date -v-4d +%Y-%m-%d`)

**ERROR HANDLING:** If a channel ID is missing from user-context.md, skip that channel and note it in results. If user-context.md is missing, use only #wilson-inbox (C0994TKREDA).

**BACKUP:** If playground-slack-mcp is down, use `mcp_callm-for-slack_evaluate_repl_function` with this exact code:
**Note:** callm-for-slack uses JavaScript functions while playground-slack-mcp uses direct parameters. Do not mix parameter formats.

```javascript
async function(slack) {
  // Get channels from user-context.md core work channels
  const channels = [
    'C0994TKREDA', // wilson-inbox
    // Add other channel IDs from user-context.md
  ];
  
  const fourDaysAgo = new Date(Date.now() - (4 * 24 * 60 * 60 * 1000));
  const oldestTimestamp = (fourDaysAgo.getTime() / 1000).toString();
  
  const results = [];
  for (const channelId of channels) {
    const response = await slack.api.conversations.history({
      channel: channelId,
      oldest: oldestTimestamp,
      limit: 20
    });
    
    if (response.ok && response.messages) {
      results.push({
        channelId,
        messages: response.messages
      });
    }
  }
  
  return { success: true, channels: results };
}
```

### Step 2: Sync Calendar
Use `mcp_gworkspace-mcp_calendar_events`:
```
calendar_events(
  time_min="today", 
  time_max="next week", 
  max_results=20,
  include_attendees=true
)
```

### Step 3: Sync GitHub
Use `gh` commands to fetch notifications:
```bash
gh api notifications --paginate
```

### Step 4: Sync Email
Use `mcp_gworkspace-mcp_read_mail` to fetch unread emails:
```
read_mail(max_results=10, query="is:unread")
```

### Step 5: Present Combined Results
"I synced all your systems and found [X] updates:

**📬 Slack:** [X] new messages across [Y] channels
**📅 Calendar:** [X] upcoming meetings this week  
**🔧 GitHub:** [X] new notifications
**📧 Email:** [X] unread emails

What would you like to dive into first?"

---

## menu sync -i (Inbox Only Sync)

### Step 1: Fetch Inbox Messages
**MANDATORY:** Use `mcp_playground-slack-mcp_slack_search` with parameters: query="in:#wilson-inbox after:YYYY-MM-DD", sort="desc", count=50 (where YYYY-MM-DD = current date minus 4 days, calculated using terminal command: `date -v-4d +%Y-%m-%d`)

**BACKUP:** If playground-slack-mcp is down, use `mcp_callm-for-slack_evaluate_repl_function` tool with this EXACT code (do not modify):
**Note:** callm-for-slack uses JavaScript functions while playground-slack-mcp uses direct parameters. Do not mix parameter formats.

```javascript
async function(slack) {
  const channelId = 'C0994TKREDA'; // Wilson's inbox from user-context.md
  
  // Get last 4 days of messages
  const fourDaysAgo = new Date(Date.now() - (4 * 24 * 60 * 60 * 1000));
  const oldestTimestamp = (fourDaysAgo.getTime() / 1000).toString();
  
  const response = await slack.api.conversations.history({
    channel: channelId,
    oldest: oldestTimestamp,
    limit: 50
  });
  
  return {
    success: response.ok,
    messageCount: response.messages ? response.messages.length : 0,
    messages: response.messages || [],
    timeRange: `${fourDaysAgo.toISOString()} to ${new Date().toISOString()}`
  };
}
```

### Step 2: Find New Messages
**MANDATORY:** Check for new messages using the archive-aware comparison:

1. **Check if archive exists:** Use `read_file` tool on `message-archive/archives/archive_metadata.json`
   - If file exists, note the `oldest_active_timestamp` 
   - If file doesn't exist, proceed with all messages

2. **Read active processed messages:** Use `read_file` tool on `message-archive/processed_messages.json`
   - If file doesn't exist, treat all messages as new

3. **Compare timestamps:** Look at MCP results from Step 1:
   - For messages older than `oldest_active_timestamp`: assume already processed
   - For newer messages: check if timestamp (`ts` field) is NOT in processed messages file
   - Those are your new messages to present

4. **Auto-archive if needed:** If processed_messages.json has >100 entries, follow the archival process in `commands/archive-messages.md`

### Step 3: Present Results (Conversational)
Present findings naturally like a Slack buddy:

"I checked your inbox and found [X] new things since we last talked:

• [Message preview with key context]
• [Another message with why it might matter]
• [Third message with potential connection to existing projects]

How do you want me to incorporate these into your project files? Anything look like it should update your shipping reconciliation work, or maybe create a new task?"

---

## menu -pt (Projects + Tasks)

### Step 1: Read Files
- Read `projects.md` 
- Read `tasks.md`

### Step 2: Present Conversationally
"Here's what's on your plate right now:

**🚨 Heads up - these need attention in the next couple days:**
• [Urgent project action with context]
• [Urgent task with deadline]

**📊 Your active projects:**
• **Shipping Invoice Reconciliation** - In progress with Jasmin, next: finalize data model
• **[Other project]** - [Status and what's next]

**📋 Your task list:**
🔴 **Urgent stuff:**
• [Task with deadline and context]

🟡 **High priority:**
• [Important task you should tackle soon]

What do you want to dive into first?"

---

## menu -projects (Projects Only)

### Step 1: Read projects.md

### Step 2: Present Conversationally
"Let me catch you up on your projects:

**🚨 First things first - these need attention soon:**
• [Urgent project action with context and deadline]

**📊 Here's everything you're working on:**
• **Shipping Invoice Reconciliation** - Looking good, you've got that meeting with Jasmin tomorrow about the data model. Next step is probably finalizing those BigQuery tables.
• **[Other project]** - [Natural description of status and what's happening next]

Which project do you want to focus on? Or should we talk through any blockers you're hitting?"

---

## menu -tasks (Tasks Only)

### Step 1: Read tasks.md

### Step 2: Present Conversationally
"Here's what's on your task list:

**🚨 These are coming up fast:**
• [Task with deadline] - Due [when], this is about [context]

**🔴 Urgent stuff to tackle:**
• [Task description with why it matters]
• [Another urgent task with context]

**🟡 Important but not burning:**
• [High priority task with some context]

**🟢 When you get a chance:**
• [Medium priority tasks]

What feels most important to knock out first? Or is there something blocking you on any of these?"

---

## menu -slack (Slack Digest)

### Step 1: Run Slack Sync
Execute the same slack sync logic as `menu sync -i` to get fresh messages.

### Step 2: Create Reader's Digest Summary
Analyze the synced messages and present conversationally
"I scanned your key Slack channels from the last day - here's what caught my attention:

**#shipping-invoice-reconciliation**: Jasmin posted about the Purolator dispute numbers - looks like the $400k gap is confirmed. Might be worth updating your project context with this.

**#shipping-taxes-data-team**: Vincent shared some new BigQuery patterns that could help with your reconciliation work.

**#wilson-inbox**: You left yourself a note about following up with Gajanan on the finance table access.

Anything here you want me to help you act on or add to your project files?"

---

## menu -calendar (Calendar Only)

### Step 1: Use Calendar MCP
Execute calendar sync from sync.md.

### Step 2: Present Conversationally
"Looking at your calendar for the week:

**Today**: You've got that 2pm sync with the shipping team - Jasmin and Vincent will be there. Perfect timing to discuss the reconciliation progress.

**Tomorrow**: 1:1 with Vincent at 10am. Good chance to update him on your data model work and maybe get his thoughts on the finance table access issue.

**Friday**: Looks like you blocked time for deep work - smart move for tackling those BigQuery queries.

Want me to help you prep for any of these? I could pull together talking points from your project updates."

---

## Execution Rules
1. **Read the specified files first**
2. **Be conversational and natural** - like a knowledgeable Slack buddy
3. **Always end with a question** that invites engagement
4. **If files are empty**, say something like "Looks like your task list is empty - nice work! Anything new you want to add?"
5. **ERROR HANDLING:** If required files (projects.md, tasks.md, user-context.md) don't exist, inform Wilson and ask if he wants to create them. If command-specific files are missing, use fallback conversational approach.