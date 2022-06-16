source $HOME/.config/nvim/vim-plug/plugins.vim
let mapleader = "C" "
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

:imap <C-g> <Esc>

set timeoutlen=200

set mouse=a             " Mouse Scrolling

" Text, tab and indent related
set expandtab                   " Use spaces instead of tabs.
set smarttab                    " Be smart using tabs ;)
set shiftwidth=4                " One tab == four spaces.
set tabstop=4                   " One tab == four spaces.


" Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
let g:UltiSnipsExpandTrigger="<C-J>"
let g:UltiSnipsJumpForwardTrigger="<c-j>"
let g:UltiSnipsJumpBackwardTrigger="<c-k>"

" disable header folding
let g:vim_markdown_folding_disabled = 1

" do not use conceal feature, the implementation is not so good
let g:vim_markdown_conceal = 0

" disable math tex conceal feature
let g:tex_conceal = ""
let g:vim_markdown_math = 1

" support front matter of various format
let g:vim_markdown_frontmatter = 1  " for YAML format
let g:vim_markdown_toml_frontmatter = 1  " for TOML format
let g:vim_markdown_json_frontmatter = 1  " for JSON format

augroup pandoc_syntax
    au! BufNewFile,BufFilePre,BufRead *.md set filetype=markdown.pandoc
augroup END

" do not close the preview tab when switching to other buffers
let g:mkdp_auto_close = 0

nnoremap <M-m> :MarkdownPreview<CR>

source $HOME/.config/nvim/themes/airline.vim
