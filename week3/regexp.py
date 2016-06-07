def search(pattern, text):
    """Return true if pattern appears anywhere in text."""
    if pattern.startswith('^'):
        return match(pattern, text) # fill this line
    else:
        return match('.*' + pattern, text) # fill this line