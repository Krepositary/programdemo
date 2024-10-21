import streamlit as st

# Sample data for books
books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "price": 10.99,
        "description": "A novel set in the Roaring Twenties that tells the story of Jay Gatsby and his love for Daisy Buchanan.",
        "image": "https://images.unsplash.com/photo-1593642632823-e3ba83b1d0e3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDF8fGJvb2slMjBjb3ZlcnxlbnwwfHx8fDE2MzAxNzg5NDA&ixlib=rb-1.2.1&q=80&w=400"
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "price": 12.99,
        "description": "A novel about the serious issues of rape and racial inequality set in the Deep South.",
        "image": "https://images.unsplash.com/photo-1593642632823-e3ba83b1d0e3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDIwfHxib29rJTIwY29sdW1ufGVufDB8fHx8MTYzMDE4MDE4MQ&ixlib=rb-1.2.1&q=80&w=400"
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "price": 14.99,
        "description": "A dystopian social science fiction novel and cautionary tale about the future.",
        "image": "https://images.unsplash.com/photo-1593642632823-e3ba83b1d0e3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDEyfHxib29rJTIwY29sdW1ufGVufDB8fHx8MTYzMDE4MDE4MQ&ixlib=rb-1.2.1&q=80&w=400"
    }
]

# Set the title of the web app
st.title("Online Bookstore")

# Sidebar for navigation
st.sidebar.header("Shopping Cart")
cart = []

# Main content
for book in books:
    st.subheader(book["title"])
    st.image(book["image"], width=150)
    st.write(f"**Author:** {book['author']}")
    st.write(f"**Price:** ${book['price']:.2f}")
    st.write(f"**Description:** {book['description']}")
    
    # Add to cart button
    if st.button("Add to Cart", key=book["title"]):
        cart.append(book)
        st.success(f"Added {book['title']} to your cart!")

# Display shopping cart
if cart:
    st.sidebar.subheader("Your Cart")
    total_price = 0
    for item in cart:
        st.sidebar.write(f"{item['title']} - ${item['price']:.2f}")
        total_price += item["price"]
    st.sidebar.write(f"**Total Price:** ${total_price:.2f}")

# Run the app
if __name__ == "__main__":
    st.write("Explore our collection of books and add your favorites to your cart!")

