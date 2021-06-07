umask 22
if ( $?prompt ) then
        set history=32
endif
set filec
set ignoreeof
set prompt="`hostname`:$cwd:t \! # "

alias   a               alias
a	setprompt	'set prompt="`hostname`:$cwd:t \! # "'
a       rm              'rm -i \!*'
a       mv              'mv -i \!*'
a       cp              'cp -i \!*'
a	cd		'cd \!* && setprompt'
a       ls              'ls -asCF \!*'
a       h               history
a       dir             'ls -agCFl \!*'
setprompt
