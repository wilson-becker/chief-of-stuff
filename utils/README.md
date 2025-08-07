# Utilities

Python utilities for the Chief of Stuff system.

## Message Tracking System

### `message_tracker.py`
Core utility for tracking processed Slack messages to avoid re-processing during sync operations.

**Features:**
- JSON-based storage for efficient lookups
- Automatic cleanup of old messages  
- CLI interface for manual operations
- Timestamp-based deduplication

**Usage:**
```bash
# Check if a message is processed
python3 utils/message_tracker.py --check "1754586153.006829"

# Mark a message as processed
python3 utils/message_tracker.py --mark "1754586153.006829" "user-inbox" "Integrated into project"

# Show count of processed messages
python3 utils/message_tracker.py --count

# Clean up old messages (30+ days)
python3 utils/message_tracker.py --cleanup 30
```

### `sync_helper.py`
High-level sync utility that integrates with message_tracker.py for clean sync operations.

**Features:**
- Filter new messages from Slack API results
- Mark batches of messages as processed
- Sync summary reporting
- Automatic cleanup scheduling

**Usage:**
```bash
# Show sync summary
python3 utils/sync_helper.py --summary

# Clean up old messages
python3 utils/sync_helper.py --cleanup 30
```

**Integration in sync process:**
```python
from utils.sync_helper import SyncHelper

helper = SyncHelper()

# Filter out already processed messages
new_messages = helper.filter_new_slack_messages(slack_api_results)

# Process only new messages...

# Mark them as processed
helper.mark_messages_processed(new_messages, "integrated into projects")
```

## Storage

- **Processed messages:** `context/processed_messages.json`
- **Format:** JSON with timestamp keys and message metadata
- **Automatic cleanup:** Messages older than 30 days are removed
- **Backup:** JSON format makes it easy to backup/restore message history

## Benefits

1. **Scalable:** JSON lookup is O(1) vs markdown scanning
2. **Programmatic:** Easy to integrate with sync automation  
3. **Maintainable:** Automatic cleanup prevents file bloat
4. **Debuggable:** CLI tools for manual inspection/correction
5. **Efficient:** Only processes genuinely new messages

---
*Last Updated: 2025-08-07*
