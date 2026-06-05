import GigaChat from 'gigachat';

const giga = new GigaChat({
    credentials: process.env.GIGACHAT_API_KEY,
    scope: 'GIGACHAT_API_PERS',
});

giga.chat({
    messages: [
    {
        role: 'system',
        content: 'вывести только финальный результат'
    },
    {
        role: 'user',
        content: 'вычислить потенциальную энергию медного шара диаметром 1 метр, поднятого на высоту 1 метр'
    }
    ],
    "stream": false,
    "max_tokens": 512,
    "repetition_penalty": 1,
    "update_interval": 0,
    "temperature": 1.2
})

.then((resp) => {
    console.log(resp.choices[0]?.message.content);
});

