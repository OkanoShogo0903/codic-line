# Codic Line (vim plug)
This is vim plugin.
This plugin use https://codic.jp/.

![demo](https://user-images.githubusercontent.com/25472671/58524198-6c4c5c80-8202-11e9-8b57-460eef7e49ac.gif)

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
