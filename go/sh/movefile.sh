#!/bin/bash

# 引数の数が正しいかチェック
if [ "$#" -ne 2 ]; then
    echo "Usage: movefile.sh <ファイルの相対パス> <新しいディレクトリの相対パス>"
    exit 1
fi

# 第1引数（ファイルの相対パス）と第2引数（ディレクトリの相対パス）を変数に格納
file_path="$1"
dir_path="$2"

# ディレクトリが存在しない場合は作成
if [ ! -d "$dir_path" ]; then
    mkdir -p "$dir_path"
fi

# ファイルを指定のディレクトリにコピー
cp "$file_path" "$dir_path/"

echo "ファイル '$file_path' をディレクトリ '$dir_path' にコピーしました。"
