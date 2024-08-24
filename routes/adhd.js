const express = require('express')
const router = express.Router()

// define the home page route
router.get('/', (req, res) => {
    res.render("adhd/adhd")
})

// define the about route
router.get('/diagnosis', (req, res) => {
    res.render("adhd/adhd-diag")
})
router.get('/treatment', (req, res) => {
    res.render("adhd/adhd-treat")
}) 
router.get('/tova', (req, res) => {
    res.render("adhd/tova")
})
router.get('/quiz', (req, res) => {
    res.render("adhd/adhd-quiz")
})
router.get('/puzzle', (req, res) => {
    res.render("adhd/adhd-puzzle")
})
router.get('/map', (req, res) => {
    res.render("adhd/adhd-map")
})
module.exports = router