# wordcloudの画像をpythonで作成するレポジトリ
## 実行方法
### ビルド
```
docker-compose up -d --build
```
### コンテナに入る
```
docker-compose exec python3 /bin/bash
```

### 実行
`opt/speech.txt`に可視化対象の文字列を保存後
```
python3 opt/sample.py
```
を実行。

### 結果確認
`opt/wordcloud.png`を確認