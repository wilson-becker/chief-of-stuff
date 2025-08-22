# Pull Command - Fetch System Improvements

## Purpose
Pull system file improvements from the global Chief of Stuff repository and merge them into your personal repo. Only system files are updated - personal content is completely protected by gitignore firewall.

## Command Formats
- `pull` → Fetch and apply system improvements with user approval
- `pull -preview` → Show what improvements are available (no changes applied)
- `pull -force` → Apply improvements without confirmation (use with caution)

---

## pull (Fetch and Apply)

### Step 1: Verify Prerequisites
**MANDATORY checks before proceeding:**

1. **Check git status:**
   ```bash
   git status
   ```
   - If uncommitted changes to system files exist, ask user to commit first
   - Personal files (gitignored) don't affect this check

2. **Verify gh CLI is installed:**
   ```bash
   gh --version
   ```

### Step 2: Fetch Global Repository Changes
**MANDATORY:** Pull latest changes from global repo:

```bash
gh repo clone wilson-becker/chief-of-stuff /tmp/chief-of-stuff-global -- --depth 1
```

### Step 3: Compare System Files
**MANDATORY:** Only compare these system files:

**System Files to Check:**
- `agent-instructions.md`
- `commands/` (all .md files)
- `utils/` (all files)  
- `README.md`
- `.cursorrules`
- `*.template.md` (any template files)

**Files to Skip:**
- `.gitignore` (hybrid file - handle manually if needed)
- All personal files (protected by gitignore)

### Step 4: Identify Differences
For each system file, check if global version differs:

```bash
diff -u ./agent-instructions.md /tmp/chief-of-stuff-global/agent-instructions.md
```

### Step 5: Present Changes for Approval
Show user what would change conversationally:

"I found [X] system improvements available from the global repo:

**📋 Available Updates:**

**agent-instructions.md:**
- Added new fallback instructions for command execution
- Improved error handling guidance

**commands/debloat.md:**
- New system audit command for maintaining consistency
- Helps identify bloat and confusion points

**commands/sync.md:**
- Enhanced MCP parameter mapping
- Added explicit date calculation instructions

**⚠️ Your Personal Files Are Safe:**
All your personal content (projects.md, tasks.md, user-context.md, etc.) will remain unchanged.

Would you like me to apply these improvements? (y/n)"

### Step 6: Backup Current System Files
**MANDATORY before applying changes:**

```bash
mkdir -p .backup/system-files-$(date +%Y%m%d-%H%M%S)
cp agent-instructions.md commands/*.md utils/* README.md .cursorrules .backup/system-files-$(date +%Y%m%d-%H%M%S)/
```

### Step 7: Apply Approved Changes
For each approved file:

1. **Simple replacement (no conflicts):**
   ```bash
   cp /tmp/chief-of-stuff-global/[file] ./[file]
   ```

2. **Merge conflicts detected:**
   Present conflict to user:
   "Conflict detected in `commands/sync.md`:
   
   **Your version:** [show local changes]
   **Global version:** [show global changes]
   
   How would you like to handle this?
   1. Keep your version
   2. Use global version  
   3. Let me help merge both
   4. Skip this file for now"

### Step 8: Commit Applied Changes
```bash
git add [updated system files]
git commit -m "Update system files from global repo

- Updated agent-instructions.md: improved fallback handling
- Added commands/debloat.md: system audit capabilities  
- Enhanced commands/sync.md: better MCP integration

Fetched from wilson-becker/chief-of-stuff on $(date)"
```

### Step 9: Cleanup and Confirm
```bash
rm -rf /tmp/chief-of-stuff-global
```

Present success message:
"✅ System improvements applied successfully!

**Updated Files:**
- [list of files that were updated]

**Backup Location:**
`.backup/system-files-[timestamp]/`

**Personal Files:**
All your personal content remains untouched and protected.

Your Chief of Stuff system is now up to date with the latest community improvements!"

---

## pull -preview (Preview Mode)

### Show Available Updates
1. **Fetch global repo to temp location**
2. **Compare system files**
3. **Present summary without applying:**

"📋 Available system improvements:

**New Files:**
- `commands/debloat.md` - System audit and cleanup command

**Updated Files:**
- `agent-instructions.md` - Enhanced error handling
- `commands/sync.md` - Better MCP integration

**No Changes:**
- `README.md`, `.cursorrules` - already up to date

**Your Personal Files:**
Protected by gitignore - no changes needed or possible.

Run `pull` to apply these improvements."

---

## pull -force (Force Mode)

**⚠️ Use with extreme caution!**

Applies all system file updates without user confirmation. Only use when you trust the global repo completely.

Same process as normal `pull` but skips Step 5 approval.

---

## Error Handling

### **Uncommitted Changes:**
"Found uncommitted changes to system files. Please commit your work first:
```bash
git add [files]
git commit -m "Your changes"
```
Then run `pull` again."

### **No Updates Available:**
"🎉 Your system files are already up to date with the global repository! No improvements to apply."

### **Network Issues:**
"Unable to fetch from global repository. Check your internet connection and try again."

### **Merge Conflicts:**
"Conflict detected in [file]. I've created a backup at `.backup/system-files-[timestamp]/`. 

Would you like me to:
1. Show you the conflicting sections
2. Help you resolve the conflict manually
3. Skip this file and continue with others"

### **Backup Failure:**
"Unable to create backup directory. Pull aborted for safety. Please ensure you have write permissions and sufficient disk space."

## Success Criteria
- Only system files updated, personal content completely protected
- All changes backed up before applying
- User maintains control over what gets applied
- Clear communication about what changed and why
- Seamless integration of community improvements
