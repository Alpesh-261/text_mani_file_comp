import argparse
import os
import zipfile

def replace_text(file, find, replace):
    try:
        with open(file, 'r') as f:
            content = f.read()
        content = content.replace(find, replace)
        print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def convert_case(file, case):
    try:
        with open(file, 'r') as f:
            content = f.read()
        if case == 'upper':
            content = content.upper()
        elif case == 'lower':
            content = content.lower()
        print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def count_word(file, word):
    try:
        with open(file, 'r') as f:
            content = f.read()
        count = content.count(word)
        print(f"The word '{word}' occurs {count} times.")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def compress_file(file, output):
    try:
        with zipfile.ZipFile(output, 'w') as zipf:
            zipf.write(file, os.path.basename(file))
        print(f"File '{file}' compressed into '{output}'")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Text Manipulation Utility')
    subparsers = parser.add_subparsers(dest='command')

    parser_replace = subparsers.add_parser('replace', help='Find and replace text')
    parser_replace.add_argument('file', help='File to process')
    parser_replace.add_argument('find', help='Text to find')
    parser_replace.add_argument('replace', help='Text to replace with')

    parser_case = subparsers.add_parser('case', help='Convert text case')
    parser_case.add_argument('file', help='File to process')
    parser_case.add_argument('case', choices=['upper', 'lower'], help='Case to convert to')

    parser_count = subparsers.add_parser('count', help='Count occurrences of a word')
    parser_count.add_argument('file', help='File to process')
    parser_count.add_argument('word', help='Word to count')

    parser_compress = subparsers.add_parser('compress', help='Compress a file into a ZIP archive')
    parser_compress.add_argument('file', help='File to compress')
    parser_compress.add_argument('output', help='Output ZIP file name')

    args = parser.parse_args()

    if args.command == 'replace':
        replace_text(args.file, args.find, args.replace)
    elif args.command == 'case':
        convert_case(args.file, args.case)
    elif args.command == 'count':
        count_word(args.file, args.word)
    elif args.command == 'compress':
        compress_file(args.file, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
