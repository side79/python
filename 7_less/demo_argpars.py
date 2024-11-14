import argparse
import os
import sys

def rgparse_ArgumentParser():
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

    if args.verbose:
        print("Gonna list this dir", args.path)

    if not os.path.isdir(args.path):
        if args.verbose:
            print("No such directory")
        sys.exit(1)
        
    print(args)

    print(os.listdir(args.path))

    
parser = argparse.ArgumentParser()
parser.version = "0.0.1.0"
parser.add_argument(
    "-V",
    "--version",
    action="version"
)

parser.add_argument(
    "--no-run",
    action="store_true"
)

args = parser.parse_args()
print(args)

if args.no_run:
    print("no run selected!")
    sys.exit()
    