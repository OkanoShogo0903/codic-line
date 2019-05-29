scriptencoding utf-8
if exists("g:loaded_codic_line")
  finish
endif
let g:loaded_codic_line = 1

let s:save_cpo = &cpo
set cpo&vim

command! CodicLine call codic#call()
command! CodeHelp call codic#call()
"nmap z :call hello#helloworld()<CR>

let &cpo = s:save_cpo
unlet s:save_cpo
