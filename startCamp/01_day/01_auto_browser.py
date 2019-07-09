"""
webbrowser.open(url)
webbrowser.open_new(url)
webbrowser.open_new_tab(url)
"""
import webbrowser

query = ['bts', '아이유']

for i in query:
    search_url = (f'http://google.com/search?q={i}')
    webbrowser.open(search_url)