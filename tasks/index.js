import express from 'express'
import paymentRoutes from './routes/payment.routes.js'
import {PORT} from '/config.js'
import path from 'path'


const app = express()

app.use(express.json())

app.use(paymentRoutes)

app.use(express.static(path.resolve('src/public')))

app.listen(3000)
console.log('Server on port', 3000)