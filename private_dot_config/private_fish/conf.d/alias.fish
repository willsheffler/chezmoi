
# alias du dust
# alias top 'btop'
alias top 'top -d 1'
# alias cat bat
alias btrfs 'sudo btrfs'
alias mount 'sudo mount'
alias umount 'sudo umount'
alias fdisk 'sudo fdisk'
alias gparted 'sudo gparted'
alias fdisk 'sudo gparted'

# alias find fd
# alias df duf
alias ls 'eza'
alias ll 'eza -l'
alias lla 'eza -la'
# alias cd 'z'
alias emacs 'emacs -nw'
alias db distrobox
alias dbe 'distrobox enter'
alias dbarch 'distrobox enter arch'
alias t tre
alias ff fastfetch
alias top htop
alias bat 'bat --color=always --paging=always'
alias unalias 'functions --erase'
alias rg 'rg --no-ignore'
alias eg 'gprp  -E'

alias doit 'doit --seek-file'

alias ghc 'gh copilot'
alias ghcs 'gh copilot suggest'

alias auri 'pikaur -S'
alias auru 'pikaur -Syu'
alias aurr 'pikaur -R'
alias reloadfish "source $HOME/.config/fish/config.fish"

alias sk "sk --preview 'bat --color=always {}'"
alias isub "subl (sk --preview 'bat --color=always {}')"
alias ipac "pacman -Slq | sk --multi --preview 'pacman -Si {1}' | xargs -ro sudo pacman -S"
alias ipacrm "pacman -Qq | sk --multi --preview 'pacman -Qi {1}' | xargs -ro sudo pacman -Rns"

alias ruff_issue_count "ruff check --output-format=json| jq 'group_by(.code) | map({code: .[0].code, count: length})'"

alias rfdsym 'mamba activate rfdsym312 && cd ~/rfdsym'
alias rfdsymrf 'mamba activate rfdsym312 && cd ~/rfdsym/lib/rf2aa'
alias rfdsymipd 'mamba activate rfdsym312 && cd ~/rfdsym/lib/rf2aa/lib/ipd'

alias gs 'git status'
alias gc 'git commit -a'
alias gb 'git branch -a'
# alias gp 'git remote prune origin'
# alias grb 'git branch -d'
alias gl 'git log --graph --oneline --decorate'
alias gla 'git log --graph --oneline --decorate --all'
alias gd 'git diff'
alias gdo 'git diff --nameonly'
alias gf 'git fetch --all'

alias code 'code --enable-features=UseOzonePlatform,WaylandWindowDecorations --ozone-platform-hint=auto'
alias ldmrestart 'sudo systemctl restart lightdm'
alias ctl 'sudo systemctl'
alias cm 'chezmoi'
