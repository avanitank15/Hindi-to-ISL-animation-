import ctranslate2
import sentencepiece as spm

def mtrans(src_lang, tgt_lang, src_text):
    """
    Translates a list of sentences from src_lang to tgt_lang
    using an M2M100 model converted to CTranslate2 format.
    
    Parameters:
    - src_lang: source language code (e.g. 'en')
    - tgt_lang: target language code (e.g. 'fr')
    - src_text: list of source sentences to translate
    """

    # Output file where translations will be saved
    target_file_path = "trans.mt"
    
    # Path to the CTranslate2 model directory
    ct_model_path = "hemant/m2m100_ct2_12b/"
    
    # Path to the SentencePiece model file
    sp_model_path = "hemant/m2m100_ct2_12b/sentencepiece.model"
    
    # Language tokens required by M2M100
    # Example: "__en__", "__fr__"
    src_prefix = "__" + src_lang + "__"
    tgt_prefix = "__" + tgt_lang + "__"
    
    # Device selection: "cpu" or "cuda" (GPU)
    device = "cpu"
    
    # Beam size controls translation quality vs speed
    beam_size = 5
    
    # Load the SentencePiece tokenizer
    sp = spm.SentencePieceProcessor()
    sp.load(sp_model_path)
    
    # Input sentences (expected to be a list of strings)
    lines = src_text
    
    # Clean up sentences (remove leading/trailing spaces)
    source_sents = [line.strip() for line in lines]
    
    # Target prefix must be provided per sentence
    # Shape: [[__fr__], [__fr__], ...]
    target_prefix = [[tgt_prefix]] * len(source_sents)
    
    # Tokenize (subword) the source sentences
    # Output is a list of token lists
    source_sents_subworded = sp.encode(source_sents, out_type=str)
    
    # Prepend source language token to each sentence
    source_sents_subworded = [[src_prefix] + sent for sent in source_sents_subworded]
    
    # Debug: print first tokenized sentence
    print("First sentence:", source_sents_subworded[0])
    
    # Load the CTranslate2 translator
    translator = ctranslate2.Translator(ct_model_path, device=device)
    
    # Translate sentences in batches
    translations = translator.translate_batch(
        source_sents_subworded,
        batch_type="tokens",        # batching by token count
        max_batch_size=2024,        # maximum tokens per batch
        beam_size=beam_size,
        target_prefix=target_prefix
    )
    
    # Extract token outputs from best hypothesis of each translation
    translations = [translation[0]['tokens'] for translation in translations]
    
    # Debug: print raw translated tokens
    print(translations)
    
    # Convert subword tokens back to normal text
    translations_desubword = sp.decode(translations)
    
    # Remove target language prefix from decoded text
    translations_desubword = [sent[len(tgt_prefix):] for sent in translations_desubword]
    
    # Debug: print first final translation
    print("First translation:", translations_desubword[0])
    
    # Save translations to a file (one sentence per line)
    with open(target_file_path, "w+", encoding="utf-8") as target:
        for line in translations_desubword:
            target.write(line.strip() + "\n")
            
    # Append source and translation pairs to a master file
    with open("master.txt", "a+", encoding="utf-8") as target:
        cnt = 0
        for line in translations_desubword:
            target.write(src_text[cnt] + "\t")  # source sentence
            target.write(line.strip() + "\n")   # translated sentence
            cnt = cnt + 1
    
    # Return the translated sentences as a list
    return translations_desubword



# import ctranslate2
# import sentencepiece as spm

# def mtrans(src_lang, tgt_lang, src_text):
#     # Initialize file paths
#     #source_file_path = src_file
#     target_file_path = "trans.mt"
    
    
#     # Set paths to the CTranslate2 and SentencePiece models
#     ct_model_path = "hemant/m2m100_ct2_12b/"
#     sp_model_path = "hemant/m2m100_ct2_12b/sentencepiece.model"
    
    
#     # Set language prefixes of the source and target
#     src_prefix = "__" + src_lang + "__"
#     tgt_prefix = "__" + tgt_lang + "__"
    
    
#     # Set the device and beam size
#     device = "cpu"  # "cpu" or "cuda" for GPU
#     beam_size = 5
    
    
#     # Load the source SentecePiece model
#     sp = spm.SentencePieceProcessor()
#     sp.load(sp_model_path)
    
    
#     # list of sentences to be translated
#     lines = src_text
    
    
#     source_sents = [line.strip() for line in lines]
#     target_prefix = [[tgt_prefix]] * len(source_sents)
    
    
#     # Subword the source sentences
#     source_sents_subworded = sp.encode(source_sents, out_type=str)
#     source_sents_subworded = [[src_prefix] + sent for sent in source_sents_subworded]
#     print("First sentence:", source_sents_subworded[0])
    
    
#     # Translate the source sentences
#     translator = ctranslate2.Translator(ct_model_path, device=device)
#     translations = translator.translate_batch(source_sents_subworded, batch_type="tokens", max_batch_size=2024, beam_size=beam_size, target_prefix=target_prefix)
#     translations = [translation[0]['tokens'] for translation in translations]
#     print(translations)
    
#     # Desubword the target sentences
#     translations_desubword = sp.decode(translations)
#     translations_desubword = [sent[len(tgt_prefix):] for sent in translations_desubword]
#     print("First translation:", translations_desubword[0])
    
    
#     # Save the translations to the a file
#     with open(target_file_path, "w+", encoding="utf-8") as target:
#         for line in translations_desubword:
#             target.write(line.strip() + "\n")
            
#     # Save the translations to the master file
#     with open("master.txt", "a+", encoding="utf-8") as target:
#         cnt=0
#         for line in translations_desubword:
#             target.write(src_text[cnt] + "\t")
#             target.write(line.strip() + "\n")
#             cnt = cnt + 1
            
    
#     # print("Done! Target file saved at:", target_file_path)
    
#     return translations_desubword

