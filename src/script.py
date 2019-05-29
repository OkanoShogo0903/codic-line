# -*- coding: utf-8 -*-
def call_codic():
    import json
    import requests

    # Word
    word = vim.current.line

    # API Key
    headers = { 'Authorization': 'Bearer '+ vim.eval("g:codic_key") }

    url = 'https://api.codic.jp/v1/engine/translate.json?text={}&casing=lower+underscore'.format(word)

    r = requests.get(url, headers=headers)

    # Decode from json
    data = json.loads(r.text)    

    # Result
    # ref : https://vim-jp.org/vimdoc-ja/if_pyth.html
    print(data[0]['translated_text'])
    if data[0]['successful'] == True:
        # Save to @* register
        vim.command('let @* = \"{}\"'.format(data[0]['translated_text']+'\n'))
        """
        # Add translated text to under the cursor line
        vim.current.buffer.append(\
                [data[0]['translated_text']],
                vim.current.window.cursor[0]
        )
        """
