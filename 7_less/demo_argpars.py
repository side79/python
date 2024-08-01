import argparse
import os

parser = argparse.ArgumentParser(
    prog="My argpars demo",
    description="Show argparse",
)

parser.add_argument(
    "path",
    metavar="path",
    type=str,
    help="the path to be listed"
)

parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="verbose show more info"
)

args = parser.parse_args()


print(args)

print("List of", os.listdir(args.path))