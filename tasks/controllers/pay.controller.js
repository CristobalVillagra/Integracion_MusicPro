import stripe from 'stripe'


const stripe = new Stripe(sk_test_4eC39HqLyjWDarjtT1zdp7dc)


export const createSession = async (req, res) => {
    const session = await stripe.checkout.sessions.create({
        line_items: [
            {
                price_data: {
                    product_data: {
                        name: 'teclado',
                        description: 'teclado electrico',
                    },
                    currency: 'usd',
                    unit_amount: 2000,
                },
                quantity: 1
            },
            {
                price_data: {
                    prouct_data: {
                        name: 'violin',
                        description: 'cuerdas de extracto de cabello de potro', 
                    },
                    currency: 'usd',
                    unit_amount: 1000,
                },
                quantity: 2
            }
        ],
        mode: 'payment',
        success_url: 'http://localhost:3000/sucess',
        cancel_url: 'http://localhost:3000/cancel',
    })
    return res.json(session)

}