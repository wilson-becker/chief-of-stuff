#!/usr/bin/env python3
"""
Message Tracker Utility

Tracks processed Slack messages to avoid re-processing during sync operations.
Uses JSON storage for efficient lookups and maintains message history.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Set, Optional
# Removed unused dataclass imports - using simple dict structure now

# Simplified: Just store timestamp -> action_taken mapping
# No need for complex dataclass since we only need deduplication + context

class MessageTracker:
    """Manages processed message tracking with simplified structure"""
    
    def __init__(self, storage_path: str = "context/processed_messages.json"):
        self.storage_path = storage_path
        self.messages: Dict[str, str] = {}  # timestamp -> action_taken
        self.load_messages()
    
    def load_messages(self) -> None:
        """Load processed messages from JSON file"""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r') as f:
                    data = json.load(f)
                    # Handle both old and new formats
                    if data and isinstance(list(data.values())[0], dict):
                        # Old format: extract action_taken from complex objects
                        self.messages = {
                            ts: msg_data.get('action_taken', 'processed')
                            for ts, msg_data in data.items()
                        }
                    else:
                        # New format: direct timestamp -> action mapping
                        self.messages = data
            except (json.JSONDecodeError, FileNotFoundError):
                self.messages = {}
    
    def save_messages(self) -> None:
        """Save processed messages to JSON file"""
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        with open(self.storage_path, 'w') as f:
            json.dump(self.messages, f, indent=2, sort_keys=True)
    
    def is_processed(self, timestamp: str) -> bool:
        """Check if a message timestamp has been processed"""
        return timestamp in self.messages
    
    def mark_processed(self, timestamp: str, channel: str = "user-inbox", 
                      action_taken: str = "processed during sync") -> None:
        """Mark a message as processed"""
        self.messages[timestamp] = action_taken
        self.save_messages()
    
    def filter_new_messages(self, messages: List[Dict]) -> List[Dict]:
        """Filter out already processed messages from a list"""
        return [
            msg for msg in messages 
            if not self.is_processed(msg.get('ts', ''))
        ]
    
    def get_processed_count(self) -> int:
        """Get total count of processed messages"""
        return len(self.messages)
    
    def get_processed_by_channel(self, channel: str) -> List[str]:
        """Get all processed message timestamps (channel filtering removed since we only track one channel)"""
        return list(self.messages.keys())
    
    def cleanup_old_messages(self, days_to_keep: int = 30) -> int:
        """Remove processed messages older than specified days"""
        cutoff_date = datetime.now().timestamp() - (days_to_keep * 24 * 60 * 60)
        
        old_timestamps = [
            ts for ts in self.messages.keys()
            if float(ts) < cutoff_date
        ]
        
        for ts in old_timestamps:
            del self.messages[ts]
        
        if old_timestamps:
            self.save_messages()
        
        return len(old_timestamps)

def main():
    """CLI interface for message tracker"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Manage processed Slack messages")
    parser.add_argument('--check', help="Check if timestamp is processed")
    parser.add_argument('--mark', nargs=3, metavar=('TIMESTAMP', 'CHANNEL', 'ACTION'),
                       help="Mark message as processed")
    parser.add_argument('--count', action='store_true', help="Show processed message count")
    parser.add_argument('--cleanup', type=int, metavar='DAYS', 
                       help="Remove messages older than N days")
    parser.add_argument('--channel', help="Filter by channel")
    
    args = parser.parse_args()
    tracker = MessageTracker()
    
    if args.check:
        result = tracker.is_processed(args.check)
        print(f"Message {args.check}: {'PROCESSED' if result else 'NEW'}")
    
    elif args.mark:
        timestamp, channel, action = args.mark
        tracker.mark_processed(timestamp, channel, action)
        print(f"Marked message {timestamp} as processed")
    
    elif args.count:
        total = tracker.get_processed_count()
        print(f"Total processed messages: {total}")
        
        if args.channel:
            channel_msgs = tracker.get_processed_by_channel(args.channel)
            print(f"Messages in #{args.channel}: {len(channel_msgs)}")
    
    elif args.cleanup:
        removed = tracker.cleanup_old_messages(args.cleanup)
        print(f"Removed {removed} old messages")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
