import json

def load(input_filename):
    """Parse and return a JSON file from a file.

    This is overly simple, you could do this with Jinja2 in the suite.rc file, but in
    the real world loading data can often be a bit more involved so this shows how you
    can run any arbitrary Python code in the generation of your suite.

    """
    with open(input_filename, 'r') as json_file:
        return json.load(json_file)
