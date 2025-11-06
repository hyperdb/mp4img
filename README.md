# mp4img

mp4 ファイルから指定秒数ごとにフレームを静止画として保存するツールです。

## 使い方

```bash
$ uv run main.py <inFile> <outDir> [--seconds <秒数l>]
```

## 環境構築

```bash
$ uv init  --app
$ uv add --link-mode=copy ruff
$ uv add --link-mode=copy opencv-python
```

## ライセンス

MIT License
