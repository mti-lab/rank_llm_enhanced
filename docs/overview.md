## 環境構築手順
.env.localを配置してOPENAI_ API_KEYを入れる
```
python -m venv .venv
source .venv/bin/activate
pip install -e '.[pyserini]'
```
uvだと、環境構築うまくいかなかったので、愚直に仮想環境内でpip installします

javaのバージョンが合わない場合
```
sudo update-alternatives --config java
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
```
