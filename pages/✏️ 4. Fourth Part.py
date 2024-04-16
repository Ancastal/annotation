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
Units of Creative Potential include, but are not limited to, the following categories:
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

st.header("4️⃣ Part 4: Text Annotation")

with st.container(border=True):
    text = """
When Jimmy was really little they’d lived in a Cape Cod–style frame house in one of the Modules – there were pictures of him, in a carry-cot on the porch, with dates and everything, stuck into a photo album at some time when his mother was still bothering – but now they lived in a large Georgian centre-plan with an indoor swimming pool and a small gym. The furniture in it was called reproduction. Jimmy was quite old before he realized what this word meant – that for each reproduction item, there was supposed to be an original somewhere.
Or there had been once. Or something.
The house, the pool, the furniture – all belonged to the OrganInc Compound, where the top people lived. Increasingly, the middle-range execs and the junior scientists lived there too. Jimmy’s father said it was better that way, because nobody had to commute to work from the Modules. Despite the sterile transport corridors and the high-speed bullet trains, there was always a risk when you went through the city.
Jimmy had never been to the city. He’d only seen it on TV – endless billboards and neon signs and stretches of buildings, tall and short; endless dingy-looking streets, countless vehicles of all kinds, some of them with clouds of smoke coming out the back; thousands of people, hurrying, cheering, rioting. There were other cities too, near and far; some had better neighbourhoods in them, said his father, almost like the Compounds, with high walls around the houses, but those didn’t get on TV much.
Compound people didn’t go to the cities unless they had to, and then never alone. They called the cities the pleeblands. Despite the fingerprint identity cards now carried by everyone, public security in the pleeblands was leaky: there were people cruising around in those places who could forge anything and who might be anybody, not to mention the loose change – the addicts, the muggers, the paupers, the crazies. So it was best for everyone at OrganInc Farms to live all in one place, with foolproof procedures.

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
        st.switch_page("pages/✏️ 5. Fifth Part.py")

    if show_labels:
        with st.expander("Show Labels"):
            st.write(labels)
