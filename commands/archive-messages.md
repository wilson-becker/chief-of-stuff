# Archive Messages - LLM-Based Process

## When to Archive
When `message-archive/processed_messages.json` has >100 entries.

## Archival Steps

### Step 1: Calculate Cutoff Date
Calculate timestamp for 30 days ago:
- Current date minus 30 days
- Convert to Unix timestamp (seconds since 1970)
- Example: If today is 2025-01-17, cutoff date is 2025-12-18

### Step 2: Separate Messages
Read `message-archive/processed_messages.json` and separate:
- **Old messages:** timestamp < cutoff timestamp
- **Recent messages:** timestamp >= cutoff timestamp

### Step 3: Create Archive File
Use `write` tool to create `message-archive/archives/processed_messages_YYYY-MM.json`:
```json
{
  "1754575836.158519": "Back office segmentation doc added to domain knowledge tasks",
  "1754576454.870969": "Data warehouse clone task moved to completed tasks"
}
```

### Step 4: Update Active File
Use `write` tool to rewrite `message-archive/processed_messages.json` with only recent messages.

### Step 5: Create/Update Metadata
Use the template in `message-archive/archive_metadata.template.json`:
- Replace `REPLACE_WITH_OLDEST_RECENT_TIMESTAMP` with oldest timestamp from recent messages
- Replace `REPLACE_WITH_CURRENT_DATE` with current date
- Replace other placeholders with actual values
- Save as `message-archive/archives/archive_metadata.json`

## Success Message
Tell user: "Archived [X] old messages, kept [Y] recent messages for faster sync operations."

## If Archival Fails
Continue with sync - archival is optional for functionality.
