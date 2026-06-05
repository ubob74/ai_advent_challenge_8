import GigaChat from 'gigachat';

const giga = new GigaChat({
    credentials: process.env.GIGACHAT_API_KEY,
    scope: 'GIGACHAT_API_PERS',
});

giga.chat({
    messages: [
    {
        role: 'user',
        content: 'промпт для написания программы вычисления площад круга на языке С'
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

