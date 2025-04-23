set user (whoami)
set host ($HOME/.local/bin/host)
set distro (grep -E '^Na
   AME=' /etc/os-release | cut -b 7-16)

bind \b backward-kill-word 
bind \e\[3\;5~ kill-word

if [ -e .singularity.d ]
   echo IN APPTAINER
# elseif [ $host == "lappy.root" ]
else
   set -gx QT_QPA_PLATFORM wayland
   # set -gx QT_QPA_PLATFORM xcb
   atuin init fish | source
   atuin gen-completions --shell fish | source
   direnv hook fish | source
   fzf --fish | source
   zoxide init fish | source
   fish_add_path -gaP $HOME/go/bin
   fish_add_path -gpP $HOME/.local/bin
   source $HOME/.config/fish/conf.d/env.fish
   # starship init fish --print-full-init | source
   # set -gx APPTAINER_CONTAINER '/software/containers/users/sheffler/rf_diffusion_aa_py310.sif'
   set -gx OMP_NUM_THREADS 4
   set -gx MKL_NUM_THREADS 4
   if set -q DISPLAY; and test $user != 'root';
      set -gx EDITOR 'subl -w'
      # fastfetch
   else if test -e /mnt/home/sheffler
      # echo "DIGS"
      set -gx EDITOR ' emacs'
   else;
      # echo "Vconsole"
      set -gx EDITOR ' emacs'
#      setfont /home/sheffler/.local/share/consolefonts/Lat15-Terminus32x16.psf.gz
      # neofetch
   end
end

bass source ~/.secrets


fish_add_path /home/sheffler/.modular/bin

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /home/sheffler/miniforge3/bin/conda
    eval /home/sheffler/miniforge3/bin/conda "shell.fish" "hook" $argv | source
else
    if test -f "/home/sheffler/miniforge3/etc/fish/conf.d/conda.fish"
        . "/home/sheffler/miniforge3/etc/fish/conf.d/conda.fish"
    else
        set -x PATH "/home/sheffler/miniforge3/bin" $PATH
    end
end
# <<< conda initialize <<<

