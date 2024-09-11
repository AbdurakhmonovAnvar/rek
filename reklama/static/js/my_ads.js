document.addEventListener('DOMContentLoaded', function() {
    const adsList = document.getElementById('ads-list');

    // Tokenni olish (cookie'dan olish usuli)
    const token = getCookie('access_token'); // Cookie'dan token olish

    // API so'rovini yuborish
    fetch('/api/v1/adver/', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Accept': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (Array.isArray(data)) {
            // E'lonlar ro'yxatini ko'rsatish
            adsList.innerHTML = data.map(ad => `
                <div class="ad-item">
                    <img src="${ad.image_url ? ad.image_url : ''}" alt="Ad Image" class="ad-image">
                    <div class="ad-details">
                        <h2 class="ad-title">${ad.title || 'No Title'}</h2>
                        <p class="ad-content">${ad.content || 'No Content'}</p>
                        <p class="ad-price">${ad.price || 'No Price'} (${ad.price_type || 'No Price Type'})</p>
                        <p class="ad-address">${ad.address || 'No Address'}</p>
                        <p class="ad-contact">${ad.contact || 'No Contact'}</p>
                        <p class="ad-status">${ad.status || 'No Status'}</p>
                        <p class="ad-created-at">${new Date(ad.created_at).toLocaleDateString() || 'No Date'}</p>
                        <div class="ad-actions">
                            <button class="edit-button" data-id="${ad.id}">Edit</button>
                            <button class="delete-button" data-id="${ad.id}">Delete</button>
                        </div>
                    </div>
                </div>
            `).join('');
        } else {
            adsList.innerHTML = '<p>No ads found.</p>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        adsList.innerHTML = '<p>An error occurred while fetching ads.</p>';
    });

    // Cookie'dan token olish funksiyasi
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
});
