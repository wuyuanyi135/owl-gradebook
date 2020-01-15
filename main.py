import argparse

from interaction import interaction_entry

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    interaction_entry(args.filename)
