set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" SuperTab plugin
Plugin 'ervandew/supertab'

" altercation/vim-colors-solarized plugin
Plugin 'altercation/vim-colors-solarized'

" bling/vim-airline plugin
Plugin 'bling/vim-airline'

" majutsushi/tagbar plugin
Plugin 'majutsushi/tagbar'

" kien/ctrlp.vim plugin
Plugin 'kien/ctrlp.vim'

" ntpeters/vim-better-whitespace plugin
Plugin 'ntpeters/vim-better-whitespace'

" joonty/vim-phpqa plugin
Plugin 'joonty/vim-phpqa'

" jiangmiao/auto-pairs
Plugin 'jiangmiao/auto-pairs'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

" altercation/vim-colors-solarized setting
syntax enable
set background=light
let g:solarized_termcolors=256
let g:solarized_visibility="normal"
colorscheme solarized

"Tab sizes - use 2 spaces for tab spacing
set softtabstop=4   " when in insert mode <tab> is pressed move 4 columns
set tabstop=4       " a tab found in a file will be represented with 4 columns
set shiftwidth=4    " indentation is 4 columns
set expandtab       " save as spaces rather than tabs
set backspace=indent,eol,start  " remove 4 spaces of tab by pressing backspace

" tagbar setting
" tagbar Open by pressing F8
nnoremap <silent> <F8> :TagbarToggle<CR>

" ntpeters/vim-better-whitespace Setting
let strip_whitespace_on_save = 1

" joonty/vim-phpqa Setting
" disable php codesniffer
" disable php messdetector
let g:phpqa_codesniffer_autorun = 0
let g:phpqa_messdetector_autorun = 0

" airline setting
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#tab_nr_type = 1
let g:airline#extensions#whitespace#enabled = 0

" jiangmiao/auto-pairs Setting
let g:AutoPairsFlyMode = 1

" Set number
set colorcolumn=80,120
set linespace=2
set ruler
set number
set incsearch
set hlsearch

" fileformat stuff
" "set fileformat=unix
set fileformats=unix,dos
set encoding=utf-8
" "set fileencoding=utf-8
set fileencodings=utf-8,ucs-bom,cp1250,iso-8859-1
