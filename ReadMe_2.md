# Claude Code CLI Setup Guide

## Overview

Claude Code is a terminal-based AI coding assistant provided by Anthropic. It allows you to interact with Claude directly from your command line to generate code, debug issues, and scaffold applications.

---

## Prerequisites

* Node.js installed (v18 or later recommended)
* npm installed
* Internet connection
* Anthropic account

---

## 1. Install Claude Code

Install the official CLI globally using npm:

```bash
npm install -g @anthropic-ai/claude-code
```

### Fixing permission issues (macOS/Linux)

Avoid using sudo. Instead configure a local npm directory:

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
```

Then reinstall:

```bash
npm install -g @anthropic-ai/claude-code
```

---

## 2. Verify Installation

Check that Claude Code is installed correctly:

```bash
claude --version
```

Expected output:

```
Claude Code v2.x.x
```

---

## 3. Authenticate

Login to your Anthropic account:

```bash
claude login
```

This will:

* Open a browser window
* Prompt you to sign in
* Link your terminal to your Anthropic account

Note:
Claude Code uses account authentication, not just an API key.

---

## 4. Run Claude Code

Navigate to your project directory:

```bash
cd your-project
```

Start Claude:

```bash
claude
```

You will see an interactive terminal interface.

---

## 5. Basic Usage

Inside the Claude interface, type natural language prompts.

### Examples

Create an app:

```
create a flask app with html
```

Explain code:

```
explain this project structure
```

Fix bugs:

```
fix this failing test
```

Generate infrastructure:

```
create a terraform setup for ec2 with elastic ip
```

---

## 6. Troubleshooting

### Auto-update failed

If you see:

```
Auto-update failed
```

Run:

```bash
claude doctor
```

This will:

* Diagnose installation issues
* Fix configuration problems
* Suggest updates

---

### Command not found

Ensure your PATH includes npm global binaries:

```bash
export PATH=~/.npm-global/bin:$PATH
```

---

### Permission errors

Do not use sudo with npm. Use the npm global directory fix shown earlier.

---

## 7. Key Concepts

### Claude Code vs SDK

| Tool                      | Purpose                                    |
| ------------------------- | ------------------------------------------ |
| @anthropic-ai/claude-code | Terminal AI assistant                      |
| @anthropic-ai/sdk         | Programmatic API for building custom tools |

---

## 8. Use Cases

Claude Code is useful for:

* Generating application scaffolding
* Debugging test failures
* Writing Terraform and infrastructure code
* Explaining unfamiliar codebases
* Automating development workflows

---

## 9. Next Steps

To get more value:

* Use it inside real projects
* Combine it with your QA automation work
* Use it to debug CI/CD pipelines
* Generate infrastructure as code

---

## Summary

Claude Code provides a powerful way to bring AI directly into your terminal workflow. With proper setup and authentication, it can significantly speed up development, debugging, and DevOps tasks.
