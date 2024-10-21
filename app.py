pip install streamlit
import streamlit as st

# Set the title of the web app
st.title("Welcome to Travel Buddy")

# Sidebar for navigation
st.sidebar.header("Navigation")
options = ["Home", "Destinations", "Itineraries", "Contact Us"]
choice = st.sidebar.selectbox("Select Page", options)

# Home Page
if choice == "Home":
    st.subheader("Explore Your Next Adventure!")
    st.write("""
    Discover amazing destinations and create unforgettable memories with our travel services.
    """)
    st.image("https://images.unsplash.com/photo-1519821659843-e0f21c4c2d48", caption="Travel Adventure", use_column_width=True)

# Destinations Page
elif choice == "Destinations":
    st.subheader("Popular Destinations")
    destinations = {
        "Paris": "The City of Light is known for its art, fashion, and culture.",
        "Tokyo": "A bustling metropolis with a mix of traditional and modern attractions.",
        "New York": "The Big Apple is famous for its skyline, culture, and diverse food.",
        "Sydney": "Known for its Sydney Opera House and beautiful beaches.",
    }
    for place, description in destinations.items():
        st.markdown(f"**{place}**: {description}")

# Itineraries Page
elif choice == "Itineraries":
    st.subheader("Sample Itineraries")
    st.write("""
    Here are some sample itineraries to help you plan your next trip.
    """)
    itineraries = {
        "Paris in 3 Days": """
        - Day 1: Visit the Eiffel Tower and Louvre Museum
        - Day 2: Explore Montmartre and enjoy a Seine River cruise
        - Day 3: Visit Versailles
        """,
        "Tokyo in 4 Days": """
        - Day 1: Explore Shibuya and Shinjuku
        - Day 2: Visit Asakusa and Tokyo Skytree
        - Day 3: Day trip to Mount Fuji
        - Day 4: Visit Akihabara and Ueno Park
        """,
    }
    for title, itinerary in itineraries.items():
        st.markdown(f"**{title}**:\n{itinerary}")

# Contact Us Page
elif choice == "Contact Us":
    st.subheader("Get in Touch")
    st.write("""
    If you have any questions, feel free to contact us!
    """)
    contact_form = st.form(key='contact_form')
    name = contact_form.text_input("Name")
    email = contact_form.text_input("Email")
    message = contact_form.text_area("Message")
    submit_button = contact_form.form_submit_button("Submit")

    if submit_button:
        st.success("Thank you for contacting us!")

# Run the app
if __name__ == "__main__":
    st.write("Use the sidebar to navigate through the website.")
