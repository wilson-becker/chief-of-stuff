# PR Command - Contribute System Improvements

## Purpose
Create a pull request to contribute system file improvements from your personal Chief of Stuff repo to the global template repository. Only system files are included - personal content is protected by gitignore firewall.

## Command Formats
- `pr` → Create pull request with all system file changes
- `pr -preview` → Show what would be included in PR (no actual PR created)

---

## pr (Create Pull Request)

### Step 1: Verify Prerequisites
**MANDATORY checks before proceeding:**

1. **Check git status:**
   ```bash
   git status
   ```
   - If there are uncommitted changes to system files, ask user to commit first
   - Personal files (gitignored) don't matter for this check

2. **Verify gh CLI is installed and authenticated:**
   ```bash
   gh auth status
   ```
   - If not authenticated, provide setup instructions

### Step 2: Identify System File Changes
**MANDATORY:** Only include these system files in PR:

**System Files (Always Include):**
- `agent-instructions.md`
- `commands/` (all .md files)
- `utils/` (all files)
- `README.md`
- `.cursorrules`
- `*.template.md` (any template files)

**Hybrid Files (Include with Care):**
- `.gitignore` (only if changes are framework-relevant)

**Personal Files (NEVER Include - Protected by Gitignore):**
- `user-context.md`
- `projects.md`
- `tasks.md`
- `reading-list.md`
- `brag-docs/`
- `projects/`
- `message-archive/processed_messages.json`

### Step 3: Auto-Detect User Info for Sanitization
**MANDATORY:** Detect personal information to sanitize before PR:

```bash
USER_NAME=$(basename $(pwd) | sed 's/chief-of-stuff-//')
USER_EMAIL=$(git config user.email)
echo "Detected user: $USER_NAME"
echo "Detected email: $USER_EMAIL"
```

### Step 4: Navigate to Global Repo and Create Feature Branch
**CRITICAL:** PR must be created from the global repo, not the personal repo:

```bash
cd ~/src/chief-of-stuff-global
git stash  # Stash any local changes
git checkout -b system-improvements-$(date +%Y%m%d)-v2
```

### Step 5: Create Sanitized Temp Directory and Copy Files
**MANDATORY:** Remove all personal information from system files:

1. **Create sanitized temp directory:**
   ```bash
   mkdir -p /tmp/pr-sanitized
   ```

2. **Copy and sanitize each system file from personal repo:**
   ```bash
   # Sanitize agent-instructions.md
   sed -e "s/$USER_NAME/USER_NAME/g" \
       -e "s/$USER_EMAIL/USER_EMAIL/g" \
       -e "s/Wilson's/User's/g" \
       -e "s/Wilson /the user /g" \
       -e "s/chief-of-stuff-$USER_NAME/chief-of-stuff-USER/g" \
       -e "s/#$USER_NAME-inbox/#user-inbox/g" \
       ~/src/chief-of-stuff-$USER_NAME/agent-instructions.md > /tmp/pr-sanitized/agent-instructions.md
   
   # Copy commands directory
   cp -r ~/src/chief-of-stuff-$USER_NAME/commands /tmp/pr-sanitized/
   
   # Sanitize README.md
   sed -e "s/$USER_NAME/USER_NAME/g" \
       -e "s/Wilson's/User's/g" \
       -e "s/Wilson /the user /g" \
       -e "s/chief-of-stuff-$USER_NAME/chief-of-stuff-USER/g" \
       ~/src/chief-of-stuff-$USER_NAME/README.md > /tmp/pr-sanitized/README.md
   
   # Sanitize .cursorrules
   sed -e "s/$USER_NAME/USER_NAME/g" \
       -e "s/Wilson's/User's/g" \
       -e "s/Wilson /the user /g" \
       ~/src/chief-of-stuff-$USER_NAME/.cursorrules > /tmp/pr-sanitized/.cursorrules
   ```

### Step 6: Copy Sanitized Files to Global Repo
```bash
# Copy sanitized files to global repo
cp /tmp/pr-sanitized/agent-instructions.md .
cp -r /tmp/pr-sanitized/commands .
cp /tmp/pr-sanitized/README.md .
cp /tmp/pr-sanitized/.cursorrules .
```

