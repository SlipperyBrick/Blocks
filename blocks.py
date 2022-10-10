import json
import sys
import subprocess

'''

(blocks.py)

Blocks is an MDBook plugin/preprocessor which lets users construct beautiful Bootstrap components with "blocks" based markdown.

'''

if __name__ == '__main__':

    # Check if there have been any arguments received
    if len(sys.argv) > 1:

        # If the received argument is "supports" this preprocessor supports the default renderer
        if sys.argv[1] == "supports":

            # Return a status code of 0 to notify mdbook we support the default renderer
            sys.exit(0)
    
    # Load both the preprocess context and book representations from stdin
    context, book = json.load(sys.stdin)

    # Call the "blocks_preprocessor.py" script in a subprocess, passing the JSON object "book" as a serialized JSON string
    output = subprocess.Popen(args = [sys.executable, 'mdbook-blocks/blocks_preprocessor.py', json.dumps(book)], stdin = subprocess.PIPE, stdout = subprocess.PIPE)

    # Print contents of book
    print(json.dumps(json.loads(output.stdout.read().decode())))