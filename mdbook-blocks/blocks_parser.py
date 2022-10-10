import re
import uuid

import blocks_factory as blocks

'''

get_blocks(list): list

Get all code blocks from the content string.
Return the code blocks in a list.

'''

# Get all code blocks from the content string
def get_blocks(content, keepFormatting = False):

    code_blocks = []

    # Check for any "```blocks-" code blocks
    if '```blocks-' not in content:

        # If no "```blocks-" code blocks exist within the content string, return from this function
        return

    # If we have found any instances of "```blocks-" code blocks, process them
    else:

        # Find the amount of occurrences for "```blocks-" code blocks in the content string
        substring = "```blocks-"
        code_block_count = content.count(substring)

        # Iterate for however many code blocks there are extracting and storing them
        for substring in range(code_block_count):

            # Our regex searches for all content between two sets of "```"
            regex = re.search(r'(?:```blocks-)([\s\S]*?)(?:```)', content)

            # Check if we want to keep new lines and return carriages
            if(keepFormatting is True):

                # Store the first occurrence of a found code block
                code_blocks.append(regex.group(0))

            else:

                # Store the first occurrence of a found code block, replacing any instances of "\r" and "\n with a space
                code_blocks.append(regex.group(0).replace('\r', ' ').replace('\n', ' '))

            # Remove the found occurrence from the content string (if duplicates exist remove only the current match)
            content = content.replace(regex.group(0), '', 1)

        return code_blocks

'''

get_attributes(list): nested dictionary

Get all attributes from each code block.
Return as a nested dictionary.

'''

# Get all attributes from each code block
def get_attributes(code_blocks):

    attributes = {}
    components = {}

    # Iterate over each code block
    for block in code_blocks:

        # Find the amount of attributes
        substring = '\"'
        attribute_count = block.count(substring) // 2

        # Get the component name of the code block
        regex = re.search(r'(?:```blocks-)(.*?)(?:\s)', block)
        component_name = regex.group(1)

        # Iterate over all attributes
        for attribute in range(attribute_count):

            # Match the attribute name and value
            key = re.search(r'(?:\s)([\s\S]*?)(?:\:)', block)
            value = re.search(r'(?:\")([\s\S]*?)(?:\")', block)

            # Store both matches of attribute name and value
            attributes[key.group(1).lstrip().rstrip()] = value.group(1).lstrip().rstrip()

            # Remove the found attribute key and value from the code block (if duplicates exist remove only the current match)
            block = block.replace(key.group(1) + ':', '', 1).replace('"' + value.group(1) + '"', '', 1)

        # Copy the contents of the attributes for each code block, assigning a uuid for each component (prevents same keys from overwriting each other)
        components[component_name + '_' + str(uuid.uuid4())[:3]] = attributes.copy()

        attributes.clear()

    return components

'''

construct_html(dictionary): list

Get all attributes from each code block and construct relevant html.
Return as a list.

'''

def construct_html(attributes):

    components = []

    is_aligned = False

    for attribute in attributes:
        
        # Matches a word followed by an underscore from the attributes dictionary (ex. "card_123" matches "card")
        regex = re.search('(\w+(?=_))', attribute)
        component_name = regex.group(0)

        if 'align' in attributes[attribute]:

            is_aligned = True;

        # Call our blocks factory to construct the HTML for the current component
        factory_component = blocks.blocks_factory(component_name)
        component = factory_component.create_component(attributes[attribute])

        # Append the HTML component to the components list
        components.append(component)

    # Check if component has 'align' key
    if is_aligned == True:

        # Align the components
        components = make_aligned(components)

    return components

'''

check_aligned(dictionary): list

Get all components with align attribute and add Bootstrap "row" CSS class to start of an aligned component
and a closing "</div>" to end of aligned component group.
Return as a list

'''

def make_aligned(components):

    align_count = 0
    component_count = 0
    index = 0

    # Iterate over all components to find aligned ones
    for component in components:

        # If there is an occurence of '<aligned>'
        if '<aligned>' in component:

            # If this is our first occurence of '<aligned>'
            if align_count == 0:

                components[index] = component.replace('<aligned>', '<aligned-first>', 1)

            # If this isn't our first occurence of '<aligned>'
            else:

                # Check if we are at the last element of the list
                if len(components) == index + 1:

                    components[index] = component.replace('<aligned>', '<aligned-last>', 1)

                # If we aren't at the last element in the list, check one element ahead for an occurence of '<aligned>'
                elif '<aligned>' not in components[index + 1]:

                    components[index] = component.replace('<aligned>', '<aligned-last>', 1)

            # Increment our align counter
            align_count += 1

        else:

            # Reset our align counter
            align_count = 0

        # Increment our index
        index += 1

    # Reset our index
    index = 0

    # Iterate over all components to find the first and last aligned ones
    for component in components:

        component_count += 1

        if '<aligned-first>' in component:

            components[index] = component.replace('<aligned-first>', '<div class="row justify-content-center">', 1)

        elif '<aligned-last>' in component:

            components[index] = component.replace('<aligned-last>', '', 1) + '</div>'

        if len(components) != index + 1:

            if '<aligned-first>' in component and '<aligned>' not in components[index + 1]:

                components[index] = components[index] + '</div>'

            elif '<aligned>' in component:

                components[index] = component.replace('<aligned>', '', 1)

        index += 1

    return components

'''

pre_process(list, str): str

Get all code blocks from a content string and replace with their HTML counterparts
Return as a string.

'''

def pre_process(html, content):

    # Keep track of code block counts
    code_block_counter = 0

    # Retrieve all the code blocks for the current content string
    code_blocks = get_blocks(content, True)

    for block in code_blocks:

        # Replace the current code block with its corresponding HTML
        content = content.replace(block, html[code_block_counter], 1)

        # Increment our code block counter
        code_block_counter += 1

    return content