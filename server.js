const NSEL = require('nsel');
const fs = require('fs');

const app = NSEL.app;
NSEL.listen();

const words = parseWords(__dirname + '/words.txt');
console.log(words.length + " words");

function parseWords(path) {
    let word_list = String(fs.readFileSync(path));
    while (word_list.includes("'"))
        word_list = word_list.replace("'", '"');
    word_list = JSON.parse(word_list);
    return word_list;
}

app.get('/words', (req, res)=>{
    res.send({'count': words.length, 'words': words});
})

app.get('/', (req, res)=>{
    res.sendFile(__dirname + '/index.html');
});