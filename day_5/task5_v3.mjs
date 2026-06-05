import GigaChat from 'gigachat';

const giga = new GigaChat({
    credentials: process.env.GIGACHAT_API_KEY,
    scope: 'GIGACHAT_API_PERS',
    model: 'GigaChat-2-Max'
});

giga.chat({
    messages: [
    {
        role: 'user',
        content: 'вычислить скорость падения медного шара диаметром 1 метр с высоты 1 метр без учета сопротивления воздуха и вернуть количестов затраченных токенов для этого запроса'
    }
    ],
    "stream": false,
    "max_tokens": 1024,
    "repetition_penalty": 1,
    "update_interval": 0,
})

.then((resp) => {
    console.log(resp.choices[0]);
});

