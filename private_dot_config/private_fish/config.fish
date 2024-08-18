
set user (whoami)
set host ($HOME/bin/host)
set distro (grep -E '^NAME=' /etc/os-release | cut -b 7-16)

function setup_conda;
   set ROOT $argv[1]
   set CONDA $argv[2]
   eval $ROOT/bin/conda "shell.fish" "hook" | source
   source $ROOT/etc/fish/conf.d/$CONDA.fish
   fish_add_path -gP $ROOT/bin
   # eval /home/sheffler/miniconda3/bin/conda "shell.fish" "hook" $argv | source
   # eval $HOME/sw/MambaForge/bin/mamba "shell.fish" "hook" $argv | source
   # eval /home/sheffler/sw/MambaForge/bin/conda "shell.fish" "hook" $argv | source
   # source /home/sheffler/sw/MambaForge/etc/fish/conf.d/mamba.fish
   conda config --set channel_priority flexible
   conda config --set auto_activate_base false
   if test -f "/home/sheffler/sw/MambaForge/etc/fish/conf.d/mamba.fish"
       source "/home/sheffler/sw/MambaForge/etc/fish/conf.d/mamba.fish"
   end
end

if [ $CONTAINER_ID ]
   eval (/home/linuxbrew/.linuxbrew/bin/brew shellenv)
   fish_add_path -gaP /home/linuxbrew/.linuxbrew/bin:$PATH
   if [ "$CONTAINER_ID" = "rfubuntu" ]
      setup_conda /opt/MambaForge mamba
      # set -gx LD_LIBRARY_PATH $HOME/miniconda3/envs/rfd/lib/python3.10/site-packages/nvidia/cuda_nvrtc/lib
   end
else if [ -e .singularity.d ]
   echo IN APPTAINER_CONTAINER
else
   set -gx QT_QPA_PLATFORM wayland
   atuin init fish | source
   direnv hook fish | source
   /usr/bin/starship init fish --print-full-init | source
   fzf --fish | source
   zoxide init fish | source
   fish_add_path -gaP $HOME/go/bin
   fish_add_path -gpP $HOME/.local/bin
   setup_conda ~/sw/MambaForge mamba
   # set -gx APPTAINER_CONTAINER '/software/containers/users/sheffler/rf_diffusion_aa_py310.sif'
   # set -gx OMP_NUM_THREADS 1
   # set -gx MKL_NUM_THREADS 1
   if set -q DISPLAY; and test $user != 'root';
      set -gx EDITOR 'sublime_text -'
      # fastfetch
   else;
      set -gx EDITOR ' emacs'
      setfont /home/sheffler/.local/share/consolefonts/Lat15-Terminus32x16.psf.gz
      # neofetch
   end
end


# conda activate rfd
# source $HOME/venv/sci/bin/activate.fish


# # set -gx __NV_PRIME_RENDER_OFFLOAD 1
# # set -gx __GLX_VENDOR_LIBRARY_NAME nvidia

# #set -gx LD_PRELOAD '/home/sheffler/tools/graphbolt/lib/mimalloc/out/release/libmimalloc.so'

# # set -gx PY /home/sheffler/venv/sci/bin/python
# # function fish_prompt; echo "-> "; end
# # function fish_prompt_right; echo ""; end




