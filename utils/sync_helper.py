#!/usr/bin/env python3
"""
Sync Helper Utility

Integrates with message_tracker.py to provide clean sync operations
that only process new messages.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from message_tracker import MessageTracker
from typing import List, Dict, Any

class SyncHelper:
    """Helper for sync operations with message deduplication"""
    
    def __init__(self):
        self.tracker = MessageTracker()
    
    def filter_new_slack_messages(self, messages_by_channel: Dict[str, Dict]) -> Dict[str, Dict]:
        """
        Filter slack messages to only include new (unprocessed) ones
        
        Args:
            messages_by_channel: Dict with channel names as keys, each containing:
                - 'messages': List of message dicts with 'ts' timestamps
                - 'messageCount': Total count
                - Other metadata
        
        Returns:
            Dict with same structure but only new messages
        """
        filtered_channels = {}
        
        for channel_name, channel_data in messages_by_channel.items():
            if 'messages' not in channel_data:
                # Handle error cases or channels without messages
                filtered_channels[channel_name] = channel_data
                continue
            
            # Filter out processed messages
            new_messages = self.tracker.filter_new_messages(channel_data['messages'])
            
            # Update the channel data
            filtered_channels[channel_name] = {
                **channel_data,  # Keep all original metadata
                'messages': new_messages,
                'messageCount': len(new_messages),
                'original_count': channel_data.get('messageCount', 0),
                'filtered_count': len(new_messages)
            }
        
        return filtered_channels
    
    def mark_messages_processed(self, messages_by_channel: Dict[str, Dict], 
                               action_taken: str = "processed during sync") -> None:
        """
        Mark messages as processed after they've been handled
        
        Args:
            messages_by_channel: Same format as filter_new_slack_messages input
            action_taken: Description of what was done with the messages
        """
        for channel_name, channel_data in messages_by_channel.items():
            if 'messages' not in channel_data:
                continue
            
            for message in channel_data['messages']:
                if 'ts' in message:
                    self.tracker.mark_processed(
                        timestamp=message['ts'],
                        channel=channel_name,
                        action_taken=action_taken
                    )
    
    def get_sync_summary(self) -> Dict[str, Any]:
        """Get summary of processed messages for reporting"""
        return {
            'total_processed': self.tracker.get_processed_count(),
            'user_inbox_count': len(self.tracker.get_processed_by_channel('user-inbox')),
            'team_channels_count': self.tracker.get_processed_count() - len(self.tracker.get_processed_by_channel('user-inbox'))
        }
    
    def cleanup_old_messages(self, days: int = 30) -> int:
        """Clean up old processed messages"""
        return self.tracker.cleanup_old_messages(days)

def main():
    """CLI interface for sync helper"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Sync helper with message deduplication")
    parser.add_argument('--summary', action='store_true', help="Show sync summary")
    parser.add_argument('--cleanup', type=int, metavar='DAYS', 
                       help="Clean up messages older than N days")
    
    args = parser.parse_args()
    helper = SyncHelper()
    
    if args.summary:
        summary = helper.get_sync_summary()
        print("📊 Sync Summary:")
        print(f"  Total processed messages: {summary['total_processed']}")
        print(f"  User inbox: {summary['user_inbox_count']}")
        print(f"  Team channels: {summary['team_channels_count']}")
    
    elif args.cleanup:
        removed = helper.cleanup_old_messages(args.cleanup)
        print(f"🧹 Cleaned up {removed} old messages")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
