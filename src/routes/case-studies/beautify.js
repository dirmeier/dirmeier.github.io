'use strict';

const fs = require('fs');

let json = JSON.parse(fs.readFileSync('books.json'));
let json_str = JSON.stringify(json, null, 2);
fs.writeFileSync('books.json', json_str);
