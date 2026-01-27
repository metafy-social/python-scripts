#!/usr/bin/env python3
"""
Git Commit Message Generator

Automatically generates commit messages based on git changes analysis.
Supports Conventional Commits specification for consistent commit messages.
"""

import subprocess
import re
import sys
from typing import List, Dict, Tuple, Optional


class GitCommitMessageGenerator:
    """Generates commit messages based on git changes analysis."""

    # Conventional Commits types
    COMMIT_TYPES = {
        'feat': 'A new feature',
        'fix': 'A bug fix',
        'docs': 'Documentation only changes',
        'style': 'Changes that do not affect the meaning of the code',
        'refactor': 'A code change that neither fixes a bug nor adds a feature',
        'perf': 'A code change that improves performance',
        'test': 'Adding missing tests or correcting existing tests',
        'build': 'Changes that affect the build system or external dependencies',
        'ci': 'Changes to CI configuration files and scripts',
        'chore': 'Other changes that do not modify src or test files',
        'revert': 'Reverts a previous commit'
    }

    # File patterns for commit type detection
    FILE_PATTERNS = {
        'docs': [r'\.md$', r'\.txt$', r'\.rst$', r'README', r'LICENSE', r'CHANGELOG'],
        'test': [r'test', r'spec', r'__test__', r'\.test\.'],
        'build': [r'requirements\.txt', r'setup\.py', r'Makefile', r'\.toml$', r'\.json$'],
        'ci': [r'\.github', r'\.gitlab', r'\.travis', r'\.circleci', r'\.jenkins'],
        'style': [r'\.css$', r'\.scss$', r'\.less$']
    }

    def __init__(self):
        """Initialize the generator."""
        self.changed_files = []
        self.staged_files = []
        self.unstaged_files = []

    def run_git_command(self, command: List[str]) -> str:
        """
        Execute a git command and return the output.

        Args:
            command: List of command arguments

        Returns:
            Command output as string

        Raises:
            subprocess.CalledProcessError: If git command fails
        """
        try:
            result = subprocess.run(
                ['git'] + command,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error running git command: {e}", file=sys.stderr)
            sys.exit(1)

    def get_git_status(self) -> Dict[str, List[str]]:
        """
        Get git status information.

        Returns:
            Dictionary with 'staged', 'unstaged', 'untracked' file lists
        """
        status_output = self.run_git_command(['status', '--porcelain'])
        status = {
            'staged': [],
            'unstaged': [],
            'untracked': []
        }

        for line in status_output.split('\n'):
            if not line:
                continue

            status_code = line[:2]
            filename = line[3:].strip()

            if status_code[0] == 'A' or status_code[0] == 'M' or status_code[0] == 'D':
                status['staged'].append(filename)
            elif status_code[1] == 'M' or status_code[1] == 'D':
                status['unstaged'].append(filename)
            elif status_code == '??':
                status['untracked'].append(filename)

        return status

    def analyze_file_changes(self, filename: str) -> Dict[str, any]:
        """
        Analyze changes in a specific file.

        Args:
            filename: Path to the file

        Returns:
            Dictionary with change analysis
        """
        try:
            diff_output = self.run_git_command(['diff', '--cached', filename])
            if not diff_output:
                diff_output = self.run_git_command(['diff', filename])

            added_lines = len(re.findall(r'^\+', diff_output, re.MULTILINE))
            removed_lines = len(re.findall(r'^\-', diff_output, re.MULTILINE))

            # Check for specific patterns
            has_feature = bool(re.search(r'\b(feat|add|new|implement|create)\b', diff_output, re.IGNORECASE))
            has_fix = bool(re.search(r'\b(fix|bug|error|issue|resolve)\b', diff_output, re.IGNORECASE))
            has_refactor = bool(re.search(r'\b(refactor|restructure|reorganize|clean)\b', diff_output, re.IGNORECASE))

            return {
                'filename': filename,
                'added': added_lines,
                'removed': removed_lines,
                'has_feature': has_feature,
                'has_fix': has_fix,
                'has_refactor': has_refactor
            }
        except subprocess.CalledProcessError:
            return {
                'filename': filename,
                'added': 0,
                'removed': 0,
                'has_feature': False,
                'has_fix': False,
                'has_refactor': False
            }

    def detect_commit_type(self, files: List[str], changes: List[Dict]) -> str:
        """
        Detect the appropriate commit type based on file changes.

        Args:
            files: List of changed file paths
            changes: List of change analysis dictionaries

        Returns:
            Suggested commit type
        """
        # Check file patterns
        for commit_type, patterns in self.FILE_PATTERNS.items():
            for pattern in patterns:
                if any(re.search(pattern, file, re.IGNORECASE) for file in files):
                    return commit_type

        # Analyze change patterns
        total_added = sum(c['added'] for c in changes)
        total_removed = sum(c['removed'] for c in changes)

        has_feature = any(c['has_feature'] for c in changes)
        has_fix = any(c['has_fix'] for c in changes)
        has_refactor = any(c['has_refactor'] for c in changes)

        if has_fix:
            return 'fix'
        elif has_feature:
            return 'feat'
        elif has_refactor:
            return 'refactor'
        elif total_added > total_removed * 2:
            return 'feat'
        elif total_removed > total_added * 2:
            return 'refactor'
        else:
            return 'chore'

    def generate_scope(self, files: List[str]) -> Optional[str]:
        """
        Generate commit scope from file paths.

        Args:
            files: List of changed file paths

        Returns:
            Scope string or None
        """
        if not files:
            return None

        # Extract common directory prefix
        common_parts = []
        first_file_parts = files[0].split('/')

        for i, part in enumerate(first_file_parts[:-1]):
            if all(len(f.split('/')) > i + 1 and f.split('/')[i] == part for f in files):
                common_parts.append(part)
            else:
                break

        if common_parts:
            return '/'.join(common_parts)

        # If no common prefix, use first directory or filename
        first_file = files[0]
        if '/' in first_file:
            return first_file.split('/')[0]
        else:
            return None

    def generate_description(self, files: List[str], changes: List[Dict]) -> str:
        """
        Generate commit message description.

        Args:
            files: List of changed file paths
            changes: List of change analysis dictionaries

        Returns:
            Description string
        """
        if not files:
            return "update files"

        # Get main file name without extension
        main_file = files[0].split('/')[-1]
        main_file = re.sub(r'\.[^.]+$', '', main_file)

        # Count changes
        total_added = sum(c['added'] for c in changes)
        total_removed = sum(c['removed'] for c in changes)

        # Generate description based on patterns
        if any(c['has_fix'] for c in changes):
            return f"fix issue in {main_file}"
        elif any(c['has_feature'] for c in changes):
            return f"add {main_file} feature"
        elif any(c['has_refactor'] for c in changes):
            return f"refactor {main_file}"
        elif total_added > 0 and total_removed == 0:
            return f"add {main_file}"
        elif total_removed > total_added:
            return f"remove unused code in {main_file}"
        else:
            return f"update {main_file}"

    def generate_commit_message(self, commit_type: str, scope: Optional[str],
                                description: str, body: Optional[str] = None) -> str:
        """
        Generate a commit message in Conventional Commits format.

        Args:
            commit_type: Type of commit (feat, fix, etc.)
            scope: Optional scope
            description: Commit description
            body: Optional commit body

        Returns:
            Formatted commit message
        """
        if scope:
            header = f"{commit_type}({scope}): {description}"
        else:
            header = f"{commit_type}: {description}"

        if body:
            return f"{header}\n\n{body}"
        else:
            return header

    def suggest_commit_message(self) -> Tuple[str, str]:
        """
        Analyze git changes and suggest a commit message.

        Returns:
            Tuple of (commit_type, full_message)
        """
        status = self.get_git_status()

        # Get all changed files
        all_files = status['staged'] + status['unstaged'] + status['untracked']

        if not all_files:
            print("No changes detected. Nothing to commit.")
            sys.exit(0)

        # Analyze changes
        changes = []
        for file in all_files[:10]:  # Limit to first 10 files for performance
            change = self.analyze_file_changes(file)
            changes.append(change)

        # Detect commit type
        commit_type = self.detect_commit_type(all_files, changes)

        # Generate scope
        scope = self.generate_scope(all_files)

        # Generate description
        description = self.generate_description(all_files, changes)

        # Generate full message
        file_list = ', '.join(all_files[:5])
        if len(all_files) > 5:
            file_list += f" and {len(all_files) - 5} more"

        body = f"Modified files: {file_list}"

        message = self.generate_commit_message(commit_type, scope, description, body)

        return commit_type, message

    def interactive_mode(self):
        """Run in interactive mode to generate and customize commit message."""
        print("Analyzing git changes...\n")

        commit_type, suggested_message = self.suggest_commit_message()

        print("Suggested commit message:")
        print("-" * 60)
        print(suggested_message)
        print("-" * 60)
        print(f"\nCommit type: {commit_type} - {self.COMMIT_TYPES.get(commit_type, 'Unknown')}")
        print("\nAvailable commit types:")
        for ctype, desc in self.COMMIT_TYPES.items():
            print(f"  {ctype:10} - {desc}")

        print("\nOptions:")
        print("1. Use suggested message")
        print("2. Edit commit type")
        print("3. Edit description")
        print("4. Enter custom message")
        print("5. Cancel")

        choice = input("\nSelect option (1-5): ").strip()

        if choice == '1':
            return suggested_message
        elif choice == '2':
            new_type = input(f"Enter commit type (current: {commit_type}): ").strip()
            if new_type in self.COMMIT_TYPES:
                scope = self.generate_scope(self.get_git_status()['staged'] + self.get_git_status()['unstaged'])
                description = input("Enter description: ").strip()
                return self.generate_commit_message(new_type, scope, description)
            else:
                print("Invalid commit type. Using original.")
                return suggested_message
        elif choice == '3':
            description = input("Enter new description: ").strip()
            scope = self.generate_scope(self.get_git_status()['staged'] + self.get_git_status()['unstaged'])
            return self.generate_commit_message(commit_type, scope, description)
        elif choice == '4':
            return input("Enter custom commit message: ").strip()
        else:
            print("Cancelled.")
            sys.exit(0)


def main():
    """Main entry point."""
    generator = GitCommitMessageGenerator()

    # Check if we're in a git repository
    try:
        generator.run_git_command(['rev-parse', '--git-dir'])
    except subprocess.CalledProcessError:
        print("Error: Not a git repository. Please run this script in a git repository.")
        sys.exit(1)

    # Generate and display commit message
    commit_message = generator.interactive_mode()

    if commit_message:
        print("\n" + "=" * 60)
        print("Final commit message:")
        print("=" * 60)
        print(commit_message)
        print("=" * 60)

        use_message = input("\nUse this message for commit? (y/n): ").strip().lower()
        if use_message == 'y':
            try:
                subprocess.run(['git', 'commit', '-m', commit_message], check=True)
                print("\nCommit created successfully!")
            except subprocess.CalledProcessError as e:
                print(f"\nError creating commit: {e}")
                print("\nYou can manually use:")
                print(f'git commit -m "{commit_message}"')
        else:
            print("\nCommit cancelled. You can manually use:")
            print(f'git commit -m "{commit_message}"')


if __name__ == "__main__":
    main()
