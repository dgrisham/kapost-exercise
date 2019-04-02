#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

import boto3
from botocore.exceptions import ClientError

__author__ = "dgrisham"
__copyright__ = "dgrisham"
__license__ = "mit"


def main(argv):
    args = cli(argv)
    src = args.src
    dst = args.dst

    s3 = boto3.resource("s3")

    try:
        s3.meta.client.head_bucket(Bucket=src)
    except ClientError as e:
        print(f"error loading bucket '{src}': {e}", sys.stderr)
        exit(1)
    try:
        s3.meta.client.head_bucket(Bucket=dst)
    except ClientError as e:
        print(f"error loading bucket '{dst}': {e}", sys.stderr)
        exit(1)

    bsrc = s3.Bucket(src)
    bdst = s3.Bucket(dst)

    return s3, bsrc, bdst


def cli(argv):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Kapost DevOps Technical Exercise")
    parser.add_argument(
        "-f", "--from", dest="src", type=str, help="source S3 bucket", required=True
    )
    parser.add_argument(
        "-t", "--to", dest="dst", type=str, help="destination S3 bucket", required=True
    )
    parser.add_argument(
        "-s",
        "--size",
        type=int,
        help="threshold for size of files to copy (in MB)",
        required=True,
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    s3, bsrc, bdst = main(sys.argv[1:])
