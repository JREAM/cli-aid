"""Demo Helper."""


def basic():
    """Basic output string."""
    return """
    We can return a single string, use three quotes \"\"\"
    For a multiline output!
    """

def standard():
    """Standard output dictionary."""
    return {
        'flags': """
            -x Fake flag example
            -d Another flag example
        """,
        'commands': """
            This a dictionary output which has "flags" and "commands".
            It still outputs a multiline item but it's separated more.
        """
    }

def wrong():
    """Wrong way, does not return string or dictionary."""
    return None
