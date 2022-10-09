import streamlit as st
import base64

# Function to Encode

def Encode(key, message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Function to decode

def Decode(key, message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

message = st.text_input('Message Text')

key = st.text_input(
    "Private key", type="password"
)

mode = st.selectbox(
    "What action would you like to perform?",
    ("Encode", "Decode")
)

if st.button('Result'):
    if (mode == "Encode"):
        # Encode(key, message)
        st.write(Encode(key, message))
    else:
        st.write(Decode(key, message))
else:
    st.write('Please enter all the required information!!')

