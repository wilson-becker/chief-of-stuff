# Chief of Stuff - Your Living Second Brain

**"Your curious Slack buddy who never forgets and always asks the right questions"**

This isn't automation - it's a conversational AI companion that learns how you think, constantly reorganizes your work context, and helps you stay on top of complex projects without getting in your way.

## How It Works

**Markdown as Database** → Your projects, tasks, and reading list live in simple markdown files  
**Conversational Intelligence** → Chat naturally with an AI that updates your files based on every answer  
**Progressive Context** → From quick rules to detailed memories, any agent can jump in and understand everything  
**Constant Learning** → Every question you answer refines how the system organizes your mental model

## Getting Started

1. **Clone this repo** and customize `user-context.md` with your info
2. **Any new Cursor conversation** starts with the AI reading your context and being ready to help
3. **Chat naturally** or use three core commands: `menu`, `sync`, `brag`
4. **Watch your second brain evolve** as the AI learns your work patterns and priorities

## Your Second Brain Structure

```
/chief/
  README.md              # You are here
  .cursorrules           # Core behavioral rules for any AI agent
  agent-instructions.md  # Complete system overview for AI agents
  
  # Templates (copy these to create your working files)
  user-context.template.md    # Your role, goals, team, preferences
  project.template.md         # Template for complex initiatives
  task.template.md           # Template for standalone action items
  reading-list.template.md   # Template for learning materials
  brag-doc.template.md       # Template for weekly accomplishments
  
  # Your working files (created from templates)
  user-context.md        # Your customized context
  projects.md            # Your active projects
  tasks.md              # Your current tasks
  reading-list.md       # Your learning materials
  
  commands/             # Detailed instructions for menu, sync, brag
  context/              # Extended context when projects get complex
  brag-docs/            # Weekly accomplishment tracking
```

## Three Commands, Infinite Possibilities

- **`menu`** → Clean 7-option dashboard of your work
- **`sync`** → Pull fresh context from Slack, Calendar, GitHub, Google Workspace  
- **`brag`** → Guided interview to create promotion-ready accomplishment docs

*Each command has detailed instructions in `/commands/` - the AI reads these automatically.*

## The Magic: Curious Intelligence

This system **assumes it doesn't understand** and **constantly asks for clarification**:

- *"This looks related to your shipping project, but I'm not sure - is that right?"*
- *"Help me understand how this fits with your current priorities"*  
- *"Let me update your project context based on what you just told me"*

**Every answer you give immediately updates your markdown files.** Your changing brain = constantly evolving second brain.

## Progressive Disclosure System

Any AI agent jumping into a new conversation follows this path:

1. **`.cursorrules`** → Basic behavioral rules and file structure
2. **Cursor memories** → Your personal preferences and work context
3. **`README.md`** → System overview and command structure  
4. **Live data files** → Current projects, tasks, reading list
5. **Detailed instructions** → Command-specific guidance when needed

**Result:** Zero onboarding time, maximum context awareness, consistent helpful behavior.

## For New Users

This is a **template repository**. To make it yours:

1. **Fork/clone** this repo
2. **Create your working files** from templates:
   ```bash
   cp user-context.template.md user-context.md
   cp projects.template.md projects.md  
   cp tasks.template.md tasks.md
   cp reading-list.template.md reading-list.md
   ```
3. **Customize** `user-context.md` with your role, team, goals, and Slack channels
4. **Install required MCPs** for Slack, Google Workspace, GitHub integration
5. **Start chatting** - the AI will help you populate your projects and tasks
6. **Use `sync`** regularly to keep your second brain current with real-world changes

## Philosophy

**Your work is complex and constantly changing.** Traditional productivity tools break when priorities shift or context evolves. This system **embraces the chaos** by staying curious, asking questions, and reorganizing your mental model in real-time.

**The AI doesn't assume it knows what you want.** It asks, learns, updates, and asks again. Your second brain stays synchronized with your actual brain.

---

*Built for knowledge workers who need intelligent organization without rigid automation.*
