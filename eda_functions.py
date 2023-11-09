import pandas as pd

def load_data(seq_path='data/sequences.txt', labels_path='data/labels.txt'):
    # Read txt files from data directory, default path is given
    df_seqs = pd.read_csv(seq_path, header=None)
    df_labels = pd.read_csv(labels_path, header=None)
    return df_seqs, df_labels

def check_is_dna(dna_string):
    # Check if all nucleotides in the input dna_string are present in the DNA alphabet
    DNA_nucleotides = set('ACTG')
    return all(base in DNA_nucleotides for base in set(dna_string))

def drop_non_dna(df_seqs):
    # Check which strings are DNA
    dna_strings = df_seqs[0].apply(check_is_dna)
    # If all strings are DNA then we return the same df
    if sum(dna_strings)==len(df_seqs):
        return df_seqs
    # If not we drop non DNA strings and return the filtered df
    else:
        return df_seqs.drop(dna_strings[dna_strings==False].index,axis=0)

