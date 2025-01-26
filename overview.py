import streamlit as st
import pandas as pd

def render():
    
    st.title("🌟 MIND Dataset Overview 📰")
    st.markdown("""
    [The MIND dataset](https://msnews.github.io/) is a large-scale dataset for news recommendation collected from the Microsoft News platform. 
    This dashboard provides insights and analysis on:
    - 📊 User behaviors and impressions
    - 🗞️ News articles and their categories
    - 🌐 Knowledge graph embeddings for entities and relations

    ### Why is the MIND Dataset Important? 🤔
    - 🚀 Enables research on personalized news recommendation systems.
    - 🧠 Combines user interaction logs with semantic information from knowledge graphs.
    - 💡 Provides real-world data for developing and evaluating machine learning models.
    """)

    
    st.header("📂 Dataset Information")
    
    
    st.write("### 👤 Behaviors Data")
    behaviors = pd.read_csv("data/behaviors.csv")
    st.dataframe(behaviors.head())
    st.markdown("""
    #### Attributes in `behaviors.csv` 📋
    - **🆔 Impression ID**: Unique identifier for each session where a user interacted with displayed articles. This helps group related user interactions.
    - **👥 User ID**: An anonymized ID for each user. This links interactions across multiple sessions while preserving privacy.
    - **⏰ Time**: Timestamp of the session. Useful for understanding temporal patterns in user behavior.
    - **🕵️‍♀️ History**: List of previously clicked articles by the user, ordered by time. This attribute is crucial for modeling user preferences.
    - **📑 Impressions**: Contains the list of displayed articles in the session and indicates whether each article was clicked (1 for clicked, 0 for not clicked). It is the primary source for training recommendation models.
    """)
    st.write(f"📊 **Total Rows:** {len(behaviors)}")
    
    
    st.write("### 📰 News Data")
    news = pd.read_csv("data/news.csv")
    st.dataframe(news.head())
    st.markdown("""
    #### Attributes in `news.csv` 📋
    - **🆔 News ID**: Unique identifier for each news article. Links news metadata with user behavior data.
    - **📂 Category**: High-level thematic classification of the news (e.g., Sports, Politics).
    - **📄 SubCategory**: More specific classification under the main category (e.g., Football under Sports).
    - **📰 Title**: The headline of the news article. Useful for text-based recommendation models.
    - **✍️ Abstract**: A brief summary of the news article. Provides additional textual information for modeling.
    - **🔍 Title Entities**: Named entities in the title, extracted using natural language processing techniques. Enhances semantic understanding of the article.
    - **🌐 Abstract Entities**: Named entities in the abstract, further enriching the semantic context.
    """)
    st.write(f"📊 **Total Rows:** {len(news)}")

    
    st.write("### 🌐 Entity Embeddings")
    entities = pd.read_csv("data/entity_embedding.csv")
    st.dataframe(entities.head())
    st.markdown("""
    #### Attributes in `entity_embedding.csv` 📋
    - **🆔 Entity ID**: Unique identifier for each entity derived from WikiData.
    - **📈 Embedding Vector**: A 100-dimensional vector representing the semantic meaning of the entity. These embeddings are used to incorporate external knowledge into recommendation models.
    
    #### Why is this Important? 🤔
    - 🧠 Captures semantic relationships between entities.
    - 💡 Supports knowledge-aware recommendation models by linking entities to user interactions and news articles.
    """)
    st.write(f"📊 **Total Rows:** {len(entities)}")

    st.write("### 🔗 Relation Embeddings")
    relations = pd.read_csv("data/relation_embedding.csv")
    st.dataframe(relations.head())
    st.markdown("""
    #### Attributes in `relation_embedding.csv` 📋
    - **🆔 Relation ID**: Unique identifier for each relationship derived from WikiData.
    - **📈 Embedding Vector**: A 100-dimensional vector representing the semantic meaning of the relationship.

    #### Why is this Important? 🤔
    - 🔗 Encodes relationships between entities, such as "is related to" or "is part of."
    - 🌟 Enables context-aware recommendations by leveraging the relationships between entities.
    """)
    st.write(f"📊 **Total Rows:** {len(relations)}")
