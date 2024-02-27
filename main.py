import streamlit as st

# DUMMY DATA
# messages_dummy_data = [
#     {
#       "role": "user",
#       "content": "User message content",
#     },
#     {
#       "role": "assistant",
#       "content": "Hello, how are you?",
#     },
# ]


# CONSTANTS
MESSAGES = "messages"


# Page title
st.title("Echo Chat")


# Initialising state
if MESSAGES not in st.session_state:
    st.session_state[MESSAGES] = []


# Display chat message from history on app re-run:
for messsage in st.session_state[MESSAGES]:
    with st.chat_message(name=messsage["role"]):
        st.write(messsage["content"])


# create a pompt component 
if prompt := st.chat_input("What is up?"):
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    # save user answer to state
    st.session_state[MESSAGES].append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(f"Echo: {prompt}")
    # save user answer to state
    st.session_state[MESSAGES].append(
        {
            "role": "assistant",
            "content": f"Echo: {prompt}",
        }
    )
