# Message Archive

This directory contains files for the message archiving system.

## Files

- **`processed_messages.json`** - Tracks which Slack messages have already been processed
- **`archive_metadata.template.json`** - Template for message archive metadata

## Purpose

Used by the sync and archive commands to avoid reprocessing the same messages and maintain proper archive structure.