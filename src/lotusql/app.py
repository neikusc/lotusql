import sys, pathlib
PROJECT_ROOT = pathlib.Path('/Users/kientrinh/src/agents/lotusql').resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import asyncio
import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from src.lotusql.chat_agent import run_conversation

def generate_response(prompt: str, msgs: StreamlitChatMessageHistory):
    
    # response = st.session_state.get("response", "")
    # response = run_conversation(user_query=prompt)
    response = asyncio.run(run_conversation(user_query=prompt))
    return response, "Source: LotusQL"

def main():
    st.sidebar.markdown("**Welcome to LotusQL!**")

    # Reset button
    reset_button = st.sidebar.button("Clear Conversation")

    # Store session conversation history for memory
    msgs = StreamlitChatMessageHistory(key="langchain_messages")

    # Store LLM responses
    if "messages" not in st.session_state or reset_button:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "How may I help you?"}
        ]

    # Display chat messages
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.write(msg["content"])
        elif msg["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(msg["content"])
                if "sources" in msg:
                    st.write(msg["sources"])

    # Accept user prompt
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt.replace("\n", "\\n"))

    # Generate new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer, sources = generate_response(prompt, msgs)
                st.write(answer)
                st.write(sources)

        # Store assistant response
        st.session_state.messages.append(
            {"role": "assistant", "content": answer, "sources": sources}
        )

if __name__ == "__main__":
    # Define custom CSS to adjust the chat input width
    custom_css = """
    <style>
    div[data-testid="stChatInput"] {
        width: 140% !important;  /* Set desired width */
        margin: 0 auto;          /* Center the chat input */
    }
    </style>
    """
    # Inject the custom CSS into the Streamlit app
    st.markdown(custom_css, unsafe_allow_html=True)

    st.set_page_config(layout="wide", initial_sidebar_state="auto")
    st.title("LotusQL: Your AI Data Assistant")
    st.sidebar.image("agent-icon.jpg", width=170)

    main()