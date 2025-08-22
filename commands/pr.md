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

### Step 3: Create Feature Branch
```bash
git checkout -b system-improvements-$(date +%Y%m%d)
```

### Step 4: Auto-Detect User Info and Sanitize System Files
**MANDATORY:** Remove all personal information from system files before PR:

1. **Detect user information:**
   ```bash
   USER_NAME=$(basename $(pwd) | sed 's/chief-of-stuff-//')
   USER_EMAIL=$(git config user.email)
   ```

2. **Create sanitized temp directory:**
   ```bash
   mkdir -p /tmp/pr-sanitized
   ```

3. **Copy and sanitize each system file:**
   ```bash
   # Replace personal references with generic ones
   sed -e "s/$USER_NAME/USER_NAME/g" \
       -e "s/$USER_EMAIL/USER_EMAIL/g" \
       -e "s/Wilson's/User's/g" \
       -e "s/Wilson /the user /g" \
       -e "s/chief-of-stuff-$USER_NAME/chief-of-stuff-USER/g" \
       -e "s/#$USER_NAME-inbox/#user-inbox/g" \
       agent-instructions.md > /tmp/pr-sanitized/agent-instructions.md
   
   # Copy other system files with sanitization
   cp -r commands/ /tmp/pr-sanitized/
   sed -e "s/$USER_NAME/USER_NAME/g" README.md > /tmp/pr-sanitized/README.md
   sed -e "s/$USER_NAME/USER_NAME/g" .cursorrules > /tmp/pr-sanitized/.cursorrules
   ```

### Step 5: Prepare PR Description
Generate description based on recent commits to system files:

```bash
git log --oneline --since="1 week ago" -- agent-instructions.md commands/ utils/ README.md .cursorrules
```

Format as:
```
## System Improvements

### Changes Made:
- [Improvement 1 with brief description]
- [Improvement 2 with brief description]

### Benefits for All Users:
- [How this helps the community]
- [What problems this solves]

### Files Changed:
- `agent-instructions.md` - [what changed]
- `commands/[file].md` - [what changed]

Tested in personal workflow and ready for community use.
```

### Step 6: Create Pull Request from Sanitized Files
```bash
# Change to sanitized directory
cd /tmp/pr-sanitized

# Initialize git and add sanitized files
git init
git add .
git commit -m "System improvements from $USER_NAME

[generated description from Step 5]"

# Create PR using sanitized files
gh pr create \
  --repo wilson-becker/chief-of-stuff \
  --title "System improvements: [brief summary]" \
  --body "[generated description from Step 5]" \
  --head system-improvements-$(date +%Y%m%d)
```

### Step 7: Cleanup and Confirm Success
```bash
# Return to original directory
cd - 

# Clean up sanitized files
rm -rf /tmp/pr-sanitized
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
