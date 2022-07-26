// Troy Smith
// CS-499-H6771
// Milestone Four

// This code is used by the .rest file to work
// within the database and perform the
// CRUD operations

// use express and sets model of object (dog)
const express = require('express')
const router = express.Router()
const Dog = require('../models/dogs')

// Getting all of collection
router.get('/', async (req, res) => {
   try {
     const dogs = await Dog.find()
     res.json(dogs)
   } catch (err) {
     res.status(500).json({message: err.message})
   }
})

// Getting One in collection
router.get('/:id', getDog, (req, res) => {
  res.json(res.dog) 
})

// Creating One in the collection
router.post('/', async (req, res) => {
  const dog = new Dog({
    name: req.body.name,
    dogFromShelter: req.body.dogFromShelter
  })
  try {
    const newDog = await dog.save()
    res.status(201).json(newDog)
  } catch (err) {
    res.status(400).json({ message: err.message})
  }
})

// Updating One in the collection
router.patch('/:id', getDog, async (req, res) => {
  if (req.body.name != null) {
    res.dog.name = req.body.name
  }  
  if (req.dogFromShelter != null) {
    res.dog.dogFromShelter = req.body.dogFromShelter
  }
  if (req.age != null) {
    res.dog.age = req.body.age
  }
  try {
    const updatedDog = await res.dog.save()
    res.json(updatedDog)
  } catch (err) {
    res.status(400).json({ message: err.message})
  }
})

// Deleting One in the collection
router.delete('/:id', getDog, async (req, res) => {
  try {
    await res.dog.remove()
    res.json({message: 'Deleted Dog'})
  } catch (err) {
    res.status(500).json({ message: err.message })
  } 
})

// This asyncronis function alliviates having to replicat
// through each operation above
async function getDog(req, res, next) {
  let dog  
  try {
    dog = await Dog.findById(req.params.id)
    if (dog == null) {
        return res.status(404).json({ message: 'Cannot find dog'})
    }
  } catch (err) {
    return res.status(500).json({ message: err.message })
  } 

  res.dog = dog
  next()
}

module.exports = router