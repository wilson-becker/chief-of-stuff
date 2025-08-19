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
- Name: [firstname]-inbox (e.g., #john-inbox)
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

### Step 7: File System Bootstrap
```
📁 **Creating Your Working Files**

Now I'll create your personalized system files from the templates...
```

**Create working files from templates with real data:**
1. **Create `user-context.md`** - Populate with Vault profile data and interview responses
2. **Create `projects.md`** - Add any imported Vault projects or user-provided projects  
3. **Create `tasks.md`** - Set up priority structure with any initial tasks
4. **Create `reading-list.md`** - Initialize with priority categories
5. **Create `brag-docs/` directory** - For future accomplishment tracking

**Remove template files and personalize README:**
```bash
rm *.template.md
```

**Create personalized README.md:**
```javascript
// Replace template README with personalized version
const firstName = userProfile.name.split(' ')[0];
const username = userProfile.github_handle || 'user';
const team = userProfile.team || 'team';

const personalizedReadme = `# ${firstName}'s Chief of Stuff System

**"Your curious Slack buddy who never forgets and always asks the right questions"**

This is ${firstName}'s personal productivity system - a conversational AI companion that learns how you think, constantly reorganizes work context, and helps stay on top of complex projects without getting in your way.

## How It Works

**Markdown as Database** → Projects, tasks, and reading list live in simple markdown files  
**Conversational Intelligence** → Chat naturally with an AI that updates files based on every answer  
**Progressive Context** → From quick rules to detailed memories, any agent can jump in and understand everything  
**Constant Learning** → Every question answered refines how the system organizes the mental model

## Current System Structure

\`\`\`
chief-of-stuff-${username}/
  user-context.md        # Your role, team, preferences, Slack channels
  projects.md            # Active projects with stakeholders and timelines
  tasks.md              # Standalone action items by priority
  reading-list.md       # Learning materials by urgency
  
  commands/             # Command execution instructions
  projects/             # Individual project workspaces with extended context
  message-archive/      # Message archiving system files
  brag-docs/            # Weekly accomplishment tracking
\`\`\`

## Three Core Commands

- **\`menu\`** → Clean 7-option dashboard of current work
- **\`sync\`** → Pull fresh context from Slack, Calendar, GitHub, Google Workspace, Vault  
- **\`brag\`** → Guided interview to create promotion-ready accomplishment docs

*Each command has detailed instructions in \`/commands/\` - the AI reads these automatically.*

## The Magic: Curious Intelligence

This system **assumes it doesn't understand** and **constantly asks for clarification**:

- *"This looks related to your ${team} work, but I'm not sure - is that right?"*
- *"Help me understand how this fits with your current priorities"*  
- *"Let me update your project context based on what you just told me"*

**Every answer immediately updates the markdown files.** Changing brain = constantly evolving second brain.

## Progressive Disclosure System

Any AI agent jumping into a new conversation follows this path:

1. **\`.cursorrules\`** → Basic behavioral rules and file structure
2. **Cursor memories** → Your personal preferences and work context
3. **\`README.md\`** → System overview and command structure  
4. **Live data files** → Current projects, tasks, reading list
5. **Detailed instructions** → Command-specific guidance when needed

**Result:** Zero onboarding time, maximum context awareness, consistent helpful behavior.

## Philosophy

**Work is complex and constantly changing.** Traditional productivity tools break when priorities shift or context evolves. This system **embraces the chaos** by staying curious, asking questions, and reorganizing the mental model in real-time.

**The AI doesn't assume it knows what you want.** It asks, learns, updates, and asks again. The second brain stays synchronized with the actual brain.

---

*Built for knowledge workers who need intelligent organization without rigid automation.*`;

// Write personalized README
await writeFile('README.md', personalizedReadme);
```

```
✅ **Your personalized files are ready:**
- user-context.md (with your real profile and preferences)
- projects.md (with your actual projects)
- tasks.md (organized by your priorities)  
- reading-list.md (ready for your learning materials)
- brag-docs/ (ready for weekly accomplishments)
- README.md (personalized for your system, no template language)

All template files have been removed - your system is now live!
```

### Step 8: Projects & Tasks Bootstrap
```
📊 **Populating Your Projects**

Let's add your current work to the system...
```

**If Vault found active projects:**
```
I found these active projects in Vault:
1. [Project Name] - [Status]
2. [Project Name] - [Status]

I've added these to your projects.md file. Should I gather more details about any of them? (y/n)
```

**If no Vault projects or user declines:**
```
Let's add your current work:

What's something you're currently working on?
- Project name: ___
- Brief description: ___
- Key people involved: ___
- Target completion: ___

I'll add this to your projects.md file with proper formatting.
```

### Step 9: Final Test & Cleanup
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
2. Remove any remaining template files  
3. Commit all your personal configuration
4. Push to your GitHub repository
5. Your system will be ready for daily use!

Proceed with cleanup and push? (y/n)
```

**If yes:**
```bash
git rm commands/setup.md
rm -f *.template.md  # Remove any remaining templates
git add .
git commit -m "Complete Chief of Stuff setup for [name]

- Created personalized working files from templates
- Configured personal context and preferences  
- Set up Slack inbox: #[name]-inbox
- Imported Vault profile and projects
- Verified all MCP connections
- Removed template files - system is now live
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

