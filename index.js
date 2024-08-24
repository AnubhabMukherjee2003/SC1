const express = require('express')
const path = require("path");
const adhd = require('./routes/adhd')
// const shop = require('./routes/shop')

const app = express()
const port = 5000

app.use('/static', express.static('static'))
app.use('/adhd', adhd)
// app.use('/shop', shop)

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'))

// https://github.com/mde/ejs/wiki/Using-EJS-with-Express

app.get('/', (req, res) => {
    res.render("index")
})

app.get('/services', (req, res) => {
    res.render("services")
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})