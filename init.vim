" source config files
source $HOME/.config/nvim/plugin_configs/coc_config.vim
source $HOME/.config/nvim/plugin_configs/sneak_config.vim

" be quiet
set noerrorbells
" better indentation
set smartindent
" line numbers
set number
set relativenumber
" enable mouse support
set mouse=a
" make tabsize 2 spaces
set shiftwidth=2
set tabstop=2
" split settigns
set splitbelow
set splitright
" where to store undofiles
set undodir=~/.config/nvim/undodir
set undofile

" Vim-Plug package manager
call plug#begin(stdpath('data') . '/plugged')
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'sheerun/vim-polyglot'
Plug 'pangloss/vim-javascript'
Plug 'preservim/nerdtree'
Plug 'justinmk/vim-sneak'
Plug 'gruvbox-community/gruvbox'
Plug 'vim-airline/vim-airline'
call plug#end()

" dark gruvbox (the only good gruvbox)
colorscheme gruvbox
set background=dark

" make :tree and alias to :NERDTree
cnoreabbrev <expr> tree ((getcmdtype() is# ':' && getcmdline() is# 'tree')?('NERDTree'):('tree'))
" set the leader key to be space
let mapleader = " "
" map leader + hjkl to navigate panes
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>

" has uses a different register so that dd, dw, etc. won't override my last yank
noremap p "0p
noremap P "0P
noremap x "0x
" so that  when I define a register to use the above remappings don't apply
for s:i in ['"','*','+','-','.',':','%','/','=','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    execute 'noremap "'.s:i.'p "'.s:i.'p'
    execute 'noremap "'.s:i.'P "'.s:i.'P'
endfor
" yanked items will be in system clipboard
set clipboard=unnamed
