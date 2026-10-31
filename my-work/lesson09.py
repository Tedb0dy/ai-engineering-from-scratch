import time

from datasets import load_dataset

# GLUE is a collection of tasks; "mrpc" picks the paraphrase task
dataset = load_dataset("nyu-mll/glue", "mrpc")
print(dataset)

# First 5 training examples
first_five = dataset["train"][:5]
print(first_five)

# Easier to read: one pair per block
for s1, s2, label in zip(
    first_five["sentence1"], first_five["sentence2"], first_five["label"]
):
    print(f"\nlabel={label}")
    print(f"  1: {s1}")
    print(f"  2: {s2}")


# streaming=True: don't download, read rows over the network as you go
stream = load_dataset("allenai/c4", "en", split="train", streaming=True)

count = 0
start = time.time()
for example in stream:
    count += 1
    if time.time() - start > 10:
        break

print(f"\nStreamed {count:,} examples in 10 seconds")
print(f"Last example starts: {example['text'][:100]}...")
