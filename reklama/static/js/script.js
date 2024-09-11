// nav.js
document.addEventListener('DOMContentLoaded', () => {
    const loginLink = document.querySelector('nav ul li a[href="/login"]');
    const registerLink = document.querySelector('nav ul li a[href="/register"]');
    const userInfoDiv = document.createElement('li');
    userInfoDiv.id = 'user-info';
    const nav = document.querySelector('nav ul');

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
            // Username'ni ko'rsatish
            const username = data.username;
            userInfoDiv.innerHTML = `<span>${username}</span>`;

            // Login va Register havolalarini yashirish
            if (loginLink) {
                loginLink.style.display = 'none';
            }
            if (registerLink) {
                registerLink.style.display = 'none';
            }

            // User info'ni navga qo'shish
            nav.appendChild(userInfoDiv);
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        });
    } else {
        // Token mavjud emas, login va register havolalarini ko'rsatish
        if (loginLink) {
            loginLink.style.display = 'block';
        }
        if (registerLink) {
            registerLink.style.display = 'block';
        }
    }
});
