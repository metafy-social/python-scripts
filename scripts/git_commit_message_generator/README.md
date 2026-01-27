# Git Commit Message Generator

A Python script that automatically generates commit messages based on git changes analysis. This tool helps save time writing commit messages and ensures consistency by supporting the [Conventional Commits](https://www.conventionalcommits.org/) specification.

## Features

- **Change Analysis**: Automatically analyzes git changes (added, modified, deleted files)
- **Commit Message Suggestions**: Generates appropriate commit messages based on file changes
- **Conventional Commits Support**: Follows Conventional Commits specification for consistent commit history
- **Interactive Mode**: Allows customization of suggested commit messages
- **Smart Type Detection**: Automatically detects commit type (feat, fix, docs, etc.) based on file patterns and changes

## Problem Statement

Writing good commit messages can be time-consuming and maintaining consistency across a project is challenging. This script automates the process by:

- Analyzing git changes to understand what was modified
- Suggesting appropriate commit messages following Conventional Commits format
- Reducing the time spent on writing commit messages
- Ensuring consistency in commit message style across the project

## Requirements

- Python 3.6 or higher
- Git installed and configured
- The script must be run in a git repository

## Installation

No external dependencies required. The script uses only Python standard library.

## Usage

1. Navigate to your git repository:
   ```bash
   cd /path/to/your/git/repository
   ```

2. Make some changes to your files (add, modify, or delete files)

3. Stage your changes (optional):
   ```bash
   git add .
   ```

4. Run the script:
   ```bash
   python script.py
   ```

5. Follow the interactive prompts:
   - Review the suggested commit message
   - Choose to use it, edit it, or create a custom message
   - Confirm to create the commit

## How It Works

1. **Change Detection**: The script analyzes git status to identify staged, unstaged, and untracked files
2. **File Analysis**: Examines file changes using `git diff` to understand what was added, removed, or modified
3. **Pattern Matching**: Detects commit type based on:
   - File patterns (e.g., `.md` files → `docs`, test files → `test`)
   - Change patterns (e.g., bug fixes → `fix`, new features → `feat`)
   - Code analysis (keywords in diffs)
4. **Message Generation**: Creates a commit message following Conventional Commits format:
   ```
   <type>(<scope>): <description>
   
   <body>
   ```

## Commit Types

The script supports the following Conventional Commits types:

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `build`: Changes that affect the build system or external dependencies
- `ci`: Changes to CI configuration files and scripts
- `chore`: Other changes that do not modify src or test files
- `revert`: Reverts a previous commit

## Examples

### Example 1: Adding a new feature
```bash
# After adding a new file: feature.py
$ python script.py

Suggested commit message:
------------------------------------------------------------
feat: add feature

Modified files: feature.py
------------------------------------------------------------
```

### Example 2: Fixing a bug
```bash
# After modifying buggy_code.py to fix an issue
$ python script.py

Suggested commit message:
------------------------------------------------------------
fix(buggy_code): fix issue in buggy_code

Modified files: buggy_code.py
------------------------------------------------------------
```

### Example 3: Documentation update
```bash
# After updating README.md
$ python script.py

Suggested commit message:
------------------------------------------------------------
docs: update README

Modified files: README.md
------------------------------------------------------------
```

## Interactive Options

When running the script, you'll be presented with options:

1. **Use suggested message**: Accept the generated message as-is
2. **Edit commit type**: Change the commit type (feat, fix, etc.)
3. **Edit description**: Modify the description part of the message
4. **Enter custom message**: Write your own commit message
5. **Cancel**: Exit without creating a commit

## Notes

- The script analyzes up to 10 files for performance reasons
- It works with both staged and unstaged changes
- If you choose not to auto-commit, you can manually use the suggested message
- The script must be run from within a git repository

## Future Improvements

- Support for breaking changes notation (`!`)
- Integration with git hooks for automatic message generation
- Support for multi-line commit bodies with detailed change descriptions
- Configuration file for custom commit type patterns
- Support for different commit message templates
- Integration with issue tracking systems (GitHub, GitLab, etc.)

## Author

Created as part of the Daily Python Scripts collection.
