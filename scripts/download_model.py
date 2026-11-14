"""Download the exact public model revision used in the recorded experiment."""
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
REVISION = '1110a243fdf4706b3f48f1d95db1a4f5529b4d41'
FILES = ['1_Pooling/config.json', 'README.md', 'config.json', 'config_sentence_transformers.json',
         'model.safetensors', 'modules.json', 'sentence_bert_config.json', 'special_tokens_map.json',
         'tokenizer.json', 'tokenizer_config.json', 'vocab.txt']


def main():
    root = ROOT / 'local_models/all-MiniLM-L6-v2'
    for name in FILES:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            temporary = path.with_suffix(path.suffix + '.part')
            urllib.request.urlretrieve(f'https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/{REVISION}/{name}', temporary)
            temporary.replace(path)
        print(name, path.stat().st_size)
    (root / 'download_revision.txt').write_text(REVISION + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
