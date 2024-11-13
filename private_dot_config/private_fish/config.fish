set user (whoami)
set host ($HOME/.local/bin/host)
set distro (grep -E '^Na
   AME=' /etc/os-release | cut -b 7-16)
set -gx CONDA_EXE '/home/sheffler/sw/MambaForge/bin/conda'
set -gx MAMBA_EXE '/home/sheffler/sw/MambaForge/bin/mamba'

bind \b backward-kill-word 
bind \e\[3\;5~ kill-word

function setup_conda;
   set ROOT $argv[1]
   set CONDA $argv[2]
   eval $ROOT/bin/conda "shell.fish" "hook" | source
   source $ROOT/etc/fish/conf.d/$CONDA.fish
   fish_add_path -gP $ROOT/bin
   # conda config --set channel_priority flexible # these 2 are slow
   # conda config --set auto_activate_base false
   source "$ROOT/etc/fish/conf.d/mamba.fish"
end
if [ $CONTAINER_ID ]
   # echo IN CONTAINER
   eval (/home/linuxbrew/.linuxbrew/bin/brew shellenv)
   fish_add_path -gaP /home/linuxbrew/.linuxbrew/bin:$PATH
   if [ "$CONTAINER_ID" = "rfubuntu" ]
      setup_conda /opt/MambaForge mamba
      # set -gx LD_LIBRARY_PATH $HOME/miniconda3/envs/rfd/lib/python3.10/site-packages/nvidia/cuda_nvrtc/lib
   end
else if [ -e .singularity.d ]
   echo IN APPTAINER
# elseif [ $host == "lappy.root" ]
else
   # set -gx QT_QPA_PLATFORM wayland
   set -gx QT_QPA_PLATFORM xcb
   setup_conda ~/sw/MambaForge mamba
   atuin init fish | source
   atuin gen-completions --shell fish | source
   direnv hook fish | source
   fzf --fish | source
   zoxide init fish | source
   fish_add_path -gaP $HOME/go/bin
   fish_add_path -gpP $HOME/.local/bin
   source $HOME/.config/fish/conf.d/env.fish
   starship init fish --print-full-init | source
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
