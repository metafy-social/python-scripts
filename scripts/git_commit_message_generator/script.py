"""
Git Commit Message Generator

Automatically generates commit messages based on git changes analysis.
Supports Conventional Commits specification for consistent commit messages.

Features:
- Intelligent commit type detection based on file patterns and diff content
- Breaking change detection
- Scope inference from file paths
- Interactive and non-interactive modes
- Cross-platform support (Windows/Linux/macOS)
- Colorized output
- Configuration via command-line arguments
"""

import subprocess
import re
import sys
import os
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any, Set
from dataclasses import dataclass
from enum import Enum


class Color:
    """ANSI color codes for terminal output."""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

    @classmethod
    def disable(cls):
        """Disable colors for non-TTY or Windows without ANSI support."""
        cls.RESET = ''
        cls.BOLD = ''
        cls.DIM = ''
        cls.RED = ''
        cls.GREEN = ''
        cls.YELLOW = ''
        cls.BLUE = ''
        cls.MAGENTA = ''
        cls.CYAN = ''
        cls.WHITE = ''


class CommitType(Enum):
    """Conventional Commits types with descriptions and emoji."""
    FEAT = ('feat', 'A new feature', '✨')
    FIX = ('fix', 'A bug fix', '🐛')
    DOCS = ('docs', 'Documentation only changes', '📚')
    STYLE = ('style', 'Changes that do not affect the meaning of the code', '💄')
    REFACTOR = ('refactor', 'A code change that neither fixes a bug nor adds a feature', '♻️')
    PERF = ('perf', 'A code change that improves performance', '⚡')
    TEST = ('test', 'Adding missing tests or correcting existing tests', '🧪')
    BUILD = ('build', 'Changes that affect the build system or external dependencies', '📦')
    CI = ('ci', 'Changes to CI configuration files and scripts', '👷')
    CHORE = ('chore', 'Other changes that do not modify src or test files', '🔧')
    REVERT = ('revert', 'Reverts a previous commit', '⏪')
    SECURITY = ('security', 'Security-related changes', '🔒')
    DEPS = ('deps', 'Dependency updates', '📌')
    CONFIG = ('config', 'Configuration changes', '⚙️')
    INIT = ('init', 'Initial commit or project initialization', '🎉')
    WIP = ('wip', 'Work in progress', '🚧')
    HOTFIX = ('hotfix', 'Critical hotfix', '🚑')
    RELEASE = ('release', 'Release/version tags', '🏷️')
    MERGE = ('merge', 'Merge branches', '🔀')
    I18N = ('i18n', 'Internationalization and localization', '🌐')
    A11Y = ('a11y', 'Accessibility improvements', '♿')
    UI = ('ui', 'UI/UX improvements', '🎨')
    API = ('api', 'API changes', '🔌')
    DB = ('db', 'Database related changes', '🗃️')

    @property
    def name_str(self) -> str:
        return self.value[0]

    @property
    def description(self) -> str:
        return self.value[1]

    @property
    def emoji(self) -> str:
        return self.value[2]


@dataclass
class FileChange:
    """Represents changes in a single file."""
    filename: str
    status: str = 'M'
    added_lines: int = 0
    removed_lines: int = 0
    is_binary: bool = False
    old_filename: Optional[str] = None
    has_feature_keywords: bool = False
    has_fix_keywords: bool = False
    has_refactor_keywords: bool = False
    has_perf_keywords: bool = False
    has_security_keywords: bool = False
    has_breaking_keywords: bool = False
    has_deprecation_keywords: bool = False
    has_todo_keywords: bool = False


@dataclass
class CommitSuggestion:
    """Represents a suggested commit message."""
    commit_type: str
    scope: Optional[str]
    description: str
    body: Optional[str]
    footer: Optional[str]
    is_breaking: bool = False
    emoji: Optional[str] = None

    def format(self, use_emoji: bool = False) -> str:
        """Format the commit message."""
        type_str = self.commit_type
        if self.is_breaking:
            type_str += '!'

        if use_emoji and self.emoji:
            type_str = f"{self.emoji} {type_str}"

        if self.scope:
            header = f"{type_str}({self.scope}): {self.description}"
        else:
            header = f"{type_str}: {self.description}"

        parts = [header]
        if self.body:
            parts.append('')
            parts.append(self.body)
        if self.footer:
            parts.append('')
            parts.append(self.footer)
        if self.is_breaking and 'BREAKING CHANGE' not in (self.footer or ''):
            parts.append('')
            parts.append('BREAKING CHANGE: This commit introduces breaking changes')

        return '\n'.join(parts)


