document.addEventListener('DOMContentLoaded', () => {
    const loginLink = document.querySelector('nav ul li a[href="/login"]');
    const registerLink = document.querySelector('nav ul li a[href="/register"]');
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
            // Username'ni select menyuga qo'shish
            const username = data.username;
            const selectElement = document.createElement('select');
            selectElement.id = 'user-info';
            selectElement.innerHTML = `<option>${username}</option>`;

            // Dropdown opsiyalarini qo'shish
            const options = [
                { text: "E'lon yozish", value: "/post" },
                { text: "Mening e'lonlarim", value: "/my_ads" },
                { text: "Adminga xabar qoldirish", value: "/msg" }
            ];

            options.forEach(option => {
                const optionElement = document.createElement('option');
                optionElement.value = option.value;
                optionElement.textContent = option.text;
                selectElement.appendChild(optionElement);
            });

            // Login va Register havolalarini yashirish
            if (loginLink) {
                loginLink.style.display = 'none';
            }
            if (registerLink) {
                registerLink.style.display = 'none';
            }

            // User info'ni navga qo'shish
            nav.appendChild(selectElement);

            // Select menyu tanloviga qo'shimcha funksiyalar
            selectElement.addEventListener('change', (event) => {
                const selectedValue = event.target.value;
                if (selectedValue) {
                    window.location.href = selectedValue;
                }
            });
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
