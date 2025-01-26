import pandas as pd

def preprocess_tsv_to_csv(input_file, output_file, column_names):
    data = pd.read_csv(input_file, sep='\t', names=column_names, quoting=3, encoding='utf-8')
    data.to_csv(output_file, index=False)
    print(f"{input_file} has been converted to {output_file}")

if __name__ == "__main__":
    preprocess_tsv_to_csv("MINDsmall_train/behaviors.tsv", "data/behaviors.csv", 
                          ["Impression ID", "User ID", "Time", "History", "Impressions"])
    preprocess_tsv_to_csv("MINDsmall_train/news.tsv", "data/news.csv", 
                          ["News ID", "Category", "SubCategory", "Title", "Abstract", "URL", "Title Entities", "Abstract Entities"])
    preprocess_tsv_to_csv("MINDsmall_train/entity_embedding.vec", "data/entity_embedding.csv", 
                          ["Entity ID"] + [f"Dim_{i}" for i in range(1, 101)])
    preprocess_tsv_to_csv("MINDsmall_train/relation_embedding.vec", "data/relation_embedding.csv", 
                          ["Relation ID"] + [f"Dim_{i}" for i in range(1, 101)])
