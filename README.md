# CLI Snippet Tool
This is a Python 2.6/2.7 package to be used in your command line to easily assist you with your favorite snippets.

_[Soon to be Python3 compatible as well.]_

> **STATUS**: In Development [PIP Packaging](https://packaging.python.org/distributing/)

<!-- TOC -->

- [CLI Snippet Tool](#cli-snippet-tool)
    - [Save Development Time](#save-development-time)
    - [Definitions](#definitions)
    - [Custom Topics](#custom-topics)
    - [Rules to Topics](#rules-to-topics)
    - [Writing your Topic](#writing-your-topic)
    - [Road Map & Contributing](#road-map--contributing)

<!-- /TOC -->

## Save Development Time

Although there are Linux `man`(ual) pages and many `--help` flags, even the most seasoned developers forget many commands and at times simply cannot recall.

Most of us turn to Google, yet it's sometimes tedious to find our solution more than once.

The greatest benefit is that you can build your own snippet library easily within your terminal and access it from your terminal on any Linux OS!

> **Fork**: Feel free to fork and customize to your liking. I highly recommend you keep it in your own git repository to transfer it from different computers and servers.


## Definitions

- **TOPICS**: Where methods define help instructions
    - **SERVICE**: The first command you want information about (eg: git, find, etc)
    - **COMMAND**: The second command to look up with a service, for example:
        - `./cli_aid.py <service> <command>`
        - `./cli_aid.py git submodule`
- **MODULE**: There is only one module: `topics`, which stores all of your items.


## Custom Topics

Adding a topic is very easy. You should look at `topics/demo.py` for an example. To se the output in action, try these three commands:

```sh
./cli_aid.py demo basic        ; A text output
./cli_aid.py demo standard     ; A dictionary output
./cli_aid.py demo wrong        ; An error output
```


## Rules to Topics

- The topic/**filename** will be the first argument
- The topic/**filename** methods can be used as a second argument
- Topics must always return something, valid options:
    - String
    - Dictionary in the format of: `{'flags': '..', 'commands': '...'}`


## Writing your Topic

If I wanted to create an example topic I would first figure out the commands I want to remember. So for mysql I may want to be able to type:

```sh
./cli_aid.py mysql connect
./cli_aid.py mysql tricks
```

To accomplish this is very easy:

```sh
touch topics/mysql.py
```

Edit the new file let's define our second arguments, I'll provide the basic (string) and standard (dictionary) output examples.

> **Remember**: You can put any output in these you want, it's for you to help yourself.

```py
def connect():
    """This is a standard dictionary return."""
    return {
        'flags': """
            -u  --user
            -p  --password[=name]
            -P  --port=#
            -v  --verbose
        """,
        'commands': """
            mysql -u root -p
            mysql -u root -p -h localhost
        """
    }

def tricks():
    """This is a basic string return."""
    return """
    user@localhost limits to the same server
    user@% allows remote connections
    """
```

That's it, now you should be able to run it, try it out!

```sh
./cli_aid.py mysql connect
./cli_aid.py mysql tricks
```


## Road Map & Contributing

If you have the desire to contribute the goal to keep in mind is this:

- The code should be extremely simple.
- There should be no third-party addons for the users benefit.
- Would like to do/Plans:
    - Unit Testing
    - Should user have ability to easily create new topics/details? For example:
        - `./cli_aid.py save java install "This is how to install java, etc."` (save would create/update)
        - `./cli_aid.py save nginx config "flags: -y auto yes"`
        - `./cli_aid.py save nginx config "commands: Anything here like a textfield"`
        - The above seems hard to format in one line unless it's basic text. However, using the save method could keep adding to the same file, but removing items would be problematic with string searching to the exact wording they wrote in the past.
        - I think if the user is using CLI they are good enough to simply `vim topics/their-file.py`.
    - More/Better Error Proofing
    - Possibly a better syntax or format for the topic files
    - Python 3 compatible
    - One argument produces a list of method names within the topic (module).
    - A nice shortname rather than `cli_aid`
        - Some name ideas:
            - `snippette` (too long)
            - `snipr` (too much typing, sounds like sniper)
            - `scrap` (sounds like garbage, or close to scraper)
            - `hlp` (I kind of like, easy to type and remember, something to do with 'help' seems best)
            - `assist` (seems nice, like when typing `assist mysql connect` )
            - `aid` (I really like this, `aid php config`, may be under the [id-utils](https://www.gnu.org/software/idutils/manual/idutils.html) package though  has this alias which runs `lid -ils` )
                - maybe even `cli_aid`, `cli_aid find list`
            - `ayd` (sounds like aid, not as easy to type)
            - `hh` (short to type, might fight with an alias, also doesn't explain much)
    - Complete the Install Script, so it can be run from a nice name, eg: `$ hlp js snippets` with out disrupting any other system commands or common words.
- Any ideas are also welcomed, just create a Git Issue!



---
License: MIT

&copy;2017 Jesse Boyer &mdash; [JREAM](http://jream.com)
