#SOLVED Woah, that was a nice piece, but mainly I designed my own version of vim :-)
def between_markers(text: str, begin: str, end: str) -> str:
    
    if begin not in text and end not in text:
        return text
    if begin not in text:
        nde = text.index(end)
        return text[:nde]
    if end not in text:
        anf = len(begin) + text.index(begin)
        return text[anf:]
    anf  = int(len(begin) + text.index(begin))
    nde = text.index(end)
    return text[anf:nde]

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What[b]ui is[/b] apple', '[b]','[/b]'))

    # "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
