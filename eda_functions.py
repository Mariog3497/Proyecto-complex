import pandas as pd

def load_data(seq_path='data/sequences.txt', labels_path='data/labels.txt'):
    df_seqs = pd.read_csv(seq_path, header=None)
    df_labels = pd.read_csv(labels_path, header=None)
    return df_seqs, df_labels