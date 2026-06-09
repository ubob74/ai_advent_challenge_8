import os
import sys
import json
import re
from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

FILENAME="/tmp/gigachat_history.json"

json_data = []

def init_gigachat():
    return GigaChat(
        credentials=os.getenv('GIGACHAT_API_KEY'),
        model='GigaChat-2',
        scope="GIGACHAT_API_PERS"
    )

def gigachat_restart_history(giga):
    if os.path.isfile(FILENAME):
        with open(FILENAME, "r", encoding='utf-8') as file:
            json_data = json.load(file)
            print("Предыдущие запросы:")
            for line in json_data:
                data = json.loads(line)
                request = data["request"]
                if len(request) == 0:
                    continue
                print(request)
                payload = Chat(
                    messages=[
                        Messages(
                            role=MessagesRole.SYSTEM,
                            content="сохранять историю запросов",
                        ),
                        Messages(
                            role=MessagesRole.USER,
                            content=request,
                        )
                    ],
                )

                result = giga.tokens_count(input_=[request])
                print(result)

                response = giga.chat(payload)
                print(response.choices[0].message)

                show_usage(response.usage)

    file = open(FILENAME, "a+", encoding='utf-8')
    return file

def show_usage(usage):
    print(f"Токены запроса: {usage.prompt_tokens}")
    print(f"Токены для генерации ответа: {usage.completion_tokens}")
    print(f"Токены для тарификации: {usage.total_tokens}")

def main():

    load_dotenv()

    giga = init_gigachat()

    file = gigachat_restart_history(giga)

    try:
        while 1:
            request = input("Введите запрос: ")

            if len(request) == 0:
                continue

            result = giga.tokens_count(input_=[request])
            print(result)

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

            show_usage(response.usage)

            gigachat_info = {
                "request" : request,
            }

            json_data.append(json.dumps(gigachat_info))

    except KeyboardInterrupt:
        if len(json_data) > 0:
            json.dump(json_data, file, indent=4)
        sys.exit(0)

if __name__ == "__main__":
    main()

