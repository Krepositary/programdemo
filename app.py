import streamlit as st

# Sample data for books
books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "price": 10.99,
        "description": "A novel set in the Roaring Twenties.",
        "image": "https://images.unsplash.com/photo-1544759936-4b2f41c1b37e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDF8fGJvb2slMjBjb2xvdXJ8ZW58MHx8fHwxNjMzNjM1MTE3&ixlib=rb-1.2.1&q=80&w=400"
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "price": 12.99,
        "description": "A novel about racial injustice.",
        "image": "https://images.unsplash.com/photo-1532350419493-f712b0c25107?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDIyfHxib29rJTIwY29sb3V0ZSUyMGNvbG91bnxlbnwwfHx8fDE2MzM2MzY2MjM&ixlib=rb-1.2.1&q=80&w=400"
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "price": 14.99,
        "description": "A dystopian novel about totalitarianism.",
        "image": "https://images.unsplash.com/photo-1543269863-6c9ab4bb75f9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDE0fHxib29rJTIwY29sb3V0ZSUyMG5hbWV8ZW58MHx8fHwxNjMzNjM1MTE3&ixlib=rb-1.2.1&q=80&w=400"
    }
]

# Set the title and layout
st.title("📚 Online Bookstore")
st.markdown("<style>h1{color: #4B0082;} h2{color: #FF6347;}</style>", unsafe_allow_html=True)

# Shopping cart initialization
cart = []

# Display book cards
for book in books:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(book["image"], use_column_width=True)
        st.subheader(book["title"])
        st.write(f"**Author:** {book['author']}")
        st.write(f"**Price:** ${book['price']:.2f}")
        st.write(book["description"])
        
        # Add to cart button
        if st.button("Add to Cart", key=book["title"]):
            cart.append(book)
            st.success(f"Added {book['title']} to your cart!")

# Display shopping cart
if cart:
    st.sidebar.header("🛒 Your Cart")
    total_price = 0
    for item in cart:
        st.sidebar.write(f"{item['title']} - ${item['price']:.2f}")
        total_price += item["price"]
    st.sidebar.write(f"**Total Price:** ${total_price:.2f}")



