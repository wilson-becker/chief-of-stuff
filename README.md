# User's Chief of Stuff System

**"Your curious Slack buddy who never forgets and always asks the right questions"**

This is the user Becker's personal productivity system - a conversational AI companion that learns how you think, constantly reorganizes work context, and helps stay on top of complex projects without getting in your way.

## How It Works

**Markdown as Database** → Projects, tasks, and reading list live in simple markdown files  
**Conversational Intelligence** → Chat naturally with an AI that updates files based on every answer  
**Progressive Context** → From quick rules to detailed memories, any agent can jump in and understand everything  
**Constant Learning** → Every question answered refines how the system organizes the mental model

## System Structure

```
chief-of-stuff-USER_NAME/
  user-context.md        # Personal info and preferences
  projects.md            # Active project registry
  tasks.md              # Standalone action items
  reading-list.md       # Learning materials
  commands/             # Command instructions
  projects/             # Project workspaces
  brag-docs/            # Accomplishment tracking
```

## Five Core Commands

- **`menu`** → Dashboard of current work with sync functionality
- **`brag`** → Guided accomplishment documentation
- **`debloat`** → System audit for inconsistencies and bloat
- **`pr`** → Contribute improvements to global repository
- **`pull`** → Fetch latest system improvements

*Each command has detailed instructions in `/commands/` - the AI reads these automatically.*

## The Magic: Curious Intelligence

This system **assumes it doesn't understand** and **constantly asks for clarification**:

- *"This looks related to your shipping project, but I'm not sure - is that right?"*
- *"Help me understand how this fits with your current priorities"*  
- *"Let me update your project context based on what you just told me"*

**Every answer immediately updates the markdown files.** Changing brain = constantly evolving second brain.

## Progressive Disclosure System

Any AI agent jumping into a new conversation follows this path:

1. **`.cursorrules`** → Basic behavioral rules and commands
2. **Cursor memories** → Personal preferences and work context
3. **Live data files** → Current projects, tasks, reading list
4. **Detailed instructions** → Command-specific guidance when needed

**Result:** Zero onboarding time, maximum context awareness, consistent helpful behavior.

## 🎯 Career Development
- **Target:** Senior → Staff Data Engineer progression
- **Focus:** Org-level problem solving and technical leadership
- **Team:** Shipping & Taxes Data Team under Vincent Chio

## 🔧 Technical Integration
- **MCPs:** Slack (callm-for-slack, backup: playground-slack-mcp), Google Workspace, GitHub, Vault, Data Platform
- **Channels:** #USER_NAME-inbox, #shipping-taxes-data-team, #shipping-invoice-reconciliation
- **Tools:** BigQuery, dbt, Looker, Python, SQL

## Philosophy

**Work is complex and constantly changing.** Traditional productivity tools break when priorities shift or context evolves. This system **embraces the chaos** by staying curious, asking questions, and reorganizing the mental model in real-time.

**The AI doesn't assume it knows what you want.** It asks, learns, updates, and asks again. The second brain stays synchronized with the actual brain.

## Repository Management

This is User's personal deployment of the Chief of Stuff system. Framework improvements can be contributed to the global template repository using the `pr` command, and updates can be fetched using the `pull` command.

---

*Built for knowledge workers who need intelligent organization without rigid automation.*