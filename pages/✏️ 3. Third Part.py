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

st.header("3️⃣ Part 3: Text Annotation")

with st.container(border=True):
    text = """
Jimmy watched Ramona eat. She took very small bites, and managed to chew up the lettuce without crunching. The raw carrots too. That was amazing, as if she could liquefy those hard, crisp foods and suck them into herself, like an alien mosquito creature on DVD.
“Maybe she should, I don’t know, see someone?” Ramona’s eyebrows lifted in concern. She had mauve powder on her eyelids, a little too much; it made them crinkly. “They can do all sorts of things, there’s so many new pills . . .” Ramona was supposed to be a tech genius but she talked like a shower-gel babe in an ad. She wasn’t stupid, said Jimmy’s dad, she just didn’t want to put her neuron power into long sentences. There were a lot of people like that at OrganInc, and not all of them were women. It was because they were numbers people, not word people, said Jimmy’s father. Jimmy already knew that he himself was not a numbers person.
“Don’t think I haven’t suggested it, I asked around, found the top guy, made the appointment, but she wouldn’t go,” said Jimmy’s father, looking down at the table. “She’s got her own ideas.”
“It’s such a shame, a waste. I mean, she was so smart!”
“Oh, she’s still smart enough,” said Jimmy’s father. “She’s got smart coming out of her ears.”
“But she used to be so, you know . . .”
Ramona’s fork would slide out of her fingers, and the two of them would stare at each other as if searching for the perfect adjective to describe what Jimmy’s mother used to be. Then they’d notice Jimmy listening, and beam their attention down on him like extraterrestrial rays. Way too bright.
“So, Jimmy sweetheart, how’s it going at school?”
“Eat up, old buddy, eat the crusts, put some hair on your chest!” “Can I go look at the pigoons?” Jimmy would say.
The pigoons were much bigger and fatter than ordinary pigs, to leave room for all of the extra organs. They were kept in special buildings, heavily secured: the kidnapping of a pigoon and its finely honed genetic material by a rival outfit would have been a disaster. When Jimmy went in to visit the pigoons he had to put on a biosuit that was too big for him, and wear a face mask, and wash his hands first with disinfectant soap. He especially liked the small pigoons, twelve to a sow and lined up in a row, guzzling milk. Pigoonlets. They were cute. But the adults were slightly frightening, with their runny noses and tiny, white- lashed pink eyes. They glanced up at him as if they saw him, really saw him, and might have plans for him later.
“Pigoon, balloon, pigoon, balloon,” he would chant to pacify them, hanging over the edge of the pen. Right after the pens had been washed out they didn’t smell too bad. He was glad he didn’t live in a pen, where he’d have to lie around in poop and pee. The pigoons had no toilets and did it anywhere; this caused him a vague sensation of shame. But he hadn’t wet his bed for a long time, or he didn’t think he had.
“Don’t fall in,” said his father. “They’ll eat you up in a minute.”
“No they won’t,” said Jimmy. Because I’m their friend, he thought. Because I sing to them. He wished he had a long stick, so he could poke them – not to hurt them, just to make them run around. They spent far too much time doing nothing.

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
        st.switch_page("pages/✏️ 4. Fourth Part.py")
