" ------------------------------------------------------------------------------
" Syntax option, color ...
syntax on
:set nu
filetype plugin indent on
highlight Pmenu ctermfg=white ctermbg=lightblue
highlight PmenuSel ctermfg=white ctermbg=lightred

" ------------------------------------------------------------------------------
"  auto complete options
set completeopt=longest,menuone

" ------------------------------------------------------------------------------
" various map, <Leader>  definition
let mapleader = ","
imap <Leader><Tab> <C-x><C-o>

" ------------------------------------------------------------------------------
" Plugin typescript-vim
let g:typescript_indent_disable = 1

" ------------------------------------------------------------------------------
" VIM Indentation
:set expandtab
":set tabstop=4
:set shiftwidth=4
:set softtabstop=4

" ------------------------------------------------------------------------------
" Plugin NEERDTree
map <C-n> :NERDTreeToggle<CR>

" ------------------------------------------------------------------------------
" Plugin : TagBar
map <C-b> :TagbarToggle<CR>

" ------------------------------------------------------------------------------
" Plugin : JavaComplete2
" Plugin 'artur-shaik/vim-javacomplete2'
autocmd FileType java setlocal omnifunc=javacomplete#Complete
autocmd FileType java JCEnable
nmap <F4> <Plug>(JavaComplete-Imports-AddSmart)
imap <F4> <Plug>(JavaComplete-Imports-AddSmart)
nmap <F5> <Plug>(JavaComplete-Imports-Add)
imap <F5> <Plug>(JavaComplete-Imports-Add)
nmap <F6> <Plug>(JavaComplete-Imports-AddMissing)
imap <F6> <Plug>(JavaComplete-Imports-AddMissing)
nmap <F7> <Plug>(JavaComplete-Imports-RemoveUnused)
imap <F7> <Plug>(JavaComplete-Imports-RemoveUnused)
