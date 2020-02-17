from math import pi
from argparse import ArgumentParser, RawDescriptionHelpFormatter

def circles(r):
    """renders the area of a circle with a given radius as input

    :param int r: radius
    """

    if r <0:
        raise ValueError("The radius should not be negative.")

    else:
        return pi * (r **2)


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, type=int, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)
