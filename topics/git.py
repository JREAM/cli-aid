"""Git Helper."""


def submodule():
    """Submodule."""
    return {
        'flags': """
            -q for --quiet | Only print error messages
            -f for --force | only with add, deinit and update
        """,
        'commands': """
            > For new instantiations
            git submodule init
            git submodule add git@github.com/user/assets.git assets
            git submodule update

            > Updating a submodule
            cd assets
            git pull

            > Remove a Submodule
            git rm -rf assets
            git rm --cached doctrine
            .. Also remove the entire block from .git/submodules
            [submodule "assets"]

            > Misc
            git submodule status
        """
    }
