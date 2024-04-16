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

st.header("5️⃣ Part 5: Text Annotation")

with st.container(border=True):
    text = """
Outside the OrganInc walls and gates and searchlights, things were unpredictable. Inside, they were the way it used to be when Jimmy’s father was a kid, before things got so serious, or that’s what Jimmy’s father said. Jimmy’s mother said it was all artificial, it was just a theme park and you could never bring the old ways back, but Jimmy’s father said why knock it? You could walk around without fear, couldn’t you? Go for a bike ride, sit at a sidewalk café, buy an ice-cream cone? Jimmy knew his father was right, because he himself had done all of these things.
Still, the CorpSeCorps men – the ones Jimmy’s father called our people – these men had to be on constant alert. When there was so much at stake, there was no telling what the other side might resort to. The other side, or the other sides: it wasn’t just one other side you had to watch out for. Other companies, other countries, various factions and plotters. There was too much hardware around, said Jimmy’s father. Too much hardware, too much software, too many
hostile bioforms, too many weapons of every kind. And too much envy and fanaticism and bad faith.
Long ago, in the days of knights and dragons, the kings and dukes had lived in castles, with high walls and drawbridges and slots on the ramparts so you could pour hot pitch on your enemies, said Jimmy’s father, and the Compounds were the same idea. Castles were for keeping you and your buddies nice and safe inside, and for keeping everybody else outside.
“So are we the kings and dukes?” asked Jimmy. “Oh, absolutely,” said his father, laughing.
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
        show_labels = st.button("Show Labels", use_container_width=True)
    if st.button("Next Part", use_container_width=True):
        st.success(
            "You have completed the annotation of the text. Thank you for your participation! 🎉🎉🎉")

    if show_labels:
        with st.expander("Show Labels"):
            st.write(labels)