### Step 7: Prepare PR Description
Generate description based on recent commits to system files from personal repo:

```bash
cd ~/src/chief-of-stuff-$USER_NAME
git log --oneline --since="1 week ago" -- agent-instructions.md commands/ utils/ README.md .cursorrules
cd ~/src/chief-of-stuff-global
```

### Step 8: Commit Changes and Create Pull Request
```bash
# Add all changes in global repo
git add -A

# Commit with detailed description
git commit -m "System improvements: [brief summary]

## System Improvements

### Changes Made:
- [List improvements based on git log from Step 7]

### Benefits for All Users:
- [How this helps the community]
- [What problems this solves]

### Files Changed:
- agent-instructions.md - [what changed]
- commands/ - [what changed]

Tested in personal workflow and ready for community use."

# Push branch to origin
git push origin system-improvements-$(date +%Y%m%d)-v2

# Create PR
gh pr create \
  --title "System improvements: [brief summary]" \
  --body "## System Improvements

### Changes Made:
- **Add commands/pr.md**: Create pull requests with automatic sanitization
- **Add commands/update.md**: Fetch system improvements from global repo  
- **Add commands/debloat.md**: System audit for consistency and bloat
- **Move sync functionality into menu command** (menu sync, menu sync -i)
- **Delete commands/sync.md** (functionality moved to menu)

### Benefits for All Users:
- ✅ **Deterministic command execution** with clear error handling
- ✅ **Personal data protection** via gitignore firewall
- ✅ **System integrity auditing** capabilities
- ✅ **Community contribution workflow** (pr/update commands)

### Files Changed:
- \`agent-instructions.md\` - Remove personal references, add new commands
- \`commands/\` - Add pr.md, update.md, debloat.md; reorganize sync into menu
- \`README.md\` - Update to five core commands, remove old references
- \`.cursorrules\` - Add new commands, fix progressive disclosure

**🧪 Tested in personal workflow and ready for community use.**"
```

### Step 9: Cleanup and Return to Personal Repo
```bash
# Clean up sanitized files
rm -rf /tmp/pr-sanitized

# Return to personal repo and clean up feature branch
cd ~/src/chief-of-stuff-$USER_NAME
git checkout main
git branch -D system-improvements-$(date +%Y%m%d) 2>/dev/null || true
```
Present result conversationally:

"✅ Pull request created successfully!

**PR Details:**
- **Repository:** wilson-becker/chief-of-stuff
- **Branch:** system-improvements-[date]
- **Files included:** [list of changed system files]
- **URL:** [PR URL from gh CLI response]

Your system improvements are now ready for review. Once merged, other users can get these improvements with the `update` command.

Want me to clean up the feature branch, or keep it for potential updates?"

---

## pr -preview (Preview Mode)

### Show What Would Be Included
1. **Run git diff on system files only:**
   ```bash
   git diff HEAD~1 -- agent-instructions.md commands/ utils/ README.md .cursorrules *.template.md
   ```

2. **Present preview conversationally:**
   "Here's what would be included in your PR:

   **Changed System Files:**
   - `commands/debloat.md` - New system audit command
   - `agent-instructions.md` - Added fallback instructions
   - `.cursorrules` - Updated progressive disclosure

   **Summary of Changes:**
   [Brief description of improvements]

   **Personal Files Excluded (Protected):**
   - All your personal content is safely gitignored and won't be included

   Ready to create the actual PR with `pr`?"

---

## Error Handling

### **Uncommitted Changes:**
"I found uncommitted changes to system files. Please commit your work first:
```bash
git add [files]
git commit -m "Your commit message"
```
Then run `pr` again."

### **No Changes to System Files:**
"No changes detected in system files since last commit. Your personal files are safe in gitignore, but there's nothing new to contribute to the global repo."

### **Authentication Issues:**
"GitHub CLI isn't authenticated. Set it up first:
```bash
gh auth login
```
Then run `pr` again."

### **Network/API Issues:**
"Failed to create PR. Check your internet connection and try again. If the issue persists, you can create the PR manually at: https://github.com/wilson-becker/chief-of-stuff/compare"

## Success Criteria
- Only system files included in PR
- Personal content completely protected
- Clear PR description explaining benefits
- Proper branch naming and cleanup
- Community-ready improvements shared efficiently
