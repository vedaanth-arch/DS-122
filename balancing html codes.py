def isbalanced(html_string):
    stack = []
    i = 0 # variable for  the index of the string

    
    while i < len(html_string):
        # Find the next tag
        if html_string[i] == '<':
            # Detect if it's a closing tag
            if html_string[i+1] == '/':
                # Extract the closing tag name
                j = i + 2
                while j < len(html_string) and html_string[j] != '>':
                    j += 1
                closing_tag = html_string[i+2:j]

                # Check if the stack is empty or top of stack doesn't match the closing tag
                if not stack or stack[-1] != closing_tag:
                    return False  # Unbalanced tag

                # Pop the matching opening tag from the stack
                stack.pop()
            else:
                # Extract the opening tag name
                j = i + 1
                while j < len(html_string) and html_string[j] != '>':
                    j += 1
                opening_tag = html_string[i+1:j]

                # Push the opening tag to the stack
                stack.append(opening_tag)

            # Move the index to the end of the current tag
            i = j
        i += 1

    # If the stack is empty, all tags were balanced
    return len(stack) == 0

# Example Usage:
html_example_1 = """
<html>
  <body>
    <h1>This is heading 1</h1>
    <h2>This is heading 2</h2>
    <h3>This is heading 3</h3>
  </body>
</html>
"""

html_example_2 = """
<html>
  <body>
    <h1>This is heading 1</h1>
    <h2>This is heading 2</h2>
    <h3>This is heading 3</h2>
  </body>
</html>
"""

# Test Example 1: Balanced HTML
print("Example 1 is balanced:", isbalanced(html_example_1))  # Should print: True

# Test Example 2: Unbalanced HTML
print("Example 2 is balanced:", isbalanced(html_example_2))  # Should print: False
