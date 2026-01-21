// Main application JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const startDateInput = document.getElementById('start-date');
    const endDateInput = document.getElementById('end-date');
    const filterBtn = document.getElementById('filter-btn');
    const clearBtn = document.getElementById('clear-btn');
    const ordersContainer = document.getElementById('orders-container');
    const orderCountSpan = document.getElementById('order-count');
    const statusMessage = document.getElementById('filter-status');

    // Load all orders on page load
    loadOrders();

    // Event listeners
    filterBtn.addEventListener('click', applyFilter);
    clearBtn.addEventListener('click', clearFilters);

    function loadOrders(startDate = null, endDate = null) {
        let url = '/api/orders';
        const params = new URLSearchParams();
        
        if (startDate) {
            params.append('start_date', startDate);
        }
        if (endDate) {
            params.append('end_date', endDate);
        }
        
        if (params.toString()) {
            url += '?' + params.toString();
        }

        fetch(url)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    showStatus('Error: ' + data.error, 'error');
                    return;
                }
                displayOrders(data.orders);
                orderCountSpan.textContent = data.count;
                
                if (startDate || endDate) {
                    showStatus(`Found ${data.count} order(s) matching your criteria`, 'success');
                }
            })
            .catch(error => {
                console.error('Error loading orders:', error);
                showStatus('Failed to load orders', 'error');
            });
    }

    function displayOrders(orders) {
        if (orders.length === 0) {
            ordersContainer.innerHTML = '<p class="no-orders">No orders found matching your criteria</p>';
            return;
        }

        ordersContainer.innerHTML = orders.map(order => `
            <div class="order-card">
                <div class="order-id">${order.id}</div>
                <div class="order-info">
                    <div><strong>Customer:</strong> ${order.customer}</div>
                    <div><strong>Date:</strong> ${formatDate(order.date)}</div>
                    <div><strong>Amount:</strong> $${order.amount.toFixed(2)}</div>
                    <div>
                        <strong>Status:</strong> 
                        <span class="order-status status-${order.status}">${order.status}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }

    function applyFilter() {
        const startDate = startDateInput.value;
        const endDate = endDateInput.value;

        if (!startDate && !endDate) {
            showStatus('Please select at least one date', 'error');
            return;
        }

        if (startDate && endDate && startDate > endDate) {
            showStatus('Start date must be before end date', 'error');
            return;
        }

        loadOrders(startDate, endDate);
    }

    function clearFilters() {
        startDateInput.value = '';
        endDateInput.value = '';
        loadOrders();
        hideStatus();
    }

    function formatDate(dateString) {
        const date = new Date(dateString + 'T00:00:00');
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
    }

    function showStatus(message, type) {
        statusMessage.textContent = message;
        statusMessage.className = 'status-message show ' + type;
    }

    function hideStatus() {
        statusMessage.className = 'status-message';
    }
});
