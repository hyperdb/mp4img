# mp4img

mp4 ファイルから指定秒数ごとにフレームを静止画として保存するツールです。開発時に uv コマンドを使用しているため、ドキュメント上 uv が前提のようになっていますが、Python スクリプトとしても実行可能です。

## 使い方

```bash
$ uv run main.py <inFile> <outDir> [--seconds <秒数>]
```

## 環境構築

```bash
$ uv init  --app
$ uv add --link-mode=copy ruff
$ uv add --link-mode=copy opencv-python
```

## ライセンス

MIT License
