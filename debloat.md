# Debloat Command - System Integrity Audit

## Purpose
Ensure the Chief of Stuff system is internally consistent, deterministic, and economical. Focus on core operational files that define system behavior - NOT user content. Verify that every command has exactly one execution path and eliminate bloat that creates misdirection or wastes context window.

## Command Formats
- `debloat` → Full system audit with recommendations
- `debloat -fix` → Run audit and implement high-priority fixes automatically
- `debloat -report` → Generate audit report only (no fixes)

---

## debloat (Full Audit)

### Step 1: Progressive Disclosure Audit
**Check consistency across entry points:**

1. **Read core files in order:**
   - `.cursorrules` 
   - `README.md`
   - `agent-instructions.md`

2. **Verify progressive disclosure path matches:**
   - Check that `.cursorrules` references match README.md
   - Verify agent-instructions.md aligns with both
   - Flag any contradictions in the disclosure sequence

3. **Check file structure consistency:**
   - Compare directory structures shown in each file
   - Verify actual files exist as documented
   - Flag missing or extra files

### Step 2: Command Consistency Audit
**Analyze all command files for deterministic execution:**

1. **Read all command files:**
   - `commands/menu.md` 
   - `commands/brag.md`
   - `commands/debloat.md`
   - `commands/pr.md`
   - `commands/update.md`
   - `commands/archive-messages.md`
   - Any other `.md` files in `commands/`

2. **Check for ambiguous instructions:**
   - Look for vague terms: "use appropriate", "as needed", "when possible"
   - Flag missing error handling scenarios
   - Identify unclear parameter specifications
   - Note missing fallback instructions

3. **Verify MCP tool references:**
   - Check all MCP tool names are current and correct
   - Verify parameter formats match tool specifications
   - Flag any mixing of tool parameter styles

### Step 3: User Context System Integration Audit
**Check user-context.md for system-relevant inconsistencies:**

1. **Read user-context.md:**
   - Focus on system-referenced elements (channel IDs, integrations)
   - Check for internal contradictions or bloat
   - Verify structure supports command execution

2. **Validate system dependencies:**
   - Confirm channel IDs referenced in sync commands exist and are correct
   - Check integration references (GitHub, Slack ID, Vault) are properly formatted
   - Flag any unused or redundant information that wastes context

3. **Skip user content files:**
   - Do NOT audit projects.md, tasks.md, reading-list.md, or project workspace files
   - These contain Wilson's work content, not system operational instructions

### Step 4: Memory Alignment Audit
**Compare memories with actual file contents:**

1. **Check each memory against current files:**
   - Verify memory facts match current file contents
   - Flag outdated preferences or contexts
   - Note contradictions between memories and files

2. **Identify memory gaps:**
   - Look for important patterns in files not captured in memories
   - Flag recent changes not reflected in memory

### Step 5: Bloat Detection
**Identify information that creates misdirection or wastes context window:**

1. **Redundant instructions:**
   - Find duplicate explanations across core system files
   - Identify repeated file structure descriptions
   - Flag verbose explanations that could be more economical

2. **Misdirection sources:**
   - Check for multiple ways to describe the same process
   - Identify conflicting guidance that could confuse execution path
   - Note unnecessary detail that obscures core instructions

3. **Context window waste:**
   - Flag overly verbose explanations in frequently-read files
   - Identify information that doesn't support command execution
   - Note structural descriptions that could be more concise

### Step 6: Generate Audit Report
Present findings conversationally:

"I ran a full system audit and found [X] issues to address:

**🚨 CRITICAL (Breaks Determinism):**
• [Inconsistency creating multiple execution paths]
• [Ambiguous instruction preventing reliable execution]

**⚠️ MAJOR (Reduces Reliability):**
• [System file inconsistency affecting command execution]
• [Missing error handling creating execution gaps]

**🔧 MINOR (Optimization):**
• [Small inconsistency in system files]
• [Minor formatting that could improve clarity]

**📊 BLOAT DETECTED (Context Window Waste):**
• [Redundant explanations across system files]
• [Verbose instructions that could be more economical]

Would you like me to implement the critical and major fixes automatically, or do you want to review them first?"

---

## debloat -fix (Auto-Fix Mode)

Execute the full audit, then automatically implement:
- **Critical fixes** (progressive disclosure, ambiguous instructions)
- **Major fixes** (outdated timestamps, memory updates)
- Skip minor and bloat issues (require human judgment)

Present summary of changes made and remaining manual items.

---

## debloat -report (Report Only)

Execute full audit but present detailed findings without making any changes:

"**SYSTEM AUDIT REPORT - [DATE]**

**Files Analyzed:** [count] core files, [count] command files, [count] data files
**Memories Checked:** [count] memories against current state
**Issues Found:** [count] critical, [count] major, [count] minor

**DETAILED FINDINGS:**

[Structured breakdown of all issues with file references and specific recommendations]

**RECOMMENDED ACTIONS:**
1. [Priority 1 fixes]
2. [Priority 2 fixes]
3. [Optional improvements]

This report can guide manual cleanup or be used with `debloat -fix` for automated fixes."

---

## Execution Rules
1. **Always run terminal `date` command first** to get current timestamp for freshness checks
2. **Read files systematically** - don't skip any core system files
3. **Be specific in findings** - include file names, line numbers when possible
4. **Categorize by impact** - critical vs nice-to-have
5. **Present actionable recommendations** - not just problems but solutions
6. **Update .cursorrules** to include debloat in command list after creation

## Success Criteria
- Every command has exactly one deterministic execution path
- Zero inconsistencies between core system files (.cursorrules, README.md, agent-instructions.md, commands/)
- All command instructions unambiguous with clear error handling
- Memories aligned with current system behavior
- System files are economical - no wasted context window or misdirection
- Progressive disclosure path is clear and consistent
