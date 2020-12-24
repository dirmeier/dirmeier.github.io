fs = require('fs');

var r = [];
var content = fs.readFileSync("books.tsv", "utf8");
var v = content.split("\n");
for (var i = 0; i < v.length; i++) {
  var w = v[i].split("\t");
  r.push({
    title: w[0],
    author: w[1],
    publisher: w[2]
  });
}

fs.writeFile('books.json', JSON.stringify(r, null, 4), (err) => {
    if (err) {
        throw err;
    }
    console.log("JSON data is saved.");
});