import os

from slack_bolt import App
from openai import OpenAI

app = App(
    signing_secret=os.environ["SLACK_SIGNING_SECRET"],
    token=os.environ["SLACK_BOT_TOKEN"]
)
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


@app.command("/summarize")
def summarize(ack, respond, command):
    ack()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    respond(completion.choices[0].message.content)


if __name__ == "__main__":
    app.start(port=3000)