class GitCommitMessageGenerator:
    """Generates commit messages based on git changes analysis."""

    FILE_PATTERNS: Dict[str, List[str]] = {
        'docs': [
            r'\.md$', r'\.mdx$', r'\.txt$', r'\.rst$', r'\.adoc$',
            r'README', r'LICENSE', r'CHANGELOG', r'CONTRIBUTING',
            r'AUTHORS', r'HISTORY', r'NOTICE', r'COPYING',
            r'docs[/\\]', r'documentation[/\\]', r'wiki[/\\]',
            r'\.docx?$', r'\.pdf$', r'man[/\\]',
        ],
        'test': [
            r'test[s]?[/\\]', r'spec[s]?[/\\]', r'__test__', r'__tests__',
            r'\.test\.', r'\.spec\.', r'_test\.', r'_spec\.',
            r'test_.*\.py$', r'.*_test\.py$', r'.*_test\.go$',
            r'\.feature$', r'fixtures[/\\]', r'mocks?[/\\]',
            r'conftest\.py$', r'pytest\.ini$', r'jest\.config\.',
            r'karma\.conf\.', r'cypress[/\\]', r'e2e[/\\]',
            r'\.snap$', r'__snapshots__',
        ],
        'build': [
            r'requirements.*\.txt$', r'setup\.py$', r'setup\.cfg$',
            r'pyproject\.toml$', r'Pipfile', r'poetry\.lock$',
            r'Makefile$', r'CMakeLists\.txt$', r'\.cmake$',
            r'package\.json$', r'package-lock\.json$', r'yarn\.lock$',
            r'pnpm-lock\.yaml$', r'\.npmrc$', r'\.yarnrc',
            r'Cargo\.toml$', r'Cargo\.lock$',
            r'go\.mod$', r'go\.sum$',
            r'Gemfile', r'\.gemspec$', r'Rakefile$',
            r'build\.gradle', r'pom\.xml$', r'\.mvn[/\\]',
            r'composer\.json$', r'composer\.lock$',
            r'mix\.exs$', r'rebar\.config$',
            r'\.cabal$', r'stack\.yaml$',
            r'vcpkg\.json$', r'conanfile\.',
            r'webpack\.', r'rollup\.', r'vite\.config\.',
            r'esbuild\.', r'parcel\.', r'snowpack\.',
            r'gulpfile\.', r'Gruntfile\.', r'grunt\.',
            r'Dockerfile', r'docker-compose', r'\.docker[/\\]',
            r'Vagrantfile$', r'\.vagrant[/\\]',
        ],
        'ci': [
            r'\.github[/\\]workflows', r'\.github[/\\]actions',
            r'\.gitlab-ci', r'\.gitlab[/\\]',
            r'\.travis\.yml$', r'\.travis[/\\]',
            r'\.circleci[/\\]', r'circle\.yml$',
            r'Jenkinsfile', r'\.jenkins[/\\]',
            r'azure-pipelines', r'\.azure[/\\]',
            r'bitbucket-pipelines', r'bamboo-specs',
            r'\.drone\.yml$', r'\.drone[/\\]',
            r'appveyor\.yml$', r'\.appveyor[/\\]',
            r'cloudbuild\.yaml$', r'\.gcloudignore$',
            r'buildspec\.yml$', r'\.aws[/\\]',
            r'codecov\.yml$', r'\.codecov\.yml$',
            r'\.coveragerc$', r'coverage\.', r'\.nyc',
            r'sonar-project\.properties$', r'\.sonarcloud',
            r'netlify\.toml$', r'vercel\.json$', r'now\.json$',
            r'heroku\.yml$', r'Procfile$', r'app\.yaml$',
            r'\.buildkite[/\\]', r'wercker\.yml$',
            r'tox\.ini$', r'noxfile\.py$',
        ],
        'style': [
            r'\.css$', r'\.scss$', r'\.sass$', r'\.less$', r'\.styl$',
            r'\.styled\.[jt]sx?$', r'styles?[/\\]',
            r'tailwind\.config\.', r'postcss\.config\.',
            r'\.prettierrc', r'\.prettier\.',
            r'\.eslintrc', r'\.eslint\.', r'eslint\.config\.',
            r'\.stylelintrc', r'stylelint\.config\.',
            r'\.editorconfig$', r'\.clang-format$',
            r'rustfmt\.toml$', r'\.rubocop\.yml$',
            r'phpcs\.xml', r'\.php-cs-fixer',
            r'checkstyle\.xml$', r'spotless\.',
        ],
        'config': [
            r'\.env', r'\.env\..*$', r'\.flaskenv$',
            r'config[/\\]', r'settings[/\\]', r'\.config[/\\]',
            r'\.ini$', r'\.cfg$', r'\.conf$', r'\.config$',
            r'\.yaml$', r'\.yml$', r'\.toml$',
            r'\.json$', r'\.json5$', r'\.jsonc$',
            r'\.xml$', r'\.properties$',
            r'tsconfig\.', r'jsconfig\.', r'babel\.config\.',
            r'\.babelrc', r'\.swcrc$',
            r'next\.config\.', r'nuxt\.config\.',
            r'angular\.json$', r'vue\.config\.',
            r'\.nvmrc$', r'\.node-version$', r'\.python-version$',
            r'\.ruby-version$', r'\.java-version$', r'\.tool-versions$',
        ],
        'security': [
            r'security[/\\]', r'auth[/\\]', r'authentication[/\\]',
            r'\.snyk$', r'snyk\.', r'security\.txt$',
            r'SECURITY\.md$', r'\.bandit$', r'\.safety$',
            r'\.dependabot[/\\]', r'dependabot\.yml$',
            r'renovate\.json', r'\.renovaterc',
        ],
        'deps': [
            r'requirements.*\.txt$', r'constraints\.txt$',
            r'package\.json$', r'package-lock\.json$',
            r'yarn\.lock$', r'pnpm-lock\.yaml$',
            r'Pipfile\.lock$', r'poetry\.lock$',
            r'Cargo\.lock$', r'go\.sum$',
            r'Gemfile\.lock$', r'composer\.lock$',
            r'mix\.lock$', r'packages\.lock\.json$',
            r'\.terraform\.lock\.hcl$',
        ],
        'i18n': [
            r'i18n[/\\]', r'l10n[/\\]', r'locales?[/\\]',
            r'translations?[/\\]', r'lang[/\\]', r'languages?[/\\]',
            r'\.po$', r'\.pot$', r'\.mo$',
            r'\.xlf$', r'\.xliff$', r'\.resx$',
            r'messages\.[a-z]{2}\.', r'\.[a-z]{2}\.json$',
        ],
        'db': [
            r'migrations?[/\\]', r'migrate[/\\]',
            r'schema[s]?[/\\]', r'seeds?[/\\]', r'fixtures[/\\]',
            r'\.sql$', r'\.prisma$', r'schema\.prisma$',
            r'\.graphql$', r'\.gql$',
            r'alembic[/\\]', r'flyway[/\\]', r'liquibase[/\\]',
            r'knexfile\.', r'sequelize\.', r'typeorm\.',
        ],
        'api': [
            r'api[/\\]', r'routes?[/\\]', r'endpoints?[/\\]',
            r'controllers?[/\\]', r'handlers?[/\\]',
            r'openapi\.', r'swagger\.', r'\.openapi\.',
            r'\.proto$', r'\.grpc\.', r'\.graphql$',
            r'resolvers?[/\\]', r'mutations?[/\\]', r'queries[/\\]',
        ],
        'ui': [
            r'components?[/\\]', r'views?[/\\]', r'pages?[/\\]',
            r'layouts?[/\\]', r'templates?[/\\]',
            r'\.vue$', r'\.svelte$', r'\.tsx$', r'\.jsx$',
            r'\.html$', r'\.htm$', r'\.pug$', r'\.ejs$',
            r'\.hbs$', r'\.handlebars$', r'\.mustache$',
            r'assets?[/\\]', r'images?[/\\]', r'icons?[/\\]',
            r'\.svg$', r'\.png$', r'\.jpg$', r'\.gif$', r'\.webp$',
            r'fonts?[/\\]', r'\.woff2?$', r'\.ttf$', r'\.eot$',
        ],
        'perf': [
            r'perf[/\\]', r'performance[/\\]', r'benchmark[s]?[/\\]',
            r'\.bench\.', r'_bench\.', r'profil',
        ],
    }

    DIFF_KEYWORDS: Dict[str, List[str]] = {
        'feature': [
            r'\b(add|added|adding|adds)\b',
            r'\b(implement|implemented|implementing|implements)\b',
            r'\b(create|created|creating|creates)\b',
            r'\b(introduce|introduced|introducing|introduces)\b',
            r'\b(new|feature|enhancement)\b',
            r'\b(support|supports|supporting)\b',
            r'\b(enable|enabled|enabling|enables)\b',
            r'\b(allow|allowed|allowing|allows)\b',
            r'\b(provide|provided|providing|provides)\b',
            r'\b(include|included|including|includes)\b',
        ],
        'fix': [
            r'\b(fix|fixed|fixing|fixes)\b',
            r'\b(bug|bugs|bugfix)\b',
            r'\b(error|errors)\b',
            r'\b(issue|issues)\b',
            r'\b(resolve|resolved|resolving|resolves)\b',
            r'\b(correct|corrected|correcting|corrects)\b',
            r'\b(repair|repaired|repairing|repairs)\b',
            r'\b(patch|patched|patching|patches)\b',
            r'\b(workaround)\b',
            r'\b(handle|handled|handling)\s+(error|exception|edge)',
            r'\b(prevent|prevented|preventing|prevents)\b',
            r'\b(address|addressed|addressing|addresses)\b',
        ],
        'refactor': [
            r'\b(refactor|refactored|refactoring|refactors)\b',
            r'\b(restructure|restructured|restructuring)\b',
            r'\b(reorganize|reorganized|reorganizing)\b',
            r'\b(clean|cleaned|cleaning|cleanup|cleanups)\b',
            r'\b(simplify|simplified|simplifying|simplifies)\b',
            r'\b(extract|extracted|extracting|extracts)\b',
            r'\b(move|moved|moving|moves)\b',
            r'\b(rename|renamed|renaming|renames)\b',
            r'\b(split|splitting|splits)\b',
            r'\b(merge|merged|merging|merges)\b',
            r'\b(consolidate|consolidated|consolidating)\b',
            r'\b(modularize|modularized|modularizing)\b',
            r'\b(decouple|decoupled|decoupling)\b',
        ],
        'perf': [
            r'\b(perf|performance)\b',
            r'\b(optimize|optimized|optimizing|optimizes|optimization)\b',
            r'\b(improve|improved|improving|improves)\s+(speed|performance|efficiency)',
            r'\b(faster|quicker|speed\s*up)\b',
            r'\b(reduce|reduced|reducing)\s+(memory|cpu|time|latency)',
            r'\b(cache|cached|caching|memoize|memoized)\b',
            r'\b(lazy|lazily|defer|deferred)\b',
            r'\b(parallelize|parallelized|async|concurrent)\b',
            r'\b(batch|batched|batching|bulk)\b',
            r'\b(index|indexed|indexing)\b',
        ],
        'security': [
            r'\b(security|secure|securing)\b',
            r'\b(vulnerability|vulnerabilities|vuln|CVE-)\b',
            r'\b(sanitize|sanitized|sanitizing|sanitization)\b',
            r'\b(escape|escaped|escaping)\b',
            r'\b(encrypt|encrypted|encrypting|encryption)\b',
            r'\b(auth|authenticate|authenticated|authentication)\b',
            r'\b(authorize|authorized|authorization)\b',
            r'\b(permission|permissions)\b',
            r'\b(csrf|xss|sqli|injection)\b',
            r'\b(token|tokens|jwt|oauth)\b',
            r'\b(secret|secrets|credential|credentials)\b',
            r'\b(password|passwords|passphrase)\b',
            r'\b(hash|hashed|hashing|bcrypt|argon)\b',
        ],
        'breaking': [
            r'\b(breaking|break|breaks)\b',
            r'\b(remove|removed|removing|removes)\s+(api|method|function|class|feature)',
            r'\b(delete|deleted|deleting|deletes)\s+(api|method|function|class)',
            r'\b(deprecate|deprecated|deprecating|deprecation)\b',
            r'\b(incompatible|incompatibility)\b',
            r'\b(major\s+version|major\s+change|major\s+update)\b',
            r'\b(migration\s+required|requires\s+migration)\b',
            r'BREAKING[\s_-]?CHANGE',
        ],
        'deprecation': [
            r'\b(deprecate|deprecated|deprecating|deprecation)\b',
            r'\b(obsolete|obsoleted)\b',
            r'\b(legacy)\b',
            r'@deprecated',
            r'DeprecationWarning',
            r'DEPRECATED',
        ],
        'todo': [
            r'\bTODO\b',
            r'\bFIXME\b',
            r'\bHACK\b',
            r'\bXXX\b',
            r'\bWIP\b',
            r'\bTEMP\b',
        ],
    }

    SCOPE_MAPPINGS: Dict[str, Optional[str]] = {
        'src': None,
        'lib': None,
        'app': None,
        'pkg': None,
        'internal': None,
        'cmd': None,
        'components': 'components',
        'pages': 'pages',
        'views': 'views',
        'controllers': 'controllers',
        'models': 'models',
        'services': 'services',
        'utils': 'utils',
        'helpers': 'helpers',
        'hooks': 'hooks',
        'store': 'store',
        'redux': 'redux',
        'api': 'api',
        'routes': 'routes',
        'middleware': 'middleware',
        'plugins': 'plugins',
        'modules': 'modules',
        'core': 'core',
        'common': 'common',
        'shared': 'shared',
        'features': 'features',
        'domain': 'domain',
        'infrastructure': 'infra',
        'presentation': 'presentation',
        'tests': 'tests',
        'test': 'test',
        'specs': 'specs',
        '__tests__': 'tests',
        'e2e': 'e2e',
        'integration': 'integration',
        'unit': 'unit',
        'docs': 'docs',
        'documentation': 'docs',
        'scripts': 'scripts',
        'tools': 'tools',
        'build': 'build',
        'config': 'config',
        'configs': 'config',
        'assets': 'assets',
        'static': 'static',
        'public': 'public',
        'styles': 'styles',
        'css': 'styles',
        'i18n': 'i18n',
        'locales': 'i18n',
        'migrations': 'db',
        'database': 'db',
        'db': 'db',
    }

    def __init__(self, use_emoji: bool = False, no_color: bool = False):
        """Initialize the generator."""
        self.use_emoji = use_emoji
        self.file_changes: List[FileChange] = []

        if no_color or not sys.stdout.isatty():
            Color.disable()

        if sys.platform == 'win32':
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except Exception:
                Color.disable()

    def run_git_command(self, command: List[str], check: bool = True) -> Tuple[str, int]:
        """Execute a git command and return the output."""
        try:
            result = subprocess.run(
                ['git', '--no-pager'] + command,
                capture_output=True,
                text=True,
                check=False,
                encoding='utf-8',
                errors='replace'
            )

            if check and result.returncode != 0:
                raise subprocess.CalledProcessError(
                    result.returncode,
                    ['git'] + command,
                    result.stdout,
                    result.stderr
                )

            return result.stdout.strip(), result.returncode
        except FileNotFoundError:
            self._print_error("Git is not installed or not in PATH")
            sys.exit(1)

    def _print_error(self, message: str):
        """Print an error message."""
        print(f"{Color.RED}Error: {message}{Color.RESET}", file=sys.stderr)

    def _print_warning(self, message: str):
        """Print a warning message."""
        print(f"{Color.YELLOW}Warning: {message}{Color.RESET}", file=sys.stderr)

    def _print_success(self, message: str):
        """Print a success message."""
        print(f"{Color.GREEN}{message}{Color.RESET}")

    def _print_info(self, message: str):
        """Print an info message."""
        print(f"{Color.CYAN}{message}{Color.RESET}")

    def is_git_repository(self) -> bool:
        """Check if current directory is a git repository."""
        _, code = self.run_git_command(['rev-parse', '--git-dir'], check=False)
        return code == 0

    def get_git_root(self) -> Optional[str]:
        """Get the root directory of the git repository."""
        output, code = self.run_git_command(['rev-parse', '--show-toplevel'], check=False)
        return output if code == 0 else None

    def get_current_branch(self) -> str:
        """Get the current branch name."""
        output, _ = self.run_git_command(['branch', '--show-current'], check=False)
        if not output:
            output, _ = self.run_git_command(['rev-parse', '--short', 'HEAD'], check=False)
            return f"HEAD@{output}" if output else "HEAD"
        return output

    def get_git_status(self) -> Dict[str, List[Any]]:
        """Get git status information."""
        status_output, _ = self.run_git_command(['status', '--porcelain', '-uall'])
        status: Dict[str, List[Any]] = {
            'staged': [],
            'unstaged': [],
            'untracked': [],
            'renamed': [],
            'deleted': [],
            'conflicted': []
        }

        for line in status_output.split('\n'):
            if not line:
                continue

            index_status = line[0]
            worktree_status = line[1]
            filename = line[3:]

            if ' -> ' in filename:
                old_name, new_name = filename.split(' -> ')
                filename = new_name.strip()
                status['renamed'].append((old_name.strip(), filename))

            if index_status in 'AMDRC':
                status['staged'].append(filename)
                if index_status == 'D':
                    status['deleted'].append(filename)

            if worktree_status in 'MD':
                status['unstaged'].append(filename)
                if worktree_status == 'D':
                    status['deleted'].append(filename)

            if index_status == '?' and worktree_status == '?':
                status['untracked'].append(filename)

            if index_status == 'U' or worktree_status == 'U' or (index_status == worktree_status == 'A'):
                status['conflicted'].append(filename)

        return status

    def get_staged_diff(self) -> str:
        """Get the full diff of staged changes."""
        output, _ = self.run_git_command(['diff', '--cached', '--unified=3'], check=False)
        return output

    def get_unstaged_diff(self) -> str:
        """Get the full diff of unstaged changes."""
        output, _ = self.run_git_command(['diff', '--unified=3'], check=False)
        return output

    def analyze_file_changes(self, filename: str, staged: bool = True) -> FileChange:
        """Analyze changes in a specific file."""
        change = FileChange(filename=filename, status='M')

        diff_cmd = ['diff', '--cached', filename] if staged else ['diff', filename]
        diff_output, code = self.run_git_command(diff_cmd, check=False)

        if code != 0:
            diff_output, _ = self.run_git_command(['diff', filename], check=False)

        if not diff_output:
            status_output, _ = self.run_git_command(['status', '--porcelain', filename], check=False)
            if status_output.startswith('A'):
                change.status = 'A'
            elif status_output.startswith('D') or (len(status_output) > 1 and status_output[1] == 'D'):
                change.status = 'D'
            return change

        if 'Binary files' in diff_output or '\x00' in diff_output:
            change.is_binary = True
            return change

        change.added_lines = len(re.findall(r'^\+(?!\+\+)', diff_output, re.MULTILINE))
        change.removed_lines = len(re.findall(r'^-(?!--)', diff_output, re.MULTILINE))

        for keyword_type, patterns in self.DIFF_KEYWORDS.items():
            for pattern in patterns:
                if re.search(pattern, diff_output, re.IGNORECASE):
                    if keyword_type == 'feature':
                        change.has_feature_keywords = True
                    elif keyword_type == 'fix':
                        change.has_fix_keywords = True
                    elif keyword_type == 'refactor':
                        change.has_refactor_keywords = True
                    elif keyword_type == 'perf':
                        change.has_perf_keywords = True
                    elif keyword_type == 'security':
                        change.has_security_keywords = True
                    elif keyword_type == 'breaking':
                        change.has_breaking_keywords = True
                    elif keyword_type == 'deprecation':
                        change.has_deprecation_keywords = True
                    elif keyword_type == 'todo':
                        change.has_todo_keywords = True
                    break

        return change

    def detect_commit_type_from_files(self, files: List[str]) -> Optional[str]:
        """Detect commit type based on file patterns."""
        normalized_files = [f.replace('\\', '/') for f in files]
        scores: Dict[str, int] = {}

        for commit_type, patterns in self.FILE_PATTERNS.items():
            for pattern in patterns:
                for file in normalized_files:
                    if re.search(pattern, file, re.IGNORECASE):
                        scores[commit_type] = scores.get(commit_type, 0) + 1

        if scores:
            return max(scores, key=lambda k: scores[k])

        return None

    def detect_commit_type(self, files: List[str], changes: List[FileChange]) -> Tuple[str, bool]:
        """Detect the appropriate commit type based on file changes."""
        is_breaking = any(c.has_breaking_keywords for c in changes)

        if any(c.has_security_keywords for c in changes):
            return 'security', is_breaking

        file_type = self.detect_commit_type_from_files(files)

        total_added = sum(c.added_lines for c in changes)
        total_removed = sum(c.removed_lines for c in changes)

        has_feature = any(c.has_feature_keywords for c in changes)
        has_fix = any(c.has_fix_keywords for c in changes)
        has_refactor = any(c.has_refactor_keywords for c in changes)
        has_perf = any(c.has_perf_keywords for c in changes)

        if file_type in ['test', 'docs', 'ci', 'i18n', 'db']:
            return file_type, is_breaking

        if file_type == 'security':
            return 'security', is_breaking

        if has_perf:
            return 'perf', is_breaking

        if has_fix and not has_feature:
            return 'fix', is_breaking

        if has_feature:
            return 'feat', is_breaking

        if has_refactor:
            return 'refactor', is_breaking

        if file_type in ['style', 'config']:
            return file_type, is_breaking

        if file_type == 'deps':
            return 'deps', is_breaking

        if file_type == 'build':
            return 'build', is_breaking

        if file_type == 'ui':
            return 'ui', is_breaking

        if file_type == 'api':
            return 'api', is_breaking

        if total_added > 0 and total_removed == 0:
            return 'feat', is_breaking
        elif total_removed > total_added * 3:
            return 'refactor', is_breaking
        elif total_added > total_removed * 3:
            return 'feat', is_breaking

        return 'chore', is_breaking

    def generate_scope(self, files: List[str]) -> Optional[str]:
        """Generate commit scope from file paths."""
        if not files:
            return None

        normalized_files = [Path(f).as_posix() for f in files]
        all_parts = [f.split('/') for f in normalized_files]

        if len(all_parts) == 1:
            parts = all_parts[0]
        else:
            common_parts = []
            for i in range(min(len(p) for p in all_parts)):
                if len(set(p[i] for p in all_parts)) == 1:
                    common_parts.append(all_parts[0][i])
                else:
                    break
            parts = common_parts if common_parts else all_parts[0]

        for part in parts[:-1]:
            part_lower = part.lower()
            if part_lower in self.SCOPE_MAPPINGS:
                mapped = self.SCOPE_MAPPINGS[part_lower]
                if mapped:
                    return mapped

        for part in parts[:-1]:
            part_lower = part.lower()
            if part_lower not in ['src', 'lib', 'app', 'pkg', 'internal', 'cmd', '.']:
                scope = re.sub(r'[^a-zA-Z0-9-]', '', part)
                if scope and len(scope) <= 20:
                    return scope.lower()

        if len(files) == 1:
            filename = Path(files[0]).stem
            scope = re.sub(r'[^a-zA-Z0-9-]', '', filename)
            if scope and len(scope) <= 15:
                return scope.lower()

        return None

    def generate_description(self, files: List[str], changes: List[FileChange],
                             commit_type: str) -> str:
        """Generate commit message description."""
        if not files:
            return "update files"

        main_file = Path(files[0]).stem
        main_file = re.sub(r'^[._]', '', main_file)
        main_file = re.sub(r'[-_.]', ' ', main_file)

        total_added = sum(c.added_lines for c in changes)
        total_removed = sum(c.removed_lines for c in changes)
        num_files = len(files)

        new_files = [c for c in changes if c.status == 'A']
        deleted_files = [c for c in changes if c.status == 'D']
        renamed_files = [c for c in changes if c.old_filename]

        if commit_type == 'docs':
            if num_files == 1:
                return f"update {main_file} documentation"
            return f"update documentation ({num_files} files)"

        elif commit_type == 'test':
            if num_files == 1:
                return f"add tests for {main_file}"
            return f"update tests ({num_files} files)"

        elif commit_type == 'ci':
            if num_files == 1:
                return f"update {main_file} configuration"
            return "update CI/CD configuration"

        elif commit_type == 'build':
            if 'requirements' in files[0].lower():
                return "update Python dependencies"
            elif 'package.json' in files[0].lower():
                return "update npm dependencies"
            elif 'cargo' in files[0].lower():
                return "update Rust dependencies"
            elif 'go.mod' in files[0].lower():
                return "update Go dependencies"
            return "update build configuration"

        elif commit_type == 'deps':
            return "update dependencies"

        elif commit_type == 'security':
            if any(c.has_security_keywords for c in changes):
                return "fix security vulnerability"
            return "improve security"

        elif commit_type == 'perf':
            return f"improve performance in {main_file}"

        elif commit_type == 'i18n':
            return "update translations"

        elif commit_type == 'db':
            if 'migration' in files[0].lower():
                return "add database migration"
            return "update database schema"

        elif commit_type == 'config':
            return f"update {main_file} configuration"

        elif commit_type == 'style':
            if any('css' in f.lower() or 'scss' in f.lower() or 'style' in f.lower() for f in files):
                return "update styles"
            return "format code"

        elif commit_type == 'fix':
            if num_files == 1:
                return f"fix issue in {main_file}"
            return f"fix issues ({num_files} files)"

        elif commit_type == 'feat':
            if len(new_files) == num_files:
                if num_files == 1:
                    return f"add {main_file}"
                return f"add new files ({num_files} files)"
            if num_files == 1:
                return f"add {main_file} feature"
            return f"add new features ({num_files} files)"

        elif commit_type == 'refactor':
            if renamed_files:
                return f"rename {main_file}"
            if num_files == 1:
                return f"refactor {main_file}"
            return f"refactor code ({num_files} files)"

        elif commit_type == 'ui':
            return f"update {main_file} UI"

        elif commit_type == 'api':
            return f"update {main_file} API"

        if len(deleted_files) == num_files:
            return f"remove {main_file}" if num_files == 1 else f"remove files ({num_files} files)"

        if len(new_files) == num_files:
            return f"add {main_file}" if num_files == 1 else f"add files ({num_files} files)"

        if renamed_files:
            return f"rename {main_file}"

        if total_removed > total_added * 2:
            return f"remove unused code in {main_file}"

        if total_added > total_removed * 2:
            return f"expand {main_file}"

        return f"update {main_file}"

    def generate_body(self, files: List[str], changes: List[FileChange]) -> Optional[str]:
        """Generate commit message body."""
        lines = []

        if len(files) > 1:
            lines.append("Changes:")
            for f in files[:10]:
                change = next((c for c in changes if c.filename == f), None)
                if change:
                    if change.status == 'A':
                        status = '+'
                    elif change.status == 'D':
                        status = '-'
                    elif change.old_filename:
                        status = 'R'
                    else:
                        status = 'M'
                    lines.append(f"  {status} {f}")
                else:
                    lines.append(f"  M {f}")

            if len(files) > 10:
                lines.append(f"  ... and {len(files) - 10} more files")

        total_added = sum(c.added_lines for c in changes)
        total_removed = sum(c.removed_lines for c in changes)

        if total_added > 0 or total_removed > 0:
            if lines:
                lines.append("")
            lines.append(f"Stats: +{total_added}/-{total_removed} lines")

        return '\n'.join(lines) if lines else None

    def generate_footer(self, changes: List[FileChange]) -> Optional[str]:
        """Generate commit message footer."""
        footers = []

        if any(c.has_breaking_keywords for c in changes):
            footers.append("BREAKING CHANGE: This commit contains breaking changes")

        if any(c.has_deprecation_keywords for c in changes):
            footers.append("Deprecated: This commit deprecates some functionality")

        return '\n'.join(footers) if footers else None

    def get_commit_emoji(self, commit_type: str) -> Optional[str]:
        """Get emoji for commit type."""
        for ct in CommitType:
            if ct.name_str == commit_type:
                return ct.emoji
        return None

    def suggest_commit_message(self, include_untracked: bool = False,
                               staged_only: bool = False) -> CommitSuggestion:
        """Analyze git changes and suggest a commit message."""
        status = self.get_git_status()

        if staged_only:
            all_files = status['staged']
        else:
            all_files = status['staged'] + status['unstaged']
            if include_untracked:
                all_files += status['untracked']

        seen: Set[str] = set()
        unique_files = []
        for f in all_files:
            if f not in seen:
                seen.add(f)
                unique_files.append(f)
        all_files = unique_files

        if not all_files:
            raise ValueError("No changes detected. Nothing to commit.")

        changes: List[FileChange] = []
        for file in all_files[:20]:
            staged = file in status['staged']
            change = self.analyze_file_changes(file, staged=staged)
            changes.append(change)

        self.file_changes = changes

        commit_type, is_breaking = self.detect_commit_type(all_files, changes)
        scope = self.generate_scope(all_files)
        description = self.generate_description(all_files, changes, commit_type)
        body = self.generate_body(all_files, changes)
        footer = self.generate_footer(changes)
        emoji = self.get_commit_emoji(commit_type)

        return CommitSuggestion(
            commit_type=commit_type,
            scope=scope,
            description=description,
            body=body,
            footer=footer,
            is_breaking=is_breaking,
            emoji=emoji
        )

    def print_commit_types(self):
        """Print available commit types."""
        print(f"\n{Color.BOLD}Available commit types:{Color.RESET}")
        for ct in CommitType:
            if self.use_emoji:
                print(f"  {ct.emoji} {Color.CYAN}{ct.name_str:12}{Color.RESET} - {ct.description}")
            else:
                print(f"  {Color.CYAN}{ct.name_str:12}{Color.RESET} - {ct.description}")

    def print_status_summary(self, status: Dict[str, List[Any]]):
        """Print git status summary."""
        print(f"\n{Color.BOLD}Git Status:{Color.RESET}")

        if status['staged']:
            print(f"  {Color.GREEN}Staged:{Color.RESET} {len(status['staged'])} file(s)")
        if status['unstaged']:
            print(f"  {Color.YELLOW}Modified:{Color.RESET} {len(status['unstaged'])} file(s)")
        if status['untracked']:
            print(f"  {Color.RED}Untracked:{Color.RESET} {len(status['untracked'])} file(s)")
        if status['conflicted']:
            print(f"  {Color.RED}{Color.BOLD}Conflicted:{Color.RESET} {len(status['conflicted'])} file(s)")
        if status['deleted']:
            print(f"  {Color.RED}Deleted:{Color.RESET} {len(status['deleted'])} file(s)")

    def interactive_mode(self, staged_only: bool = False) -> Optional[str]:
        """Run in interactive mode to generate and customize commit message."""
        self._print_info("Analyzing git changes...\n")

        status = self.get_git_status()
        self.print_status_summary(status)

        if status['conflicted']:
            self._print_error("You have unresolved merge conflicts. Please resolve them first.")
            for f in status['conflicted']:
                print(f"  - {f}")
            return None

        try:
            suggestion = self.suggest_commit_message(staged_only=staged_only)
        except ValueError as e:
            self._print_error(str(e))
            return None

        formatted_message = suggestion.format(use_emoji=self.use_emoji)

        print(f"\n{Color.BOLD}Suggested commit message:{Color.RESET}")
        print("-" * 60)
        print(f"{Color.GREEN}{formatted_message}{Color.RESET}")
        print("-" * 60)

        print(f"\n{Color.BOLD}Detected type:{Color.RESET} {Color.CYAN}{suggestion.commit_type}{Color.RESET}", end='')
        if suggestion.is_breaking:
            print(f" {Color.RED}(BREAKING CHANGE){Color.RESET}")
        else:
            print()

        if suggestion.scope:
            print(f"{Color.BOLD}Scope:{Color.RESET} {suggestion.scope}")

        self.print_commit_types()

        print(f"\n{Color.BOLD}Options:{Color.RESET}")
        print("  1. Use suggested message")
        print("  2. Edit commit type")
        print("  3. Edit scope")
        print("  4. Edit description")
        print("  5. Toggle breaking change")
        print("  6. Enter custom message")
        print("  7. Show diff")
        print("  8. Cancel")

        while True:
            try:
                choice = input(f"\n{Color.CYAN}Select option (1-8):{Color.RESET} ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nCancelled.")
                return None

            if choice == '1':
                return formatted_message

            elif choice == '2':
                valid_types = [ct.name_str for ct in CommitType]
                new_type = input(f"Enter commit type (current: {suggestion.commit_type}): ").strip().lower()
                if new_type in valid_types:
                    suggestion.commit_type = new_type
                    suggestion.emoji = self.get_commit_emoji(new_type)
                    formatted_message = suggestion.format(use_emoji=self.use_emoji)
                    print(f"\n{Color.GREEN}Updated message:{Color.RESET}\n{formatted_message}")
                else:
                    self._print_warning(f"Invalid commit type. Valid types: {', '.join(valid_types[:6])}...")

            elif choice == '3':
                new_scope = input(f"Enter scope (current: {suggestion.scope or 'none'}, empty to remove): ").strip()
                suggestion.scope = new_scope if new_scope else None
                formatted_message = suggestion.format(use_emoji=self.use_emoji)
                print(f"\n{Color.GREEN}Updated message:{Color.RESET}\n{formatted_message}")

            elif choice == '4':
                new_desc = input(f"Enter description (current: {suggestion.description}): ").strip()
                if new_desc:
                    suggestion.description = new_desc
                    formatted_message = suggestion.format(use_emoji=self.use_emoji)
                    print(f"\n{Color.GREEN}Updated message:{Color.RESET}\n{formatted_message}")

            elif choice == '5':
                suggestion.is_breaking = not suggestion.is_breaking
                formatted_message = suggestion.format(use_emoji=self.use_emoji)
                status_str = "enabled" if suggestion.is_breaking else "disabled"
                print(f"\n{Color.YELLOW}Breaking change {status_str}{Color.RESET}")
                print(f"\n{Color.GREEN}Updated message:{Color.RESET}\n{formatted_message}")

            elif choice == '6':
                custom = input("Enter custom commit message: ").strip()
                if custom:
                    return custom

            elif choice == '7':
                print(f"\n{Color.BOLD}Staged diff:{Color.RESET}")
                print("-" * 60)
                diff = self.get_staged_diff()
                if diff:
                    for line in diff.split('\n')[:50]:
                        if line.startswith('+') and not line.startswith('+++'):
                            print(f"{Color.GREEN}{line}{Color.RESET}")
                        elif line.startswith('-') and not line.startswith('---'):
                            print(f"{Color.RED}{line}{Color.RESET}")
                        elif line.startswith('@@'):
                            print(f"{Color.CYAN}{line}{Color.RESET}")
                        else:
                            print(line)
                    if diff.count('\n') > 50:
                        print(f"\n{Color.DIM}... (truncated, {diff.count(chr(10)) - 50} more lines){Color.RESET}")
                else:
                    print("No staged changes to show.")
                print("-" * 60)

            elif choice == '8':
                print("Cancelled.")
                return None

            else:
                print("Invalid option. Please select 1-8.")

    def quick_mode(self, staged_only: bool = False) -> str:
        """Generate commit message without interaction."""
        suggestion = self.suggest_commit_message(staged_only=staged_only)
        return suggestion.format(use_emoji=self.use_emoji)

    def commit(self, message: str, amend: bool = False, no_verify: bool = False) -> bool:
        """Create a git commit with the given message."""
        cmd = ['commit', '-m', message]
        if amend:
            cmd.append('--amend')
        if no_verify:
            cmd.append('--no-verify')

        try:
            output, code = self.run_git_command(cmd)
            if code == 0:
                self._print_success("\nCommit created successfully!")
                return True
            else:
                self._print_error(f"Failed to create commit: {output}")
                return False
        except subprocess.CalledProcessError as e:
            self._print_error(f"Failed to create commit: {e.stderr or e.stdout}")
            return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Git Commit Message Generator - Auto-generate conventional commit messages',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Interactive mode
  %(prog)s -q                 # Quick mode (non-interactive)
  %(prog)s -e                 # Include emoji in message
  %(prog)s -s                 # Only analyze staged files
  %(prog)s --dry-run          # Show message without committing
        """
    )

    parser.add_argument('-q', '--quick', action='store_true',
                        help='Quick mode: generate and commit without interaction')
    parser.add_argument('-e', '--emoji', action='store_true',
                        help='Include emoji in commit message')
    parser.add_argument('-s', '--staged', action='store_true',
                        help='Only analyze staged changes')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show generated message without committing')
    parser.add_argument('--amend', action='store_true',
                        help='Amend the last commit')
    parser.add_argument('--no-verify', action='store_true',
                        help='Skip pre-commit hooks')
    parser.add_argument('--no-color', action='store_true',
                        help='Disable colored output')
    parser.add_argument('-t', '--type', choices=[ct.name_str for ct in CommitType],
                        help='Override commit type')
    parser.add_argument('--scope', help='Override commit scope')
    parser.add_argument('-m', '--message', help='Override commit description')

    args = parser.parse_args()

    generator = GitCommitMessageGenerator(use_emoji=args.emoji, no_color=args.no_color)

    if not generator.is_git_repository():
        generator._print_error("Not a git repository. Please run this script in a git repository.")
        sys.exit(1)

    branch = generator.get_current_branch()
    print(f"{Color.BOLD}Branch:{Color.RESET} {Color.MAGENTA}{branch}{Color.RESET}")

    try:
        if args.quick:
            try:
                commit_message = generator.quick_mode(staged_only=args.staged)

                if args.type or args.scope or args.message:
                    suggestion = generator.suggest_commit_message(staged_only=args.staged)
                    if args.type:
                        suggestion.commit_type = args.type
                        suggestion.emoji = generator.get_commit_emoji(args.type)
                    if args.scope:
                        suggestion.scope = args.scope
                    if args.message:
                        suggestion.description = args.message
                    commit_message = suggestion.format(use_emoji=args.emoji)

                print(f"\n{Color.GREEN}{commit_message}{Color.RESET}")

                if args.dry_run:
                    print(f"\n{Color.YELLOW}(dry-run: commit not created){Color.RESET}")
                else:
                    generator.commit(commit_message, amend=args.amend, no_verify=args.no_verify)

            except ValueError as e:
                generator._print_error(str(e))
                sys.exit(1)
        else:
            commit_message = generator.interactive_mode(staged_only=args.staged)

            if commit_message:
                print(f"\n{'=' * 60}")
                print(f"{Color.BOLD}Final commit message:{Color.RESET}")
                print("=" * 60)
                print(f"{Color.GREEN}{commit_message}{Color.RESET}")
                print("=" * 60)

                if args.dry_run:
                    print(f"\n{Color.YELLOW}(dry-run: commit not created){Color.RESET}")
                    print("\nYou can manually use:")
                    escaped_message = commit_message.replace('"', '\\"')
                    print(f'git commit -m "{escaped_message}"')
                else:
                    try:
                        use_message = input(f"\n{Color.CYAN}Use this message for commit? (y/n):{Color.RESET} ").strip().lower()
                    except (KeyboardInterrupt, EOFError):
                        print("\nCancelled.")
                        sys.exit(0)

                    if use_message == 'y':
                        if generator.commit(commit_message, amend=args.amend, no_verify=args.no_verify):
                            sys.exit(0)
                        else:
                            sys.exit(1)
                    else:
                        print("\nCommit cancelled. You can manually use:")
                        escaped_message = commit_message.replace('"', '\\"')
                        print(f'git commit -m "{escaped_message}"')

    except KeyboardInterrupt:
        print("\n\nCancelled.")
        sys.exit(0)


if __name__ == "__main__":
    main()
