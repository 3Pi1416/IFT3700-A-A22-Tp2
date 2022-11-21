import wikipedia
import pandas as pd

dict_wiki = {"List of countries by GDP (nominal) per capita": [0]}

for wiki_title, args in dict_wiki.items():
    wiki_page = wikipedia.page(wiki_title).html().encode("UTF-8")
    data = pd.read_html(wiki_page)[args[0]]


