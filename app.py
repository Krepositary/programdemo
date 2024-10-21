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
        "aut



