from tokenizers import ByteLevelBPETokenizer

tokenizer = ByteLevelBPETokenizer.from_file(
    "./vocabularies/codet5-vocab.json",
    "./vocabularies/codet5-merges.txt"
)
tokenizer.add_special_tokens([
    "<pad>",
    "<s>",
    "</s>",
    "<unk>",
    "<mask>"
])

print(
    tokenizer.encode("<s> hello <unk> Don't you love 🤗 Transformers <mask> yes . </s>").tokens
)
