from streamlit_js_eval import streamlit_js_eval
import json
from streamlit_annotation_tools import text_labeler
import streamlit as st
st.set_page_config(page_title="Text Labeler", page_icon="📝", layout="wide")

st.title("📝 Text Labeler Tool")
st.write(
    """
    This website application was developed in the context of the research project _Extending CREAMT with LLMs_.
    Your task is to use the tool below to label **Units of Creative Potential** (UCPs) within the text.

    Units of Creative Potential are units expected to require translators to use problem-solving skills.
    Such units are possibly expected to require particular cognitive effort in their translation process.

    """)
with st.expander("ℹ️ What are the possible types of UCPs?"):
    st.write("""
Units of Creative Potential include, but are not limited, to the following categories:
- Metaphors and imagery
- Comparisons
- Idiomatic phrases
- Wordplay and puns
- Onomatopoeias
- Phrasal verbs
- Cultural and historical references
- Neologisms
- Lexical variety
-  Expressions specific to linguistic variety (e.g. AmE or BrE)
-  Unusual punctuation
-  Rhyme and metrics
-  Proper names
-  Register (formal or informal)
""")

st.header("2️⃣ Part 2: Text Annotation")

with st.container(border=True):
    text = """
    The pigoon organs could be customized, using cells from individual human donors, and the organs were frozen until needed. It was much cheaper than getting yourself cloned for spare parts – a few wrinkles left to be ironed out there, as Jimmy’s dad used to say – or keeping a for-harvest child or two stashed away in some illegal baby orchard. In the OrganInc brochures and promotional materials, glossy and discreetly worded, stress was laid on the efficacy and comparative health benefits of the pigoon procedure. Also, to set the queasy at ease, it was claimed that none of the defunct pigoons ended up as bacon and sausages: No one would want to eat an animal whose cells might be identical with at least some of their own.
Still, as time went on and the coastal aquifers turned salty and the northern permafrost melted and the vast tundra bubbled with methane, and the drought in the midcontinental plains regions went on and on, and the Asian steppes turned to sand dunes, and meat became harder to come by, some people had their doubts. Within OrganInc Farms itself it was noticeable how often back bacon and ham sandwiches and pork pies turned up on the staff café menu. André’s Bistro was the official name of the café, but the regulars called it Grunts. When Jimmy had lunch there with his father, as he did when his mother was feeling harried, the men and women at nearby tables would make jokes in bad taste.
“Pigoon pie again,” they would say. “Pigoon pancakes, pigoon popcorn. Come on, Jimmy, eat up!” This would upset Jimmy; he was confused about who should be allowed to eat what. He didn’t want to eat a pigoon, because he thought of the pigoons as creatures much like himself. Neither he nor they had a lot of say in what was going on.
“Don’t pay any attention to them, sweetheart,” said Ramona. “They’re only teasing, you know?” Ramona was one of his dad’s lab technicians. She often ate lunch with the two of them, him and his dad. She was young, younger than his father and even his mother; she looked something like the picture of the girl in the haircut man’s window, she had the same sort of puffed-out mouth, and big eyes like that, big and smudgy. But she smiled a lot, and she didn’t have her hair
in quills. Her hair was soft and dark. Jimmy’s mother’s hair was what she herself called dirty blonde. (“Not dirty enough,” said his father. “Hey! Joke. Joke. Don’t kill me!”)
Ramona would always have a salad. “How’s Sharon doing?” she would say to Jimmy’s father, looking at him with her eyes wide and solemn. Sharon was Jimmy’s mother.
“Not so hot,” Jimmy’s father would say. “Oh, that’s too bad.”
“It’s a problem. I’m getting worried.”

    """

    labels = text_labeler(text, labels={
        "Metaphor": [],
        "Comparison": [],
        "Idiomatic Phrase": [],
        "Wordplay": [],
        "Onomatopoeia": [],
        "Phrasal Verb": [],
        "Cultural Reference": [],
        "Neologism": [],
        "Lexical Variety": [],
        "Linguistic Variety": [],
        "Punctuation": [],
        "Rhyme": [],
        "Proper Name": [],
        "Register": []
    })

    # We turn labels into json
    labels_json = json.dumps(labels)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.download_button(
            label="Download Labels",
            data=labels_json,
            file_name="labels_1.json",
            mime="application/json",
            type="primary",
            use_container_width=True
        )
    with col2:
        if st.button("Reset Labels", use_container_width=True):
            streamlit_js_eval(js_expressions="parent.window.location.reload()")
    with col3:
        if st.button("Show Labels", use_container_width=True):
            with st.expander("Show Labels"):
                st.write(labels)
    if st.button("Next Part", use_container_width=True):
        st.switch_page("pages/✏️ 3. Third Part.py")
