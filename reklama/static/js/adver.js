document.addEventListener('DOMContentLoaded', () => {
    const contentDiv = document.getElementById('content');
    const filterButton = document.getElementById('filterButton');
    const loginDiv = document.getElementById('loginDiv');
    const userInfoDiv = document.getElementById('userInfo');
    const usernameSpan = document.getElementById('username');
    const loginLink = document.getElementById('login-link');
    const registerLink = document.getElementById('register-link');

    // Cookie'ni olish funksiyasi
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }

    // Tokenlarni olish
    const accessToken = getCookie('access_token');

    if (accessToken) {
        // Token mavjud bo'lsa, foydalanuvchi ma'lumotlarini olish
        fetch('/api/v1/user/', {
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        })
        .then(response => response.json())
        .then(data => {
            // Username'ni ko'rsatish va login va register havolalarini yashirish
            if (usernameSpan) {
                usernameSpan.textContent = data.username;
            }
            if (userInfoDiv) {
                userInfoDiv.style.display = 'block';
            }
            if (loginLink) {
                loginLink.style.display = 'none';
            }
            if (registerLink) {
                registerLink.style.display = 'none';
            }
            if (loginDiv) {
                loginDiv.style.display = 'none';
            }
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        });
    } else {
        // Token mavjud emas, login va register bo'limlarini ko'rsatish
        if (loginDiv) {
            loginDiv.style.display = 'block';
        }
        if (loginLink) {
            loginLink.style.display = 'block';
        }
        if (registerLink) {
            registerLink.style.display = 'block';
        }
    }

    // Ma'lumotlarni random tarzda olish uchun API so'rov
    fetch('/api/v1/random_adver/')
        .then(response => response.json())
        .then(data => {
            // Ma'lumotlarni ko'rsatish uchun funksiya chaqiriladi
            displayAds(data);
        })
        .catch(error => {
            console.error('Error fetching ads:', error);
        });

    // Filter bo'yicha ma'lumotlarni olish
    filterButton.addEventListener('click', () => {
        const region = document.getElementById('region').value;
        const city = document.getElementById('city').value;
        const type = document.getElementById('type').value;
        const startPrice = document.getElementById('startPrice').value;
        const endPrice = document.getElementById('endPrice').value;
        const currencyType = document.getElementById('currencyType').value;

        // Filter ma'lumotlarini API orqali olish
        const apiUrl = `/api/v1/filter?street=${city}&type=${type}&start_price=${startPrice}&end_price=${endPrice}&price_type=${currencyType}`;

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                // Ma'lumotlar mavjud bo'lsa, ular ko'rsatiladi
                if (data.length > 0) {
                    contentDiv.innerHTML = ''; // Oldingi ma'lumotlarni tozalash
                    displayAds(data);
                } else {
                    // Agar ma'lumotlar bo'lmasa
                    contentDiv.innerHTML = '<p>Bunday e\'lon hozircha mavjud emas</p>';
                }
            })
            .catch(error => {
                console.error('Error fetching filtered ads:', error);
            });
    });

    // E'lonlarni HTMLga qo'shish funksiyasi
    function displayAds(ads) {
        ads.forEach(ad => {
            const adDiv = document.createElement('div');
            adDiv.classList.add('ad-item');

            adDiv.innerHTML = `
                <h3>${ad.title}</h3>
                <p><strong>Content:</strong><br>${ad.content}</p>
                <p><strong>Address:</strong> ${ad.address}</p>
                <p><strong>Narx:</strong> ${ad.price} ${ad.price_type}</p>
                <p><strong>Bog'lanish uchun:</strong> ${ad.contact}</p>
                <p><strong> </strong> ${new Date(ad.created_at).toLocaleDateString()}</p>
                ${ad.image_url ? `<img src="${ad.image_url}" alt="${ad.title}" class="ad-image">` : ''}
            `;

            // Kontent qismiga qo'shish
            contentDiv.appendChild(adDiv);
        });
    }
});
