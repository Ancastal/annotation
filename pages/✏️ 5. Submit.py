import base64
import requests
import json
import tomllib
import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from streamlit_annotation_tools import text_labeler

st.set_page_config(page_title="Text Labeler", page_icon="📝", layout="wide")

github_api = st.secrets['GITHUB_TOKEN']


def upload_to_github(file, path, repo, token):
    """
    Uploads a file to GitHub.
    Args:
    - file: file object to upload.
    - path: path in the repository (including filename).
    - repo: repository name, e.g., 'username/repo'.
    - token: GitHub Personal Access Token.
    """
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }
    content = base64.b64encode(file).decode('utf-8')
    data = {
        "message": "Upload annotations",
        "content": content
    }
    response = requests.put(url, headers=headers, json=data)
    return response.json()


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

st.header("📝 Submit Annotations")
with st.form(key="form"):
    st.write("Please, fill in the information below")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
    with col2:
        surname = st.text_input("Surname")

    st.write(
        "Please, upload the annotations you have downloaded from the previous sections")
    col1, col2 = st.columns(2)

    with col1:
        file_1 = st.file_uploader("**Upload Labels - Part 1**", type=["json"])
    with col2:
        file_2 = st.file_uploader("**Upload Labels - Part 2**", type=["json"])
    with col1:
        file_3 = st.file_uploader("**Upload Labels - Part 3**", type=["json"])
    with col2:
        file_4 = st.file_uploader("**Upload Labels - Part 4**", type=["json"])

    submit = st.form_submit_button(
        "Submit Annotations", use_container_width=True, type="primary")
    if submit:
        for file in [file_1, file_2, file_3, file_4]:
            index = [file_1, file_2, file_3, file_4].index(file)
            if file is not None:
                upload_to_github(
                    file.read(
                    ), f"annotations/{surname}.{name[0]}-{index}.json", "Ancastal/annotation",
                    "")
        st.success("Thank you for your task! 🙏")
        st.stop()
