/*
NSEL - Nimi Server Express Library
~ By: Nimi
*/

const fs = require('fs');
const mysql = require('mysql');
const express = require('express');

const PORT = process.env.PORT || 80;
const app = express();

class DB {
    
    sqlDB; // mySql db - user doesnt touch it
    prevDb; // user doesnt touch it
    jdb; // json db - user changes this one
    
    sqlDataId;
    sqlColName;
    sqlTableName;

    constructor(host, user, pass, db, dataId = 0, colName = 'data', tableName = 'info', load = true) {
        this.prevDb = -1;
        // sql db settings
        this.sqlDataId = dataId;
        this.sqlColName = colName;
        this.sqlTableName = tableName;
        // init json db
        this.jdb = {};
        // connect and load db to json db
        this.connectDB(host, user, pass, db);
        if (load)
            this.loadDB();
    }
    
    connectDB(host, user, pass, db) {
        // set this.sqlDB
        this.sqlDB = mysql.createPool({
            host: host,
            user: user,
            password: pass,
            database: db
        });
    }

    // save db to sqlDB
    saveDB() {
        if (JSON.stringify(this.prevDb) != JSON.stringify(this.jdb)) // update database only if the data has changed
        {
            let data = JSON.stringify(this.jdb);
            let q = "UPDATE " + this.sqlTableName + " SET " + this.sqlColName + " = '" + data + "' WHERE id = " + this.sqlDataId.toString() + ";";
            this.sqlDB.query(q, (err, result)=>{
                if (err)
                    throw err;

                this.prevDb = JSON.parse(JSON.stringify(this.jdb));
            });
        }
        /*
        else
        {
            console.log('same vals.. didnt save');
            console.log(this.prevDb);
            console.log(this.jdb);
        }
        */
    }

    // loads sqlDB to db
    loadDB() {
        let q = "SELECT " + this.sqlColName + " FROM " + this.sqlTableName + " WHERE id = " + this.sqlDataId.toString() + ";";
        this.sqlDB.query(q, (err, result)=>{
            if (err) {
                // err msg
                console.error('NSEL: loading from db failed, make sure you have a table named "' + this.sqlTableName + '", inside, a column named "' + this.sqlColName + '", and an entry with an id of ' + this.sqlDataId.toString() + ' which it\'s value is "{}".\n');
                throw err;
            }
            else {
                let res = result[0].data;
                this.jdb = JSON.parse(res);
            }
        });
    }

    resetDB() {
        this.jdb = {}; // clear db
        this.saveDB(); // save the cleared db
    }

    //if a json path is undefined, make it {}.
    set(pathList, value, save_db = true)
    {
        let obj = this.jdb;
        let path;
        while (pathList.length > 0)
        {
            path = pathList[0];
            pathList.splice(0, 1);
            let temp = obj[path];
            if (temp == undefined)
            {
                if (pathList.length == 0)
                    obj[path] = value;
                else
                    obj[path] = {};
            }
            if (pathList.length > 0)
                obj = obj[path];
        }
        
        if (save_db)
            this.saveDB()
    }

    get(pathList)
    {
        let obj = this.jdb;
        let path;
        while (pathList.length > 0)
        {
            path = pathList[0];
            pathList.splice(0, 1);
            let temp = obj[path];
            if (temp == undefined)
            {
                if (pathList.length == 0)
                    obj[path] = undefined;
                else
                    obj[path] = {};
            }
            obj = obj[path];
        }
        
        return obj;
    }
}

DB.prototype.toJson = function dbToJson() {
    return (this.jdb);
}

function listen(port = PORT)
{
    app.listen(port, (err)=>{
        if (err)
            throw err;

        console.log('~~~ NSEL App Active ~~~');
    });

    return app;
}

function quick(host, user, pass, db, reset = false, dataId = 0, colName = 'data', tableName = 'info', port = PORT)
{
    let database = new DB(host, user, pass, db, dataId, colName, tableName, !reset);
    let json = database.jdb;
    let app = listen(port);

    return [app, database];
}

function htmlReplace(htmlPath, src, dst)
{
    const content = fs.readFileSync(htmlPath);
    html = String(content);
    while (html.includes(src))
    {
        html = html.replace(src, dst);
    }

    return html;
}

module.exports = {DB, app, listen, quick, htmlReplace, express};