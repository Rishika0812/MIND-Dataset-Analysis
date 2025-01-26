import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def render():
    
    st.title("📊 Relation Embedding Dashboard")
    st.markdown("Analyze and visualize relation embeddings in a fun and interactive way! 🚀")

    
    csv_file_path = "data/relation_embedding.csv"
    try:
        
        st.header("📂 Data Overview")
        df = pd.read_csv(csv_file_path)
        st.write("**Preview of the Data:**")
        st.dataframe(df.head())

     
        st.header("📊 Exploratory Data Analysis")
        
        
        st.subheader("📌 Five Number Summary")
        summary = df.describe().T[['min', '25%', '50%', '75%', 'max']]
        st.write("**Five Number Summary:**")
        st.dataframe(summary)

        
        st.subheader("🔍 Importance of the Analysis")
        st.markdown("""
        This analysis provides insights into the **distribution** and **correlation** of embedding dimensions. By understanding these embeddings, you can:
        1. **Identify patterns**: Detect how different dimensions relate to each other and the distribution of values across them.
        2. **Understand spread**: The Five Number Summary helps to quickly grasp the spread, central tendency, and variability of the data.
        3. **Anomaly detection**: Outliers in the boxplot can indicate anomalies or unique data points that may need special attention.
        4. **Improve clustering models**: Understanding the relationships between dimensions is crucial for clustering or grouping similar data points.
        5. **Dimensionality Reduction**: Analyzing the relationship between embedding dimensions can help in techniques like PCA for reducing dimensionality while preserving information.
        """)
        
        
        st.subheader("📊 Boxplot of Selected Embedding Dimension")
        dimension_list = df.columns[1:]  
        selected_dimension = st.selectbox("Select Embedding Dimension for Boxplot:", dimension_list)

    
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.boxplot(y=df[selected_dimension], ax=ax, color="skyblue")
        ax.set_title(f"Boxplot of Embedding Dimension: {selected_dimension}")
        ax.set_ylabel("Embedding Value")
        st.pyplot(fig)

        

    except FileNotFoundError:
        st.error(f"❌ File not found at path: {csv_file_path}. Please check the file location and try again.")


