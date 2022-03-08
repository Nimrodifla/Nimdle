const NSEL = require('nsel');
const fs = require('fs');

const app = NSEL.app;
NSEL.listen();

app.get('/words', (req, res)=>{
    let word_list = String(fs.readFileSync(__dirname + '/words.txt'));
    while (word_list.includes("'"))
        word_list = word_list.replace("'", '"');
    word_list = JSON.parse(word_list);
    res.send({'count': word_list.length, 'words': word_list});
})

app.get('/', (req, res)=>{
    res.sendFile(__dirname + '/index.html');
});