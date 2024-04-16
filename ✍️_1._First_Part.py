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

st.header("1️⃣ Part 1: Text Annotation")

with st.container(border=True):
    text = """
    Jimmy’s father worked for OrganInc Farms. He was a genographer, one of the best in the field. He’d done some of the key studies on mapping the proteonome when he was still a post-grad, and then he’d helped engineer the Methuselah Mouse as part of Operation Immortality. After that, at OrganInc Farms, he’d been one of the foremost architects of the pigoon project, along with a team of transplant experts and the microbiologists who were splicing against infections. Pigoon was only a nickname: the official name was sus multiorganifer. But pigoon was what everyone said. Sometimes they said Organ-Oink Farms, but not as often. It wasn’t really a farm anyway, not like the farms in pictures.
    The goal of the pigoon project was to grow an assortment of foolproof human- tissue organs in a transgenic knockout pig host – organs that would transplant smoothly and avoid rejection, but would also be able to fend off attacks by opportunistic microbes and viruses, of which there were more strains every year. A rapid-maturity gene was spliced in so the pigoon kidneys and livers and hearts would be ready sooner, and now they were perfecting a pigoon that could grow five or six kidneys at a time. Such a host animal could be reaped of its extra kidneys; then, rather than being destroyed, it could keep on living and grow more organs, much as a lobster could grow another claw to replace a missing one. That would be less wasteful, as it took a lot of food and care to grow a pigoon. A great deal of investment money had gone into OrganInc Farms.
    All of this was explained to Jimmy when he was old enough.
    Old enough, Snowman thinks as he scratches himself, around but not on top of the insect bites. Such a dumb concept. Old enough for what? To drink, to fuck, to know better? What fathead was in charge of making those decisions? For example, Snowman himself isn’t old enough for this, this – what can it be called? This situation. He’ll never be old enough, no sane human being could ever . . .
    Each one of us must tread the path laid out before him, or her, says the voice in his head, a man’s this time, the style bogus guru, and each path is unique. It is not the nature of the path itself that should concern the seeker, but the grace and strength and patience with which each and every one of us follows the sometimes challenging . . .
    “Stuff it,” says Snowman. Some cheap do-it-yourself enlightenment handbook, Nirvana for halfwits. Though he has the nagging feeling that he may well have written this gem himself.
    In happier days, naturally. Oh, so much happier.
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
        st.switch_page("pages/✏️ 2. Second Part.py")

    if show_labels:
        with st.expander("Show Labels"):
            st.write(labels)
