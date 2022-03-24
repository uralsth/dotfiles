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
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'

    " Change surrounding marks
    Plug 'tpope/vim-surround'

    Plug 'inkarkat/vim-ReplaceWithRegister'

    " Distraction-free viewing
    Plug 'junegunn/goyo.vim'

    " Hyperfocus on a range
    Plug 'junegunn/limelight.vim'


    " CocInstall for installing Coc-Pyright
    Plug 'neoclide/coc.nvim', {'branch': 'release'}

    " Color previews for CSS
    Plug 'ap/vim-css-color'                            
    if has("nvim")
	    Plug 'neovim/nvim-lspconfig'
    endif

call plug#end()
