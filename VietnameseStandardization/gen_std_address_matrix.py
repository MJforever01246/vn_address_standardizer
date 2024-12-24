from . import Parameters
from . import Utils
import json
import torch

std_add = json.load(
    open(Parameters.NORM_ADDS_FILE_RAW, "r", encoding="utf8")
)

def gen_matrix(embedding_model, batch_size=100):
    accent_addresses, unaccent_addresses = [], []
    for i in std_add:
        add = std_add[i]
        str_add = ' '.join([add[i] for i in add])
        unac_str_add = Utils.remove_accent(str_add)
        accent_addresses.append(str_add)
        unaccent_addresses.append(unac_str_add)
    
    print(f"Total addresses to encode: {len(accent_addresses)}")

    def encode_in_batches(addresses, batch_size):
        embeddings = []
        for i in range(0, len(addresses), batch_size):
            batch = addresses[i:i + batch_size]
            print(f"Encoding batch {i // batch_size + 1}/{(len(addresses) + batch_size - 1) // batch_size}")
            batch_embeddings = embedding_model.encode(batch)
            embeddings.append(torch.tensor(batch_embeddings))
        return torch.cat(embeddings, dim=0)

    print("Encoding accent addresses...")
    accent_matrix = encode_in_batches(accent_addresses, batch_size)
    print("Encoding non-accent addresses...")
    noaccent_matrix = encode_in_batches(unaccent_addresses, batch_size)

    embedding = {
        'accent_matrix': accent_matrix,
        'noaccent_matrix': noaccent_matrix
    }

    print("Saving embeddings...")
    torch.save(embedding, Parameters.STD_EMBEDDING_FILE_ALL_1)
    print("Done")

# Example usage:
# gen_matrix(embedding_model, batch_size=100)