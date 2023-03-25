import streamlit as st
import numpy as np
import pandas as pd

st.write("Hello World")
st.write(1234)

st.title("DataFrame")

df = pd.DataFrame({
    "first-column":[1,2,3,4,5],
    "second-column":[6,7,8,9,10]
})

st.write(df)

st.write(np.array([1,2,3,4]))

df1 = pd.DataFrame({
    "first-column":[1,2,3,4,5],
    "second-column":[6,7,8,9,10]
})

df1

st.markdown('''
# Markdown
## For Heading Level -1 or Title use (#)
### For Heading Level -2 or Header use (##)
#### For Heading Level -3 or Subheader use (###)
For Heading Level -4 

To create paragraphs, use a blank line to separate one or more lines of text.

---

### Emphasis
making text bold, italic, bold italic
To **bold text**, add **two asterisks or underscores before and after a word or phrase**
To *italicize text*, add *one asterisk or underscore before and after a word or phrase.* 
Add three asterisks or underscores before and after a word or ***phrase for bold italic***

### Blockquotes
To create a blockquote, add a > in front of a paragraph.
> Dorothy followed her through many of the beautiful rooms in her castle.
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

### List

1. Order List (items with number)
2. First item
3. Second item
4. third item
5. Fourth item

    1. Intendent Item1
    2. Intendent Item2

### Unordered List
add dashes (-), asterisks (*), or plus signs (+) in front of line items.

- First item
- Second item
- Third item
    - Fourth item

### Links
To create a link, enclose the link text in brackets and then follow it immediately with the URL in parentheses
My favorite search engine is [Duck Duck Go](https://duckduckgo.com).

### URLs and Email Address
To quickly turn a URL or email address into a link, enclose it in angle brackets.
- <https://www.datascienceanywhere.org>
- <srikanthdakoju@gmail.com>

### Images
To add an image, add an exclamation mark (!), followed by alt text in brackets, and the path or URL to the image asset in parentheses. You can optionally add a title in quotation marks after the path or URL. 

![Mountains are beautiful](https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80)

            ''')


st.title("This is Title")
st.caption("using st.title() you can display the text in title format")

st.header("This is Header")
st.caption("using st.title() you can display the text in title format")

st.subheader("This is subheader")
st.caption("using st.title() you can display the text in title format")

st.markdown('---')
st.subheader("Generate Random Numbers")
body = """
import numpy as np

def generate_random(size):
    rand = random.random(size=size)
    return rand
    
number = generate_random(10)
"""
st.code(body, language='python')

st.subheader("Latex")
formula = """
a + ar + ar^2 + ar^3 + \cdots + ar^(n-1) = \sum_{k=0}^{n-1} ar^k
"""
st.latex(formula)

