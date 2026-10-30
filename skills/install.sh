#!/usr/bin/env sh
# Install a Preppr skill into the skills directory of one or more AI tools.
#
#   sh install.sh <tool> [--project] [skill-name]
#
#   <tool>      claude | copilot | gemini | codex | all
#   --project   install into the current project (default: your user profile)
#   skill-name  defaults to preparedness-alert-warning-templates
#
# All of these tools read the same Agent Skills format (a folder with SKILL.md),
# so the installer only copies the folder to where each tool looks for it:
#
#   tool     user-level                 project-level
#   claude   ~/.claude/skills/          ./.claude/skills/
#   copilot  ~/.copilot/skills/         ./.github/skills/
#   gemini   ~/.gemini/skills/          ./.gemini/skills/
#   codex    ~/.agents/skills/          ./.agents/skills/
#
# Copilot, Gemini CLI and Codex also all read ./.agents/skills, so for a shared
# project folder "codex --project" covers those three at once.
set -eu

HERE=$(cd "$(dirname "$0")" && pwd)
TOOL=${1:-}
SCOPE=user
NAME=preparedness-alert-warning-templates
shift || true
for arg in "$@"; do
  case "$arg" in
    --project) SCOPE=project ;;
    *) NAME=$arg ;;
  esac
done

SRC="$HERE/$NAME"
if [ -z "$TOOL" ] || [ ! -f "$SRC/SKILL.md" ]; then
  sed -n '2,20p' "$0"
  exit 1
fi

dest_for() {
  case "$1:$SCOPE" in
    claude:user)    echo "$HOME/.claude/skills" ;;
    claude:project) echo "./.claude/skills" ;;
    copilot:user)   echo "$HOME/.copilot/skills" ;;
    copilot:project) echo "./.github/skills" ;;
    gemini:user)    echo "$HOME/.gemini/skills" ;;
    gemini:project) echo "./.gemini/skills" ;;
    codex:user)     echo "$HOME/.agents/skills" ;;
    codex:project)  echo "./.agents/skills" ;;
    *) echo "Unknown tool: $1 (use claude, copilot, gemini, codex or all)" >&2; exit 1 ;;
  esac
}

install_one() {
  dest=$(dest_for "$1")
  mkdir -p "$dest"
  rm -rf "$dest/$NAME"
  cp -R "$SRC" "$dest/$NAME"
  echo "Installed $NAME for $1 at $dest/$NAME"
}

if [ "$TOOL" = all ]; then
  for t in claude copilot gemini codex; do install_one "$t"; done
else
  install_one "$TOOL"
fi
