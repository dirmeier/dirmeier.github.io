const express = require('express');
const path = require('path');
const cors = require('cors');
const morgan = require('morgan');
const bodyParser = require('body-parser');

const app = express();
app.use(morgan('tiny'));
app.use(cors());
app.use(bodyParser.json());
app.use(express.static(__dirname + '/dist'));

app.get('*', (req, res) => {
	res.sendFile(path.resolve(__dirname, 'dist', 'index.html'));
});

const port = process.env.PORT || 4000;
app.listen(port, () => {
	console.log(`listening on ${port}`);
});
