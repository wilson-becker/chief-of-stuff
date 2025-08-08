# Setup Command - New User Onboarding

## Purpose
Guide new users through complete Chief of Stuff system setup, from MCP authentication to personalized configuration.

## Setup Flow

### Step 1: Welcome & Overview
```
🎉 Welcome to Chief of Stuff - Your Living Second Brain!

This setup will guide you through:
1. ✅ MCP Authentication & Testing
2. 📱 Slack Inbox Channel Creation  
3. 🔄 Initial Sync Test
4. 👤 Vault Profile Import
5. 📝 Personal Context Interview
6. 📊 Projects & Tasks Bootstrap
7. 🚀 Final Cleanup & GitHub Push

Let's get started! This will take about 10-15 minutes.
```

### Step 2: MCP Authentication Check
**Test each MCP with actual API calls:**

```javascript
// Test Slack MCP
const slackTest = await slack.api.auth.test();
console.log("✅ Slack:", slackTest.user);

// Test Vault MCP  
const vaultTest = await vault.get_user("me");
console.log("✅ Vault:", vaultTest.name);

// Test Google Workspace MCP
const calendarTest = await google.list_calendars();
console.log("✅ Google:", calendarTest.length, "calendars");

// Test Data Portal MCP
const dataTest = await data.list_data_platform_docs("test");
console.log("✅ Data Portal: Connected");
```

**For each failed MCP:**
- Show specific error message
- Provide setup instructions  
- Ask: "Do you want to use [MCP NAME]? (y/n/skip)"
- If skip: Remove MCP references from menu.md, sync.md, user-context.md template

**Continue only when at least Slack + Vault are working**

### Step 3: Slack Inbox Creation
```
📱 **Slack Inbox Setup**

You need a private Slack channel for personal notes and task context.

**Please create a private channel named: #[firstname]-inbox**
- In Slack: Click + next to "Channels" 
- Choose "Create a channel"
- Name: [firstname]-inbox (e.g., #wilson-inbox)
- Make it Private
- Add only yourself

**Once created, type "test" in the channel, then come back here.**

Ready to continue? (y/n)
```

**Verify the channel exists:**
```javascript
const channels = await slack.api.users.conversations({
  types: "private_channel",
  exclude_archived: true
});
// Look for [firstname]-inbox pattern
```

### Step 4: Initial Sync Test
```
🔄 **Testing Sync Functionality**

Running initial sync to verify all connections...
```

**Run sync command flow but with extra logging:**
- Test Slack message retrieval
- Test Calendar access
- Test GitHub (if enabled)
- Test Google Drive (if enabled)
- Show success/failure for each

**If any critical failures, stop and troubleshoot**

### Step 5: Vault Profile Import
```
👤 **Importing Your Shopify Profile**

Getting your details from Vault...
```

**Use Vault MCP to get user info:**
```javascript
const userProfile = await vault.get_user("me");
const userTeam = await vault.get_team(userProfile.home_team_id);
```

**Extract and show:**
- Full name, email, GitHub handle
- Job title, team, manager
- Location, timezone
- Current projects (if any)

```
Found your profile:
- Name: [name]
- Email: [email]  
- Team: [team]
- GitHub: [github_handle]
- Timezone: [timezone]

Does this look correct? (y/n)
```

### Step 6: Personal Context Interview
```
📝 **Personal Context Setup**

Now I'll ask you some questions to customize your experience...
```

**Ask user for:**

1. **Slack Channels:** "Which Slack channels should I monitor for important updates?"
   - Show channels they're in, let them select
   - Exclude their inbox channel automatically

2. **Work Focus:** "What are your main work areas or responsibilities?"
   - Use for project categorization

3. **Meeting Preferences:** "What types of meetings should I prioritize in your calendar?"
   - All-hands, 1:1s, team meetings, etc.

4. **GitHub Repos:** "Which GitHub repositories do you work on regularly?"
   - For targeted issue/PR monitoring

5. **Notification Preferences:** "How often should I sync data?"
   - Every hour, twice daily, manual only

**Create user-context.md with all collected info**

### Step 7: Projects & Tasks Bootstrap
```
📊 **Setting Up Your First Project**

Let's create your first project to get you started...
```

**If Vault found active projects:**
```
I found these active projects in Vault:
1. [Project Name] - [Status]
2. [Project Name] - [Status]

Should I import these as starting projects? (y/n)
```

**If no Vault projects or user declines:**
```
Let's create a sample project:

What's something you're currently working on?
- Project name: ___
- Brief description: ___
- Key people involved: ___
- Target completion: ___
```

**Create initial projects.md and tasks.md with:**
- Sample project structure
- 2-3 example tasks
- Proper formatting examples

### Step 8: Final Test & Cleanup
```
🚀 **Final Setup Verification**

Running complete system test...
```

**Execute:**
- `menu` command (show all options work)
- `sync` command (verify no errors)
- Show sample output from each

```
✅ **Setup Complete!**

Your Chief of Stuff system is ready:
- ✅ All MCPs authenticated and tested
- ✅ Slack inbox created: #[name]-inbox
- ✅ Personal context configured
- ✅ Initial projects and tasks created
- ✅ Sync working perfectly

**Final step:** Should I clean up the setup command and push your personalized system to GitHub?

This will:
1. Delete commands/setup.md
2. Commit all your personal configuration
3. Push to your GitHub repository
4. Your system will be ready for daily use!

Proceed with cleanup and push? (y/n)
```

**If yes:**
```bash
git rm commands/setup.md
git add .
git commit -m "Complete Chief of Stuff setup for [name]

- Configured personal context and preferences  
- Set up Slack inbox: #[name]-inbox
- Imported Vault profile and projects
- Verified all MCP connections
- Ready for daily productivity use"
git push origin main
```

```
🎉 **Welcome to your new second brain!**

Try these commands to get started:
- `menu` - See all your options
- `menu -pt` - Quick projects + tasks view  
- `sync` - Get latest updates from all sources
- `brag` - Track your accomplishments

Your Chief of Stuff system is now live and personalized! 🚀
```

## Error Handling
- **MCP failures:** Offer to skip or retry with different auth
- **Slack channel issues:** Provide detailed creation steps
- **Vault access problems:** Fall back to manual context entry
- **GitHub push failures:** Show manual push instructions

## Recovery
If setup is interrupted, user must restart from beginning. All progress is discarded to ensure clean state.
