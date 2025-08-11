# Sync Command - Deterministic Data Fetching

🚨 **MANDATORY EXECUTION RULES** 🚨
1. **NEVER SIMULATE OR FAKE RESULTS** - Always use real MCP tools
2. **FOLLOW EXACT STEPS** - Do not improvise or skip any step  
3. **USE EXACT CODE** - Copy/paste the JavaScript and Python exactly as written
4. **IF ANY STEP FAILS** - STOP and report the error, do not continue

## Command Formats
- `sync` → Full sync (all sources)
- `sync -i` → Inbox only (Wilson's private channel)
- `sync -slack` → All Slack channels
- `sync -calendar` → Calendar events only
- `sync -github` → GitHub notifications only
- `sync -email` → Unread emails only

---

## sync -i (Inbox Only)

### Step 1: Fetch Inbox Messages
**MANDATORY:** Use `mcp_callm-for-slack_evaluate_repl_function` tool with this EXACT code (do not modify):

```javascript
async function(slack) {
  const channelId = '{USER_INBOX_CHANNEL_ID}'; // Wilson's inbox from user-context.md
  
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

1. **Check if archive exists:** Use `read_file` tool on `context/archives/archive_metadata.json`
   - If file exists, note the `oldest_active_timestamp` 
   - If file doesn't exist, proceed with all messages

2. **Read active processed messages:** Use `read_file` tool on `context/processed_messages.json`

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

## sync -slack (All Channels)

### Step 1: Fetch All Channels
Use `mcp_callm-for-slack_evaluate_repl_function` with this exact code:

```javascript
async function(slack) {
  // Get channels from user-context.md core work channels
  const channels = [
    '{USER_INBOX_CHANNEL_ID}', // {user-inbox}
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

### Step 2: Filter and Present
Same filtering process as inbox, then present channel-by-channel results.

---

## sync -calendar (Calendar Only)

### Step 1: Fetch Calendar Events
Use `mcp_gworkspace-mcp_calendar_events`:
```
calendar_events(
  time_min="today", 
  time_max="next week", 
  max_results=20,
  include_attendees=true
)
```

### Step 2: Present Results (Conversational)
Present findings naturally:

"I looked at your calendar for the next week - here's what's coming up:

• **Tomorrow 2pm**: Shipping team sync with Jasmin and Vincent - looks like this might need some reconciliation prep?
• **Friday 10am**: 1:1 with Vincent - good timing to discuss your project progress
• **Next Tuesday**: All-hands meeting

Which of these do you want to prep for? Should I check if any connect to your current projects?"

---

## sync (Full Sync)

Execute all individual sync commands in sequence:
1. sync -slack
2. sync -calendar  
3. sync -github (using `gh` commands)
4. sync -email (using `mcp_gworkspace-mcp_read_mail`)

Present combined results and ask what to update.

---

## Error Handling

If any MCP call fails, be conversational:

"Hey, I ran into an issue trying to fetch your [Slack/calendar/etc] data - looks like [brief explanation of error]. 

Want me to try that again, or should we skip it for now and work with what we have?"

**Never proceed with partial data.**