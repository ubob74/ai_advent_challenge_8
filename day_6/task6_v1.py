import os
import sys
from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

def main():

    load_dotenv()

    giga = GigaChat(
        credentials=os.getenv('GIGACHAT_API_KEY'),
        model='GigaChat-2',
        scope="GIGACHAT_API_PERS"
    )

    try:
        print("Ну что, начнем?")
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

    except KeyboardInterrupt:
        print("Вы к нам почаще заходите, без вас потом так хорошо")
        sys.exit(0)

if __name__ == "__main__":
    main()

