#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\W] \$ '

# PS1='[\u@\h \W]\$ '
alias luamake=/home/ural/Cloned/lua-language-server/3rd/luamake/luamake
PATH=$PATH:$HOME/.local/bin
