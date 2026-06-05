import GigaChat from 'gigachat';

const giga = new GigaChat({
    credentials: process.env.GIGACHAT_API_KEY,
    scope: 'GIGACHAT_API_PERS',
});

giga.chat({
    messages: [
    {
        role: 'system',
        content: 'рассмотреть решение с точки зрения математика, поэта, программиста'
    },
    {
        role: 'user',
        content: 'найти площадь круга'
    }
    ],
    "stream": false,
    "max_tokens": 512,
    "repetition_penalty": 1,
    "update_interval": 0
})

.then((resp) => {
    console.log(resp.choices[0]?.message.content);
});

