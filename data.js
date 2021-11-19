const axios = require('axios')

axios.post('http://127.0.0.1:5000/users/login', {
    username: '',
    password: ''
}, {
    headers: {
        'Content-Type' : 'application/json'
    }
})
.then((response) => {
    console.log(response.data)
})
.catch((error) => {
    console.log(error.response)
})

// axios.post('http://127.0.0.1:5000/users/signup', {
//     email: 'lloydwarui27@gmail.com',
//     password: 'noni'
// }, {
//     headers: {
//         'Content-Type' : 'application/json'
//     }
// })
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.get('http://127.0.0.1:5000/dashboard/farms/1',)
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.get('http://127.0.0.1:5000/dashboard/farm/chickendata/1',)
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.post('http://127.0.0.1:5000/dashboard/farm/chickendata/1', {
//     chicken_type: 'broilers',
    //    price: 20000,
//     number: 50
// }, {
//     headers: {
//         'Content-Type' : 'application/json'
//     }
// })
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.get('http://127.0.0.1:5000/dashboard/farm/chickensales/1',)
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.post('http://127.0.0.1:5000/dashboard/farm/chickensales/1', {
//     
//     chicken_type: 'broilers',
//     sales_to: 'mamaa',
//     chicken_sold: 50,
//     price_per_chicken: 1400,
//     medium_of_sale: 'mpesa'
// }, {
//     headers: {
//         'Content-Type' : 'application/json'
//     }
// })
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.get('http://127.0.0.1:5000/dashboard/farm/deathreports/1',)
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.post('http://127.0.0.1:5000/dashboard/farm/deathreports/1', {
//     broilers: 1,
//     layers: 1
// }, {
//     headers: {
//         'Content-Type' : 'application/json'
//     }
// })
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.get('http://127.0.0.1:5000/dashboard/farm/eggdata/1',)
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.post('http://127.0.0.1:5000/dashboard/farm/eggdata/1', {
//     egg_type: 'layers',
//     no_of_eggs_laid: 30
// }, {
//     headers: {
//         'Content-Type' : 'application/json'
//     }
// })
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.get('http://127.0.0.1:5000/dashboard/farm/eggsales/1',)
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.post('http://127.0.0.1:5000/dashboard/farm/eggsales/1', {
//     eggs_sold: 10,
//     sales_to: 'mamaa'
// }, {
//     headers: {
//         'Content-Type' : 'application/json'
//     }
// })
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.get('http://127.0.0.1:5000/dashboard/farm/feeds/1',)
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.post('http://127.0.0.1:5000/dashboard/farm/feeds/1', {
//     feed_type: 'layers',
//     bags_purchased: 10,
//     price_per_bag: 650,
//     medium_of_sale: 'mpesa'
// }, {
//     headers: {
//         'Content-Type' : 'application/json'
//     }
// })
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.get('http://127.0.0.1:5000/dashboard/farm/vaccines/1',)
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.post('http://127.0.0.1:5000/dashboard/farm/vaccines/1', {
//     name: 'Moderna',
//     units: 10,
//     price_per_unit: 1250,
//     medium_of_sale: 'mpesa'
// }, {
//     headers: {
//         'Content-Type' : 'application/json'
//     }
// })
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.get('http://127.0.0.1:5000/dashboard/farm/additionalexpenses/1',)
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })

// axios.post('http://127.0.0.1:5000/dashboard/farm/additionalexpenses/1', {
//     name: 'Materials',
//     description: 'Building materials for chicken house',
//     cost: 25500,
//     medium_of_sale: 'mpesa'
// }, {
//     headers: {
//         'Content-Type' : 'application/json'
//     }
// })
// .then((response) => {
//     console.log(response.data)
// })
// .catch((error) => {
//     console.log(error.response)
// })