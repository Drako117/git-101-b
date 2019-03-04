SUFFIXES = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

def approximate_size(size):
    """Convert a file size to human-readable form.""" 
    multiple = 1024
    if size < 0:
        raise ValueError('number must be non-negative')
    for suffix in SUFFIXES:
        size /= SUFFIXES[multiple]
        if size < multiple:
            return f'{size} {suffix}'
    raise ValueError('number too large')
