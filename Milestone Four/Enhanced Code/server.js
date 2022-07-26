// Troy Smith
// CS-499-H6771
// Milestone Four

// This code constructs the server and components
// run command 'npm run devStart' in terminal 
// Success =  'Server Started' and 'Connected to Database'


require('dotenv').config()

const express = require('express')
const app = express()
const mongoose = require('mongoose')

mongoose.connect(process.env.DATABASE_URL)
const db = mongoose.connection
db.on('error', (error) => console.error(error))
db.once('open', () => console.log('Connected to Database'))

app.use(express.json())

const dogsRouter = require('./routes/dogs')
app.use('/dogs', dogsRouter)

app.listen(3000, () => console.log('Server Started'))
