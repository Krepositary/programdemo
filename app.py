import streamlit as st

# Sample data for books
books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "price": 10.99,
        "description": "A novel set in the Roaring Twenties.",
        "image": "https://images.unsplash.com/photo-1544759936-4b2f41c1b37e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDF8fGJvb2slMjBjb2xvdXJ8ZW58MHx8fHwxNjMzNjM1MTE3&ixlib=rb-1.2.1&q=80&w=400",
        "tags": ["classic", "novel", "literature"]
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "price": 12.99,
        "description": "A novel about racial injustice.",
        "image": "https://images.unsplash.com/photo-1532350419493-f712b0c25107?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDIyfHxib29rJTIwY29sb3V0ZSUyMGNvbG91bnxlbnwwfHx8fDE2MzM2MzY2MjM&ixlib=rb-1.2.1&q=80&w=400",
        "tags": ["classic", "literature", "social"]
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "price": 14.99,
        "description": "A dystopian novel about totalitarianism.",
        "image": "https://images.unsplash.com/photo-1543269863-6c9ab4bb75f9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDE0fHxib29rJTIwY29sb3V0ZSUyMG5hbWV8ZW58MHx8fHwxNjMzNjM1MTE3&ixlib=rb-1.2.1&q=80&w=400",
        "tags": ["dystopian", "political", "literature"]
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "price": 11.99,
        "description": "A romantic novel that critiques the British landed gentry.",
        "image": "https://images.unsplash.com/photo-1593642632823-e3ba83b1d0e3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDE2fHxib29rJTIwY29sb3V0ZSUyMG5hbWV8ZW58MHx8fHwxNjMzNjM1MTE3&ixlib=rb-1.2.1&q=80&w=400",
        "tags": ["romance", "classic", "literature"]
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "price": 13.99,
        "description": "A story about teenage angst and alienation.",
        "image": "https://images.unsplash.com/photo-1543269863-6c9ab4bb75f9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDIyfHxib29rJTIwY29sb3V0ZSUyMG5hbWV8ZW58MHx8fHwxNjMzNjM1MTE3&ixlib=rb-1.2.1&q=80&w=400",
        "tags": ["classic", "novel", "coming-of-age"]
    },
]

# Initialize session state for cart and wishlist
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'wishlist' not in st.session_state:
    st.session_state.wishlist = []

def recommend_books(book):
    """Recommend books based on matching tags."""
    recommendations = [b for b in books if book["title"] != b["title"] and set(b["tags"]).intersection(set(book["tags"]))]
    return recommendations[:2]  # Return 2 recommended books

def display_books():
    """Display all books and their details."""
    for book in books:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.image(book["image"], use_column_width=True)
            st.subheader(book["title"])
            st.write(f"**Author:** {book['author']}")
            st.write(f"**Price:** ${book['price']:.2f}")
            st.write(book["description"])

            # Add to cart button
            if st.button("Add to Cart", key=f"cart_{book['title']}"):
                st.session_state.cart.append(book)
                st.success(f"Added {book['title']} to your cart!")

            # Add to wishlist button
            if st.button("Add to Wishlist", key=f"wishlist_{book['title']}"):
                st.session_state.wishlist.append(book)
                st.success(f"Added {book['title']} to your wishlist!")

        with col2:
            st.write("### You May Also Like:")
            for recommended in recommend_books(book):
                st.image(recommended["image"], width=100)
                st.write(recommended["title"])
                st.write(f"**Price:** ${recommended['price']:.2f}")
                st.write("---")

def display_sidebar():
    """Display shopping cart and wishlist in the sidebar."""
    with st.sidebar:
        st.header("🛒 Your Cart")
        if st.session_state.cart:
            total_price = sum(item["price"] for item in st.session_state.cart)
            for item in st.session_state.cart:
                st.write(f"{item['title']} - ${item['price']:.2f}")
            st.write(f"**Total Price:** ${total_price:.2f}")
        else:
            st.write("Your cart is empty.")

        st.header("💖 Your Wishlist")
        if st.session_state.wishlist:
            for item in st.session_state.wishlist:
                st.write(item["title"])
        else:
            st.write("Your wishlist is empty.")

def main():
    """Main function to run the bookstore app."""
    st.title("📚 Online Bookstore APP")
    st.markdown("<style>h1{color: #4B0082;} h2{color: #FF6347;}</style>", unsafe_allow_html=True)
    
    display_books()
    display_sidebar()

if __name__ == "__main__":
    main()
