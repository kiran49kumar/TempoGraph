import pandas as pd
import os

RAW_DIR = "data/raw/lastfm-dataset-1K"
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

def preprocess_profiles():
    print("Loading user profiles...")
    profiles = pd.read_csv(
        os.path.join(RAW_DIR, "userid-profile.tsv"),
        sep="\t"
    )
    print(f"Profiles: {len(profiles)} users")
    profiles.to_csv(os.path.join(PROCESSED_DIR, "profiles.csv"), index=False)
    print("Processed profiles saved to data/processed/profiles.csv")


def preprocess_listening():
    print("Loading listening history in chunks...")
    LISTEN_FILE = "data/raw/lastfm-dataset-1K/userid-timestamp-artid-artname-traid-traname.tsv"
    OUTPUT_FILE = "data/processed/listening.csv"

    col_names = ["userid", "timestamp", "artid", "artname", "traid", "traname"]

    chunks = []
    for chunk in pd.read_csv(
        LISTEN_FILE,
        sep="\t",
        header=None,
        names=col_names,
        on_bad_lines="skip",
        quoting=3,             # 🚑 QUOTE_NONE (treat quotes as normal chars)
        engine="python",
        chunksize=100000,
    ):
        # Drop rows with missing timestamps
        chunk = chunk.dropna(subset=["timestamp"])

        # Convert timestamp column to datetime
        chunk["timestamp"] = pd.to_datetime(
            chunk["timestamp"], errors="coerce"
        )

        # Drop rows where conversion failed
        chunk = chunk.dropna(subset=["timestamp"])

        chunks.append(chunk)

    listens = pd.concat(chunks, ignore_index=True)
    print(f"Processed listening history: {len(listens)} rows")
    listens.to_csv(OUTPUT_FILE, index=False)
    print(f"Processed listening history saved to {OUTPUT_FILE}")



if __name__ == "__main__":
    preprocess_profiles()
    preprocess_listening()



