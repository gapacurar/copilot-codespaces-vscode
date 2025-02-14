document.addEventListener('DOMContentLoaded', () => {
    const productList = document.getElementById('product-list');
    const addProductForm = document.getElementById('add-product-form');
    const productNameInput = document.getElementById('product-name');
    const productPriceInput = document.getElementById('product-price');

    // Fetch and display products
    function fetchProducts() {
        fetch('http://localhost:3000/products') // Ensure this points to your Express.js server
            .then(response => response.json())
            .then(products => {
                productList.innerHTML = '';
                products.forEach(product => {
                    const productDiv = document.createElement('div');
                    productDiv.className = 'product';
                    productDiv.innerHTML = `
                        <h3>${product.name}</h3>
                        <p>Price: $${product.price}</p>
                        <button onclick="deleteProduct(${product.id})">Delete</button>
                    `;
                    productList.appendChild(productDiv);
                });
            });
    }

    // Add product
    addProductForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = productNameInput.value;
        const price = productPriceInput.value;

        fetch('http://localhost:3000/products', { // Ensure this points to your Express.js server
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, price })
        })
        .then(response => response.json())
        .then(product => {
            fetchProducts();
            productNameInput.value = '';
            productPriceInput.value = '';
        });
    });

    // Delete product
    window.deleteProduct = function(id) {
        fetch(`http://localhost:3000/products/${id}`, { // Ensure this points to your Express.js server
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(() => {
            fetchProducts();
        });
    };

    // Initial fetch
    fetchProducts();
});