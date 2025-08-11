# Menu Command - Deterministic Display

## Command Formats
- `menu` → Show 7 options
- `menu -pt` → Projects + Tasks combined
- `menu -projects` → Projects only
- `menu -tasks` → Tasks only
- `menu -slack` → Slack digest only
- `menu -calendar` → Calendar only

---

## menu (Show Options)

Present exactly these 7 options:
```
**1.** 📊 **List all Projects**
**2.** 📋 **List all Tasks** 
**3.** 💬 **Slack digest**
**4.** 📅 **Upcoming meetings**
**5.** 🔧 **GitHub digest**
**6.** 📧 **Google Digest**
**7.** 📚 **Reading list**
```

Wait for user to choose 1-7.

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

### Step 1: Use Slack MCP
Execute the slack sync logic from sync.md to get recent messages.

### Step 2: Present Conversationally
"I scanned your key Slack channels from the last day - here's what caught my attention:

**#shipping-invoice-reconciliation**: Jasmin posted about the Purolator dispute numbers - looks like the $400k gap is confirmed. Might be worth updating your project context with this.

**#team-data-channel**: Vincent shared some new BigQuery patterns that could help with your reconciliation work.

**#user-inbox**: You left yourself a note about following up with Gajanan on the finance table access.

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