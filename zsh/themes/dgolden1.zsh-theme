# This is like the robbyrussell theme, but without the built-in
# git prompt. There are some vestiges of my attempts and failures to use
# the official git prompt
#
# Install this in ~/.oh-my-zsh/themes/

# Git prompt
# https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh
# source ~/.git-prompt.sh

local ret_status="%(?:%{$fg_bold[green]%}➜ :%{$fg_bold[red]%}➜ )"
# PROMPT='${ret_status} %{$fg[cyan]%}%c%{$reset_color%} $(__git_ps1 " (%s)") '
PROMPT='${ret_status} %{$reset_color%}[%m] %{$fg[cyan]%}%c%{$reset_color%} $ '
# precmd () { __git_ps1 "%n" ":%~$ " "|%s" }

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg_bold[blue]%}git:(%{$fg[red]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%} "
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[blue]%}) %{$fg[yellow]%}✗"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[blue]%})"
