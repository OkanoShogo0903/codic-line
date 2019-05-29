scriptencoding utf-8

let s:save_cpo = &cpo
set cpo&vim

pyfile <sfile>:h:h/src/script.py
python import vim

function! codic#call()
  python call_codic()
endfunction

let &cpo = s:save_cpo
unlet s:save_cpo
