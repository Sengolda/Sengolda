import urllib.request
import json
import random


TO_APPEND = """
### Quotes
- A random programming quote from the [hourly quote generator](auto_update.py) 
- Quote for the hour is:

```
{quote}
  - {author}
```
"""

def get_random_quote():
    resp = urllib.request.urlopen("https://raw.githubusercontent.com/skolakoda/programming-quotes-api/master/Data/quotes.json")
    actual_resp = json.loads(resp.read())
    quote_info = random.choice(actual_resp)
    return quote_info["author"], quote_info["en"]

with open("README.md", "w") as actual_readme:
    with open("without_quote_readme.txt", "r") as no_quote_readme:
        author, quote = get_random_quote()
        readme_with_new_quote = no_quote_readme.read() + "\n\n" + TO_APPEND.format(quote=quote, author=author)
        actual_readme.write(readme_with_new_quote)
