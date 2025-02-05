const express = require('express');

const app = express();
const port = 3000;

app.use(express.json());

let products = [
    { id: 1, name: 'Product 1', price: 100 },
    { id: 2, name: 'Product 2', price: 200 },
];

let customers = [
    { id: 1, name: 'Customer 1', email: 'customer1@example.com' },
    { id: 2, name: 'Customer 2', email: 'customer2@example.com' },
];

// Routes for products
app.get('/products', (req, res) => {
    res.json(products);
});

app.get('/products/:id', (req, res) => {
    const product = products.find(p => p.id === parseInt(req.params.id));
    if (!product) return res.status(404).send('Product not found');
    res.json(product);
});

app.post('/products', (req, res) => {
    const product = {
        id: products.length + 1,
        name: req.body.name,
        price: req.body.price
    };
    products.push(product);
    res.status(201).json(product);
});

app.put('/products/:id', (req, res) => {
    const product = products.find(p => p.id === parseInt(req.params.id));
    if (!product) return res.status(404).send('Product not found');

    product.name = req.body.name;
    product.price = req.body.price;
    res.json(product);
});

app.delete('/products/:id', (req, res) => {
    const productIndex = products.findIndex(p => p.id === parseInt(req.params.id));
    if (productIndex === -1) return res.status(404).send('Product not found');

    const deletedProduct = products.splice(productIndex, 1);
    res.json(deletedProduct);
});

// Routes for customers
app.get('/customers', (req, res) => {
    res.json(customers);
});

app.get('/customers/:id', (req, res) => {
    const customer = customers.find(c => c.id === parseInt(req.params.id));
    if (!customer) return res.status(404).send('Customer not found');
    res.json(customer);
});

app.post('/customers', (req, res) => {
    const customer = {
        id: customers.length + 1,
        name: req.body.name,
        email: req.body.email
    };
    customers.push(customer);
    res.status(201).json(customer);
});

app.put('/customers/:id', (req, res) => {
    const customer = customers.find(c => c.id === parseInt(req.params.id));
    if (!customer) return res.status(404).send('Customer not found');

    customer.name = req.body.name;
    customer.email = req.body.email;
    res.json(customer);
});

app.delete('/customers/:id', (req, res) => {
    const customerIndex = customers.findIndex(c => c.id === parseInt(req.params.id));
    if (customerIndex === -1) return res.status(404).send('Customer not found');

    const deletedCustomer = customers.splice(customerIndex, 1);
    res.json(deletedCustomer);
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});