
const NSEL = require('./NSEL.js');

// NSEL INIT
const [app, db] = NSEL.quick('host', 'user', 'password', 'db');

// End Points
app.get('/', (req, res)=>{
    db.set(['users', 'user1', 'password'], '1234'); // set data to db
    let password = db.get(['users', 'user1', 'password']); // get data from db
    res.send(password); // send response
});