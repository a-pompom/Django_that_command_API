# Djangoのインストール
FROM ubuntu:18.04

RUN apt update && \
         apt install -y locales curl python3-distutils python-psycopg2 language-pack-ja && \
         # pipの実体を取得し、ファイルに保存
         curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
         # ファイルからpipをインストール 
         python3 get-pip.py  && \
         pip install -U pip && \
         # pytestで日本語メソッド名が扱えるようロケールを設定
         update-locale LANG=ja_JP.UTF-8

# コマンドのエントリポイントを設定
WORKDIR /code

# ローカルのrequirements.txtを追加
ADD requirements.txt /code

# requirements.txtをもとにpipでDjangoをインストール
RUN pip install -r requirements.txt
