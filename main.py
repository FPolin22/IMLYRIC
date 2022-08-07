import argparse


def parse_arguments():
    """Parse the command arguments"""
    parser = argparse.ArgumentParser(
        description="Retrieve lyrics information for a given song",
        prog="IMLYRIC",
        epilog="Powered by Musixmatch and Spotify")
    parser.add_argument("--album", help="name of the album")
    parser.add_argument("--artist", help="name of the artist")
    parser.add_argument("--song", help="title of the song")
    parser.add_argument('--verbose', '-v', action='store_true', help="show additional logs")
    parser.add_argument("--version", action="version", version="IMLYRIC 1.0")
    return parser.parse_args()


def throw_console_errors(message):
    """Show arguments' errors"""
    return argparse.ArgumentParser().error(message)


if __name__ == "__main__":
    arguments = parse_arguments()  # parse the command-line arguments
    verbosity = arguments.verbose
    try:
       pass
    except Exception as err:
        throw_console_errors(str(err))
