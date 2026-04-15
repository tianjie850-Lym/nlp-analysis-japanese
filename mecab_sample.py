import MeCab

mecab = MeCab.Tagger()
text = "私は日本語を勉強しています。"
result = mecab.parse(text)

print(result)
