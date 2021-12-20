" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')

    " File Explorer
    Plug 'scrooloose/NERDTree'

    " Nord Theme
    Plug 'shaunsingh/nord.nvim'

    " Pywal Theme
    Plug 'dylanaraps/wal.vim'

    " Plugin for git
    Plug 'tpope/vim-fugitive'
    Plug 'tpope/vim-rhubarb'

    " Autoclose parenthesis
    Plug 'cohama/lexima.vim'

    " fzf
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'junegunn/fzf.vim'

    " Statusline/tabline
    Plug 'itchyny/lightline.vim'

    " Change surrounding marks
    Plug 'tpope/vim-surround'

    " Distraction-free viewing
    Plug 'junegunn/goyo.vim'

    " Hyperfocus on a range
    Plug 'junegunn/limelight.vim'
    
    " Color previews for CSS
    Plug 'ap/vim-css-color'                            
    if has("nvim")
	    Plug 'neovim/nvim-lspconfig'
    endif

call plug#end()
