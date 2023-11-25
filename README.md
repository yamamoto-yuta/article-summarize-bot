# article-summarize-bot

記事を要約してくれる Slack App

次の記事の実装を試してみる予定:

> [技術 blog のリンクを投げたら ChatGPT が要約して、いい感じに整形してチャンネル投稿してくれる bot を社内 Slack に生やしたら捗った話](https://zenn.dev/sigmai_tech/articles/368533f22feb7f)

## 初回環境構築

1. `git clone`
1. `.env.sample` を複製して `.env` を作成
1. `docker-compose build`

## 開発手順

1. ngrok を起動

```
$ ngrok http 8000
```

2. ngrok の URL を Slack App の設定へ反映

3. Slack App を起動

```
$ docker-compose up -d
$ docker exec -it <CONTAINER_ID> bash
[IN CONTAINER]# uvicorn main:app --reload --host 0.0.0.0
```
