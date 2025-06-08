import os

def convert_conll4_to_bio2(input_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(input_path, encoding='utf-8') as fin, \
         open(output_path, 'w', encoding='utf-8') as fout:

        for line in fin:
            line = line.strip()
            if not line or line.startswith('-DOCSTART-'):
                fout.write('\n')  # sentence boundary
                continue

            parts = line.split()
            if len(parts) >= 4:
                token, ner_tag = parts[0], parts[-1]
                fout.write(f"{token} {ner_tag}\n")
            else:
                print(f"Skipping malformed line: {line}")


if __name__ == "__main__":
    # Adjust filenames if needed
    input_dir = "Eng_Datasets"
    output_dir = "Eng_Datasets/train_bio"

    files = ["train.txt", "valid.txt", "test.txt"]

    for fname in files:
        in_path = os.path.join(input_dir, fname)
        out_path = os.path.join(output_dir, fname.replace(".txt", ".bio"))
        print(f"Converting {in_path} → {out_path}")
        convert_conll4_to_bio2(in_path, out_path)

    print(" All English files converted to BIO2 format.")
