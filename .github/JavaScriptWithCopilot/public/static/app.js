document.addEventListener('DOMContentLoaded', () => {
    const accountsDiv = document.getElementById('accounts');
    const depositForm = document.getElementById('deposit-form');
    const withdrawForm = document.getElementById('withdraw-form');

    // Fetch and display accounts
    function fetchAccounts() {
        fetch('/accounts')
            .then(response => response.json())
            .then(accounts => {
                accountsDiv.innerHTML = '';
                for (const [accountNumber, account] of Object.entries(accounts)) {
                    const accountDiv = document.createElement('div');
                    accountDiv.className = 'account';
                    accountDiv.innerHTML = `<p>${account}</p>`;
                    accountsDiv.appendChild(accountDiv);
                }
            });
    }

    // Handle deposit
    depositForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const accountNumber = document.getElementById('deposit-account-number').value;
        const amount = document.getElementById('deposit-amount').value;

        fetch(`/accounts/${accountNumber}/deposit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ amount: parseFloat(amount) })
        })
        .then(response => response.json())
        .then(result => {
            alert(result.message || result.error);
            fetchAccounts();
        });
    });

    // Handle withdraw
    withdrawForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const accountNumber = document.getElementById('withdraw-account-number').value;
        const amount = document.getElementById('withdraw-amount').value;

        fetch(`/accounts/${accountNumber}/withdraw`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ amount: parseFloat(amount) })
        })
        .then(response => response.json())
        .then(result => {
            alert(result.message || result.error);
            fetchAccounts();
        });
    });

    // Initial fetch
    fetchAccounts();
});