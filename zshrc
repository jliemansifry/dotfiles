# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# hist
HISTSIZE=50000

# Path to your oh-my-zsh installation.
export ZSH=~/.oh-my-zsh

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="dgolden1"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to disable auto-setting terminal title.
DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
HIST_STAMPS="mm/dd/yyyy"

# plugins
plugins=(git git-prompt)

# deal with autosuggestions and syntax highlighting not playing nice on zshrc reload
if [[ $ZSH_EVAL_CONTEXT == 'file' ]]; then
  plugins=(zsh-autosuggestions zsh-syntax-highlighting)
fi

source $ZSH/oh-my-zsh.sh

# PATHs
export PATH=~/anaconda3/bin:/usr/local/bin:$PATH

# autojump
if [ "$(uname)" = "Darwin" ]; then
  # Autojump https://github.com/joelthelion/autojump
  [[ -s $(brew --prefix)/etc/profile.d/autojump.sh ]] && . $(brew --prefix)/etc/profile.d/autojump.sh

  test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"
else
  # Autojump
  if [ -f /usr/share/autojump/autojump.sh ]; then
    . /usr/share/autojump/autojump.sh
  fi
fi

# Git prompt
# PROMPT='%B%~%b$(git_super_status) %# '

# Keys
# CTRL+U kills left of line, not entire line
bindkey \^U backward-kill-line

# Aliases
alias jnb='jupyter notebook'
alias jnbb='jupyter notebook --no-browser'
alias tma='tmux attach || tmux'
# SSH into EC2 instance
alias sse='ssh -i ~/.ssh/gcp-key.pem'

# tmux aliases
alias ta='tmux attach -t'
alias tn='tmux new -s'
alias tls='tmux ls'

# git
alias gs='git status'
alias gd='git diff'
alias ga='git add .'

# helpful randoms
alias gps='ps aux | grep'
alias ddport='ssh -N -f -L localhost:8901:localhost:8905 dd'
alias dtport='ssh -N -f -L localhost:8900:localhost:8904 dt'

# The next line updates PATH for the Google Cloud SDK.
if [ -f ~/google-cloud-sdk/path.zsh.inc ]; then
  source ~/google-cloud-sdk/path.zsh.inc
fi

# The next line enables shell command completion for gcloud.
if [ -f ~/google-cloud-sdk/completion.zsh.inc ]; then
  source ~/google-cloud-sdk/completion.zsh.inc
fi

# Local config
[[ -f ~/.zshrc.local ]] && source ~/.zshrc.local
