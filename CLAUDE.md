# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**PlaneSpottr** - A new project repository that is currently at its initial commit.

## Current State

- The repository has been initialized with a basic structure
- Ready for development and code implementation
- Follow semantic versioning for version numbers

## Repository Structure

The project is in its early stages. As code is added:
- Review file organization patterns established
- Follow existing code style and conventions
- Respect the project's architecture decisions

## Development Commands

### Setting Up the Project

```bash
# Install dependencies
npm install

# Or if using other package managers, install as appropriate
```

### Code Quality

```bash
# Run linter
npm run lint

# Run formatter
npm run format
```

### Testing

```bash
# Run all tests
npm test

# Run a specific test file
npm test path/to/test/file.test.ts

# Run tests with coverage
npm run test:coverage

# Run a specific test with verbose output
npm test -- --verbose path/to/test/file
```

### Build

```bash
# Build the project
npm run build
```

### Common Tasks

```bash
# Start development server
npm run dev

# Type checking
npm run check

# Clean build artifacts
npm run clean
```

## Adding Features

When adding new functionality:
1. Review existing code patterns and architecture
2. Ensure tests are written for new features
3. Update documentation as needed
4. Follow existing code style and naming conventions

## Notes for Future Development

- The project uses standard web development tooling (npm, linting, testing)
- Follow existing architecture patterns when implementing features
- Write clear, meaningful commit messages
- Keep dependencies minimal and well-documented
