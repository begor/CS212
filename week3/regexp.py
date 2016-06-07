def search(pattern, text):
    """Return true if pattern appears anywhere in text."""
    if pattern.startswith('^'):
        return match(pattern[1:], text) # fill this line
    else:
        return match('.*' + pattern, text) # fill this line


def match(pattern, text):
    """
    Return True if pattern appears at the start of text."""

    if pattern == '':
        return True
    elif pattern == '$':
        return text is ''
    elif len(pattern) > 1 and pattern[1] in '*?':
    	return True
    else:
        return True