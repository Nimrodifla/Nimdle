# NSEL
Make nodejs express server & json structured database in 1 line!
```javascript
const NSEL = require('nsel');

// NSEL INIT
const [app, db] = NSEL.quick('host', 'user', 'password', 'db');

// End Points
app.get('/', (req, res)=>{
    db.shieldSetter(['users', 'user1', 'password'], '1234'); // set data from db
    let password = db.shieldGetter(['users', 'user1', 'password']); // get data from db
    res.send(password); // send response
});
```

## Database
NSEL.DB.jdb is a json object, that can be saved in your mysql db with the:
```javascript
db.saveDB();
```
command.

but a quicker way to work with this db, is to write the path to the json object in an array.
replace this syntax:
```javascript
db.jdb['a']['b'] = 8; // set
let num = db.jdb['a']['b']; // get
```
with this syntax:
```javascript
db.set(['a', 'b'], 8); // set
let num = db.get(['a', 'b']); // get
```
the set & get functions make sure that undefined objects will be set to {}.
that way you can write entire imaginery pathes that doesn't exist and they will be created!
another amazing thing is that the set function automaticaly saves the db (unless you set the last parameter to false).