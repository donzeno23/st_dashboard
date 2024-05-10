import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

st.write("This is just a sample page!")

selection = st.radio(
    "Test page hiding",
    ["Show all pages", "Hide pages 1 and 2", "Hide Other apps Section"],
)

if selection == "Show all pages":
    hide_pages([])
elif selection == "Hide pages 1 and 2":
    hide_pages(["Example One", "Example Two"])
elif selection == "Hide Other apps Section":
    hide_pages(["Other apps"])

st.selectbox("test_select", options=["1", "2", "3"])


hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
st.write(f"You selected: {hour_to_filter}")

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'

#######################

# if 'button' not in st.session_state:
#     st.session_state.button = False

# def click_button():
#     st.session_state.button = not st.session_state.button

# st.button('Click me', on_click=click_button)

# if st.session_state.button:
#     # The message and nested widget will remain on the page
#     st.write('Button is on!')
#     st.slider('Select a value')
# else:
#     st.write('Button is off!')

#########################

# if 'button' not in st.session_state:
#     st.session_state.button = False

# def click_button():
#     st.session_state.button = not st.session_state.button

# st.button('Click me', on_click=click_button)

# st.slider('Select a value', disabled=st.session_state.button)

###########################

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    name = st.text_input('Name', on_change=set_state, args=[2])

if st.session_state.stage >= 2:
    st.write(f'Hello {name}!')
    color = st.selectbox(
        'Pick a Color',
        [None, 'red', 'orange', 'green', 'blue', 'violet'],
        on_change=set_state, args=[3]
    )
    if color is None:
        set_state(2)

if st.session_state.stage >= 3:
    st.write(f':{color}[Thank you!]')
    st.button('Start Over', on_click=set_state, args=[0])