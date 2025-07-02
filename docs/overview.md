## 環境構築手順
.env.localを配置してOPENAI_ API_KEYを入れる
```
uv sync
source .venv/bin/activate
pip install -e '.[pyserini]'
```
uvだと、環境構築うまくいかなかったので、愚直に仮想環境内でpip installします
