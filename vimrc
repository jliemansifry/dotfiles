set ruler
set cursorline
call pathogen#infect()
syntax on

set tabstop=4
set expandtab  

set showcmd 
set lazyredraw          " redraw only when we need to.

set incsearch           " search as characters are entered
set hlsearch            " highlight matches

" turn off search highlight
nnoremap <leader><space> :nohlsearch<CR>
"

filetype plugin indent on

let mapleader=","       " leader is comma

syntax enable

" Solarized stuff
let g:solarized_termtrans = 1
set background=dark
colorscheme molokai

set backspace=indent,eol,start

" set number
" filetype indent plugin on

if has("autocmd")
  au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$")
    \| exe "normal! g'\"" | endif
endif

