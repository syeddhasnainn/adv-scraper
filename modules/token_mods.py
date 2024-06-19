import html2text
import tiktoken



def tokenGenerator(text=None,encode_type='gpt-3.5-turbo-0125'):
    encoder = tiktoken.encoding_for_model(encode_type)
    tokens = encoder.encode(html2text.html2text(text))
    return tokens
