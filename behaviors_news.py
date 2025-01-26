import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def render():

    st.title("🌟 Behavior-News Analysis Dashboard")
    st.write(
        "Welcome to the **Behavior-News Analysis Dashboard**! Here, we analyze user behavior "
        "and news data to derive actionable insights for improving news recommendation systems. "
        "Let's dive into the data! 🚀"
    )

    
    behaviors = pd.read_csv("data/behaviors.csv")
    news = pd.read_csv("data/news.csv")


    st.header("📊 User Click History")
    user_clicks = behaviors["History"].str.split(" ", expand=True).stack().value_counts()
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    ax1.bar(user_clicks.index[:20], user_clicks.values[:20], color="skyblue")
    ax1.set_xticklabels(user_clicks.index[:20], rotation=45, ha="right")
    ax1.set_title("Top 20 Clicked Articles")
    ax1.set_ylabel("Click Count")
    st.pyplot(fig1)
    st.write(
        "**Importance:**\n"
        "Analyzing user click history helps uncover the most popular news articles among users. "
        "This information is crucial for understanding user interests and creating better user profiles. "
        "By identifying high-demand news, platforms can promote engaging content to attract more clicks."
    )

    
    st.header("🗂️ News Categories")
    category_counts = news["Category"].value_counts().reset_index()
    category_counts.columns = ["Category", "Count"]
    fig2 = px.pie(
        category_counts,
        names="Category",
        values="Count",
        title="Distribution of News Categories",
        hole=0.4,
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.write(
        "**Importance:**\n"
        "Understanding the distribution of news categories allows platforms to balance the variety of content available. "
        "For example, if users are primarily engaging with sports and technology news, the platform might consider "
        "increasing content in these categories to improve user satisfaction. Moreover, underrepresented categories could "
        "be strategically highlighted to diversify user engagement."
    )


    
    st.header("📂 Top Subcategories")
    subcategory_counts = news["SubCategory"].value_counts().head(10)
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    ax3.bar(subcategory_counts.index, subcategory_counts.values, color="salmon")
    ax3.set_xticklabels(subcategory_counts.index, rotation=45, ha="right")
    ax3.set_title("Top 10 News Subcategories")
    ax3.set_ylabel("Count")
    st.pyplot(fig3)
    st.write(
        "**Importance:**\n"
        "Diving into subcategories allows for a more granular understanding of user interests. "
        "For example, within the 'Technology' category, users might prefer articles about 'AI' or 'Blockchain.' "
        "Highlighting these trends enables better personalization of content for users."
    )


    st.header("✍️ Length of News Titles")
    news["Title Length"] = news["Title"].str.len()
    title_length_distribution = news["Title Length"].value_counts().sort_index()
    st.line_chart(title_length_distribution)
    st.write(
        "**Importance:**\n"
        "The length of news titles can impact user click rates. Shorter titles might be better for quick consumption, "
        "whereas longer, descriptive titles may be more informative. Understanding this distribution can help optimize "
        "title crafting for better engagement."
    )

    st.write("🎉 This dashboard is a comprehensive tool for understanding user behavior and news content trends. By leveraging these insights, platforms can improve their recommendation systems, optimize user engagement, and drive higher satisfaction rates. 🚀")


    st.header("☁️ Word Cloud: Titles and Abstracts")
    st.write("Explore the most frequent words in the news titles and abstracts! 🎨")

    
    title_text = " ".join(news["Title"].dropna())
    abstract_text = " ".join(news["Abstract"].dropna())


    title_wordcloud = WordCloud(width=800, height=400, background_color="white").generate(title_text)
    abstract_wordcloud = WordCloud(width=800, height=400, background_color="white").generate(abstract_text)


    st.subheader("🔤 Word Cloud for Titles")
    fig4, ax4 = plt.subplots(figsize=(12, 6))
    ax4.imshow(title_wordcloud, interpolation="bilinear")
    ax4.axis("off")
    st.pyplot(fig4)

    st.subheader("📖 Word Cloud for Abstracts")
    fig5, ax5 = plt.subplots(figsize=(8, 4))
    ax5.imshow(abstract_wordcloud, interpolation="bilinear")
    ax5.axis("off")
    st.pyplot(fig5)