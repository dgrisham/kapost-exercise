#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

__author__ = "dgrisham"
__copyright__ = "dgrisham"
__license__ = "mit"


def main(args):
    cli(args)


def cli(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Kapost DevOps Technical Exercise")
    parser.add_argument(
        "-f", "--from", type=str, help="source S3 bucket", required=True
    )
    parser.add_argument(
        "-t", "--to", type=str, help="destination S3 bucket", required=True
    )
    parser.add_argument(
        "-s",
        "--size",
        type=int,
        help="threshold for size of files to copy (in MB)",
        required=True,
    )
    return parser.parse_args(args)


if __name__ == "__main__":
    main(sys.argv[1:])
