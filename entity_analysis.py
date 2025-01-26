import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from mpl_toolkits.mplot3d import Axes3D
import os



def render():

    st.title("🌟 Entity Analysis Dashboard 🌟")
    st.write("""
    # 📊 Explore Entity Embeddings with Ease!
    Entity embeddings are dense vector representations of categorical variables, learned using deep learning models.
    These embeddings help capture semantic similarities between entities. Let's dive into the world of entity embeddings!
    """)

    
    file_path = "data/entity_embedding.csv"
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        return
    
    entities = pd.read_csv(file_path)

    
    entities = entities.dropna(axis=1, how="all")

    
    imputer = SimpleImputer(strategy="mean")
    entities.iloc[:, 1:] = imputer.fit_transform(entities.iloc[:, 1:])


    st.write("### 🔍 Sample of Entity Embeddings")
    st.dataframe(entities.head())

    
    st.write("### 📈 Histogram Analysis")
    user_input = st.text_input("Select dimensions to analyze (e.g., `1, 2, 3`):", "1, 2, 3")

    try:
        selected_dims = [int(dim.strip()) for dim in user_input.split(",") if dim.strip().isdigit()]
    except ValueError:
        st.error("Please enter valid numeric dimensions.")
        return

    for dim in selected_dims:
        col_name = f"Dim_{dim}"
        if col_name in entities.columns:
            st.write(f"#### 📊 Histogram for Dimension {dim} 🎯")
            fig, ax = plt.subplots()
            ax.hist(entities[col_name], bins=20, color="skyblue", edgecolor="black")
            ax.set_title(f"Distribution of Dimension {dim}")
            ax.set_xlabel("Value")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
            st.write("""
            **🧐 Why this matters:**
            - Histograms reveal the distribution of values, helping identify patterns like skewness or outliers.
            """)

    
    st.write("### 🌌 What is PCA?")
    st.write("""
    Principal Component Analysis (PCA) reduces high-dimensional data into lower dimensions while retaining the most variance. Let's explore it step-by-step!
    """)

    
    st.write("### 🟢 Step-by-Step 2D PCA Explanation")
    standardized_data = (entities.iloc[:, 1:] - entities.iloc[:, 1:].mean()) / entities.iloc[:, 1:].std()
    standardized_data = standardized_data.fillna(0)

    
    pca_2d = PCA(n_components=2)
    try:
        pca_result_2d = pca_2d.fit_transform(standardized_data)
        st.write("#### 2D PCA Result")
        st.dataframe(pd.DataFrame(pca_result_2d, columns=["PCA_1", "PCA_2"]).head())

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.scatter(pca_result_2d[:, 0], pca_result_2d[:, 1], alpha=0.6, color="purple")
        ax.set_title("2D PCA Scatter Plot")
        ax.set_xlabel("PCA Component 1")
        ax.set_ylabel("PCA Component 2")
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error performing 2D PCA: {e}")

    
    st.write("### 🔵 Step-by-Step 3D PCA Explanation")
    pca_3d = PCA(n_components=3)
    try:
        pca_result_3d = pca_3d.fit_transform(standardized_data)
        st.write("### 3D PCA Result")
        st.dataframe(pd.DataFrame(pca_result_3d, columns=["PCA_1", "PCA_2", "PCA_3"]).head())

        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(pca_result_3d[:, 0], pca_result_3d[:, 1], pca_result_3d[:, 2], alpha=0.6, color="teal")
        ax.set_title("3D PCA Scatter Plot")
        ax.set_xlabel("PCA Component 1")
        ax.set_ylabel("PCA Component 2")
        ax.set_zlabel("PCA Component 3")
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error performing 3D PCA: {e}")



    st.write("### 📦 Box Plot for Dimensions")
    summary = entities.describe().T[['min', '25%', '50%', '75%', 'max']]
    st.subheader("📌 Five Number Summary")
    st.dataframe(summary)

        

    selected_dims_boxplot = st.multiselect(
        "Select dimensions for box plot visualization:",
        entities.columns[1:],
        default=entities.columns[1:5].tolist()  
    )


    if selected_dims_boxplot:
        fig, ax = plt.subplots(figsize=(8, 4))
        boxplot_data = entities[selected_dims_boxplot]
        boxplot_data.boxplot(ax=ax)
        ax.set_title("Box Plot of Selected Dimensions")
        ax.set_ylabel("Values")
        ax.set_xlabel("Dimensions")

       
        y_min = boxplot_data.min().min()  
        y_max = boxplot_data.max().max()  
        ax.set_ylim(y_min - 0.1 * abs(y_min), y_max + 0.1 * abs(y_max))  
        ax.yaxis.set_major_locator(plt.MaxNLocator(nbins=10))  

        st.pyplot(fig)
    else:
        st.write("Select at least one dimension to view the box plot.")


    st.write("""
    **📌 Why This Matters for the MIND Dataset:**
    - **Central Tendencies**: Measures like the mean and median help identify the "typical" value for each embedding dimension. For example:
      - An unusually high mean might indicate a bias in the dataset toward certain entities (e.g., more news articles from a specific category).
      - A median close to the extremes (min/max) could signal skewness in the data.

    - **Variability**: Standard deviation and range reveal how spread out the embedding values are. In the context of the MIND dataset:
      - High variability in a dimension could mean it's capturing diverse characteristics of the entities.
      - Low variability might suggest redundancy or lack of meaningful differences in that dimension.

    - **Potential Anomalies**:
      - Outliers detected through min/max values or by inspecting skewness can indicate unusual entities or errors in the embedding process.
      - Such anomalies could be critical for debugging the embedding generation pipeline or uncovering unique entity relationships.

    - **Feature Importance**: 
      - Dimensions with high variability often contribute more to entity differentiation, making them important for downstream tasks like clustering or classification.
      - Conversely, near-zero variability might indicate dimensions that can be dropped to simplify models without losing information.

    - **Insights for Recommendation Systems**: 
      - Understanding how dimensions relate to the dataset can help refine the recommendation algorithms. For example:
        - If certain dimensions strongly correlate with user engagement metrics, they might be emphasized during training.
        - Detecting clusters or gaps in the data (e.g., users with similar embeddings) could suggest personalization opportunities.

    - **Dimension Interpretability**: 
      - Analyzing statistical patterns in dimensions might hint at their semantic meaning. For instance, dimensions with a skewed distribution might be associated with rare categories or specific user behaviors.
    """)
