
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
alias cz chezmoi
alias emacs 'emacs -nw'
alias db distrobox
alias dbe 'distrobox enter'
alias dbarch 'distrobox enter arch'
alias t tree
alias ff fastfetch
alias top htop
alias bat 'bat --color=always --paging=always'
alias unalias 'functions --erase'

alias ghc 'gh copilot'
alias ghcs 'gh copilot -t shell'
alias ghcg 'gh copilot -t git'
alias ghcgh 'gh copilot -t gh'

alias auri 'pikaur -S'
alias auru 'pikaur -Syu'
alias aurr 'pikaur -R'
alias reloadfish "source $HOME/.config/fish/config.fish"

alias sk "sk --preview 'bat --color=always {}'"
alias isub "subl (sk --preview 'bat --color=always {}')"
alias ipac "pacman -Slq | sk --multi --preview 'pacman -Si {1}' | xargs -ro sudo pacman -S"
alias ipacrm "pacman -Qq | sk --multi --preview 'pacman -Qi {1}' | xargs -ro sudo pacman -Rns"

