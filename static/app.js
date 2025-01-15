// Function to display data as a table
function displayDataAsTable(data, containerId, headers) {
    const container = document.getElementById(containerId);
    container.innerHTML = ''; // Clear previous content

    if (!data || Object.keys(data).length === 0) {
        container.textContent = 'No data available.';
        return;
    }

    const table = document.createElement('table');
    table.className = 'data-table';

    // Create table header
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    headers.forEach(header => {
        const th = document.createElement('th');
        th.textContent = header;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table body
    const tbody = document.createElement('tbody');
    for (const row of data) {
        const tr = document.createElement('tr');
        for (const cell of row) {
            const td = document.createElement('td');
            td.textContent = cell;
            tr.appendChild(td);
        }
        tbody.appendChild(tr);
    }
    table.appendChild(tbody);

    container.appendChild(table);
}

// Function to fetch arbitrage data
function fetchArbitrageData() {
    const result = document.getElementById('arbitrage-result');
    result.textContent = ''; // Clear old result

    fetch('/api/v1/arbitrage-opportunities')
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                const formattedData = data.data.map(item => {
                    const [buyFrom, sellTo] = item.direction.split(" -> ");
                    return [
                        item.pair,
                        buyFrom, // Correctly assign Buy From
                        sellTo,  // Correctly assign Sell To
                        item.profit
                    ];
                });
                displayDataAsTable(formattedData, 'arbitrage-result', ['Pair Name', 'Buy From', 'Sell To', 'Profit']);
                showNotification('Arbitrage opportunities fetched successfully!', 'success');
            } else {
                showNotification('Failed to fetch arbitrage opportunities.', 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showNotification('Error fetching arbitrage opportunities.', 'error');
        });
}


// Function to fetch Binance data
function fetchBinanceData() {
    const result = document.getElementById('binance-result');
    result.textContent = ''; // Clear old result

    fetch('/api/v1/markets/binance')
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                const formattedData = Object.entries(data.data).map(([key, value]) => [key, value]);
                displayDataAsTable(formattedData, 'binance-result', ['Pair Name', 'Pair Price']);
                showNotification('Binance data fetched successfully!', 'success');
            } else {
                showNotification('Failed to fetch Binance data.', 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showNotification('Error fetching Binance data.', 'error');
        });
}

// Function to fetch Solana data
function fetchSolanaData() {
    const result = document.getElementById('solana-result');
    result.textContent = ''; // Clear old result

    fetch('/api/v1/markets/solana')
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                const formattedData = Object.entries(data.data).map(([key, value]) => [key, value]);
                displayDataAsTable(formattedData, 'solana-result', ['Pair Name', 'Pair Price']);
                showNotification('Solana data fetched successfully!', 'success');
            } else {
                showNotification('Failed to fetch Solana data.', 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showNotification('Error fetching Solana data.', 'error');
        });
}

// Notification function
function showNotification(message, type) {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = `notification ${type}`;
    notification.classList.remove('hidden');

    setTimeout(() => {
        notification.classList.add('hidden');
    }, 3000);
}
