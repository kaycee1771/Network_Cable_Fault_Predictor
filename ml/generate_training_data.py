import pandas as pd
import random

def generate_sample():
    in_octets = random.randint(50000, 1000000)
    out_octets = random.randint(50000, 1000000)
    in_errors = random.randint(0, 5)
    out_errors = random.randint(0, 5)
    
    # If errors > 3 or octet drop vs previous is large, it's degrading
    is_degrading = 1 if (in_errors + out_errors > 5 or random.random() < 0.2) else 0
    
    return {
        "in_octets": in_octets,
        "out_octets": out_octets,
        "in_errors": in_errors,
        "out_errors": out_errors,
        "speed": 1000000000,
        "label": is_degrading
    }

def generate_dataset(n=1000):
    return pd.DataFrame([generate_sample() for _ in range(n)])

if __name__ == "__main__":
    df = generate_dataset()
    df.to_csv("data/cable_fault_dataset.csv", index=False)
    print("✅ Generated dataset: data/cable_fault_dataset.csv")
