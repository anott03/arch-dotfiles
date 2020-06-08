export ZSH="/home/amitav/.oh-my-zsh"

ZSH_THEME="amitav-agnoster"
plugins=(git zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh
export PATH="/home/amitav/.local/bin:$PATH"
export DENO_INSTALL="/home/amitav/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"
export EDITOR="nvim"
# vi mode
bindkey -v
export KEYTIMEOUT=1

# Use vim keys in tab complete menu:
bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'j' vi-down-line-or-history
bindkey -v '^?' backward-delete-char

# Change cursor shape for different vi modes.
function zle-keymap-select {
  if [[ ${KEYMAP} == vicmd ]] ||
     [[ $1 = 'block' ]]; then
    echo -ne '\e[1 q'
  elif [[ ${KEYMAP} == main ]] ||
       [[ ${KEYMAP} == viins ]] ||
       [[ ${KEYMAP} = '' ]] ||
       [[ $1 = 'beam' ]]; then
    echo -ne '\e[5 q'
  fi
}
zle -N zle-keymap-select
zle-line-init() {
    zle -K viins # initiate `vi insert` as keymap (can be removed if `bindkey -V` has been set elsewhere)
    echo -ne "\e[5 q"
}
zle -N zle-line-init
echo -ne '\e[5 q' # Use beam shape cursor on startup.
preexec() { echo -ne '\e[5 q' ;} # Use beam shape cursor for each new prompt.

# aliases 
alias push="git push origin master"
alias esl='npm i -D eslint eslint-config-airbnb-base eslint-plugin-import && touch .eslintrc.js && echo "module.exports = { extends: \"airbnb-base\" };" > .eslintrc.js'
alias init='npm init -y && esl'
alias vim='nvim'
alias vi='nvim'
alias vf='vifm'
alias ls='exa -al --group-directories-first'
alias rm='rm -i'
alias mutt='neomutt'
alias m='neomutt'
alias e='nvim ~/.zshrc'
alias l='. ~/.zshrc'
alias a='nvim ~/.config/alacritty/alacritty.yml'

transset-df 0.85 --id "$WINDOWID" >/dev/null

source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
