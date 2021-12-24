source $HOME/.config/nvim/vim-plug/plugins.vim

set nocompatible        " Required to be iMproved

" Removes filetype
filetype plugin on
filetype plugin indent on

colorscheme wal         " Enabling Nord Theme Plugins

set laststatus=2        " Always show statusline

set noshowmode          " Prevents from showing insert on below powerline

set t_Co=256            " Set if term supports 256 colors.

set number relativenumber   " Display line numbers

syntax on               " Enable syntax

set clipboard+=unnamedplus  " Copy/paste between vim and other programs

:imap ii <Esc>          " Remap ESC to ii


set mouse=a             " Mouse Scrolling

" Text, tab and indent related
set expandtab                   " Use spaces instead of tabs.
set smarttab                    " Be smart using tabs ;)
set shiftwidth=4                " One tab == four spaces.
set tabstop=4                   " One tab == four spaces.

" LSP Mode: Pyright
lua << EOF
require'lspconfig'.pyright.setup{}
EOF

" vim-airline
let g:airline_theme='base16'

