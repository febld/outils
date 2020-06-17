# VIM


## Vim : installation plugins pour dev

  * Installation plugin vim typescript "tsuquyomi" via plugin manager "pathogen"
    * Mise à niveau vim pour version graphique

        aptitude install vim-gui-common vim-runtime

    * Pathogen :

        mkdir -p ~/.vim/autoload ~/.vim/bundle
        curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim

    * tsuquyomi

        npm -g install typescript
        mkdir -p ~/.vim/bundle #### create bundle folder if it doesn't exist
        git clone https://github.com/Quramy/tsuquyomi.git ~/.vim/bundle/tsuquyomi ### Install tsuquyomi

  * Installation plugin vim "tsuquyomi" selon standard VIM

        mkdir -p ~/.vim/pack/vendor/start
        git clone https://github.com/Quramy/tsuquyomi.git ~/.vim/pack/typescript/start/tsuquyomi

  * Installation plugin vim "typescript-vim" (syntaxe) :

        git clone https://github.com/leafgarland/typescript-vim.git ~/.vim/pack/typescript/start/typescript-vim

  * Plugin VIM : NERDTree

        mkdir -p ~/.vim/pack/vendor/start
        git clone https://github.com/preservim/nerdtree.git ~/.vim/pack/files/start/nerdtree

