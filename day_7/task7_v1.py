import os
import sys
import json
from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

FILENAME="/tmp/gigachat_history.json"

def main():

    load_dotenv()

    giga = GigaChat(
        credentials=os.getenv('GIGACHAT_API_KEY'),
        model='GigaChat-2',
        scope="GIGACHAT_API_PERS"
    )

    json_data = []

    if os.path.isfile(FILENAME):
        with open(FILENAME, "r", encoding='utf-8') as file:
            json_data = json.load(file)
            print("Предыдущие запросы:")
            for line in json_data:
                data = json.loads(line)
                request = data["request"]
                print(request)
                payload = Chat(
                    messages=[
                        Messages(
                            role=MessagesRole.SYSTEM,
                            content="не присылать ответ",
                        ),
                        Messages(
                            role=MessagesRole.USER,
                            content=request,
                        )
                    ],
                )

                giga.chat(payload)

        file.close()

    file = open(FILENAME, "w", encoding='utf-8')

    try:
        while 1:
            request = input("Введите запрос: ")

            payload = Chat(
                messages=[
                    Messages(
                        role=MessagesRole.USER,
                        content=request,
                    )
                ],
            )

            response = giga.chat(payload)
            print(response.choices[0].message)

            gigachat_info = {
                "request" : request,
            }

            json_data.append(json.dumps(gigachat_info))

    except KeyboardInterrupt:
        json.dump(json_data, file, indent=4)
        sys.exit(0)

if __name__ == "__main__":
    main()

