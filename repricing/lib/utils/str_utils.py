def contains_any(string, matches):
    """
    Determine if a string contains any of the given values. *matches* may be a
    single string, or a list of strings.
    """
    return any([m in string for m in ([matches] if isinstance(matches, str) else matches)])


def contains_any_ignorecase(string, matches):
    """
    Determine if a string contains any of the given values. *matches* may be a
    single string, or a list of strings.
    """
    return any([m.lower() in string.lower() for m in ([matches] if isinstance(matches, str) else matches)])


def contains_all(string, matches):
    """
    Determine if a string contains all of the given values.
    """
    return all([m in string for m in matches])


def contains_all_ignorecase(string, matches):
    """
    Determine if a string contains all of the given values.
    """
    return all([m.lower() in string.lower() for m in matches])
