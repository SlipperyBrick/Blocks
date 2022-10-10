import json
import sys

import blocks_parser as blocks_parser

# Retrieve the book data
#book = json.loads(sys.argv[1])

# FOR DEBUG PURPOSES
file = open('output/test-book.json')
book = json.load(file)

# Keep track of chapter counts
chapter_counter = 0

# Get all chapters of the book
chapters = book['sections']

# Iterate over each chapter of the book
for chapter in chapters:

    # Get each code block
    code_blocks = blocks_parser.get_blocks(chapter['Chapter'].get('content'))

    # Get the attributes of each code block
    attributes = blocks_parser.get_attributes(code_blocks)

    # Construct the HTML for each code block using the attributes
    html = blocks_parser.construct_html(attributes)

    # Replace all code blocks with their corresponding HTML output
    book['sections'][chapter_counter]['Chapter']['content'] = blocks_parser.pre_process(html, chapter['Chapter'].get('content'))

    # Increment our chapter counter
    chapter_counter += 1

# Write the contents of the book in JSON representation to stdout
sys.stdout.write(json.dumps(book))