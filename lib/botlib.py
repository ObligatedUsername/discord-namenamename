import wikipedia as wapi
import re

# workerbot-lib
#
#   building block of all that is 'full on processing' bot.
#

# features
def wikiSearch(lang="indonesia", seq="Test", *args):
    """Search for a specific subject on wikipedia and returns its title, summary, and link in a list.
    
    If your search query return multiple search results, this function will return a tuple of the error name and a list of top 5 search results."""
    if type(lang) is not str and type(seq) is not str: raise TypeError('language and search query must be a string.')

    for _, ls in enumerate(list(wapi.languages().items())):
        if lang in ls[1].lower():
            lang = ls[0]
            break
    try:
        wapi.set_lang(lang)
        page = wapi.page(seq)
    except wapi.exceptions.DisambiguationError as err:
        return ('error', err.args[1][:5]) 

    return [page.title, wapi.summary(seq).split('\n')[0][:1000]+'..', page.url]

def calculate(exp: str, *args):
    '''Calculates given expression and returns a float.'''
    exp = exp.replace(' ', '').replace('^', '**')
    pattexp = r'[^A-Za-z]'
    pattinv = r'[A-Za-z]'

    if exp == '': return None
    elif re.findall(pattinv, exp): raise TypeError('if you\'re looking to run a "test" code, maybe just don\'t, yeah?')

    return eval(''.join(re.findall(pattexp, exp)))

if __name__ == "__main__":
    print('this is a lib for a reason.')