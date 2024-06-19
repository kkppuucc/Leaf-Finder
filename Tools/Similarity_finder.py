import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def find_similar(hist_count, connection, cursor):
    # Retrieve histogram data from the database
    cursor.execute("SELECT fileName, hist0, hist1, hist2, hist3, hist4, hist5, hist6, hist7 FROM leaf2files")
    rows = cursor.fetchall()
    # Compare the new image histogram with each stored histogram
    similarities = []

    for row in rows:
        file_name = row[0]
        hist_values = row[1:9]

        similarity = compute_similarity(hist_count, hist_values)
        similarities.append((file_name, similarity))

    # Sort similarities in descending order
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Print the top 10 most similar images
    print("\nTop 10 most similar images:")
    for i, (file_name, similarity) in enumerate(similarities[:10]):
        print(f"{i+1}. Similarity with {file_name}: {similarity:.3f}")


def compute_similarity(hist1, hist2, method='cosine'):
    """
    Computes the similarity between two histogram vectors.

    Parameters:
    - hist1: First histogram vector.
    - hist2: Second histogram vector.
    - method: The method used for similarity computation ('cosine', 'euclidean').

    Returns:
    - similarity: A similarity score between 0 and 1 (for cosine similarity).
    """
    if method == 'cosine':
        # Reshape the histograms to 2D arrays for cosine_similarity function
        hist1 = np.array(hist1).reshape(1, -1)
        hist2 = np.array(hist2).reshape(1, -1)

        # Compute cosine similarity
        similarity = cosine_similarity(hist1, hist2)[0][0]
    elif method == 'euclidean':
        # Compute Euclidean distance and convert it to similarity
        distance = np.linalg.norm(np.array(hist1) - np.array(hist2))
        similarity = 1 / (1 + distance)  # Convert distance to similarity
    else:
        raise ValueError("Unsupported method. Use 'cosine' or 'euclidean'.")

    return similarity
