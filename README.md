# Codic Line (vim plug)
This is vim plugin.
This plugin use https://codic.jp/.

## How to use
Please command `:CodicLine` at target line.
This plugin translate all string in the line.

Result registed to `@*` on success.

## Install
```
[[plugins]]
repo = 'OkanoShogo0903/codic-line'
hook_add = '''
let g:codic_key = "************************"
'''
```

## License
MIT
