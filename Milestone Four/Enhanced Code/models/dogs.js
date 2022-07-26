// Troy Smith
// CS-499-H6771
// Milestone Four

// This code establishes the attributes of the 
// items in the database collection (Dog)

const { default: mongoose } = require('mongoose')
const mogoose = require('mongoose')

// Establish each feature of the entry
const dogsSchema = new mongoose.Schema({
    name: {
      type: String,
      required: true  
    },
    dogFromShelter: {
        type: String,
        required: true 
    },
    acquiredDate: {
        type: Date,
        required: true,
        default: Date.now
    }
})

module.exports = mongoose.model('Dog', dogsSchema)