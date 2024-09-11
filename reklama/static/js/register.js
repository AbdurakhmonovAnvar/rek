console.log('JavaScript fayli yuklandi');

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM to\'liq yuklandi');
    document.getElementById('register-form').addEventListener('submit', async function (e) {
        e.preventDefault();

        console.log('Forma yuborilmoqda');

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        console.log(`Username: ${username}, Password: ${password}`);

        try {
            const registerResponse = await fetch('/api/v1/user/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            });

            if (!registerResponse.ok) {
                throw new Error('Registration failed! Status: ' + registerResponse.status);
            }

            console.log('Registration successful');

            const tokenResponse = await fetch('/api/v1/get_token/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            });

            if (!tokenResponse.ok) {
                throw new Error('Token olishda xatolik yuz berdi! Status: ' + tokenResponse.status);
            }

            const tokenData = await tokenResponse.json();
            console.log("Access Token:", tokenData.access);
            console.log("Refresh Token:", tokenData.refresh);

            document.cookie = `access_token=${tokenData.access}; path=/; secure; expires=${new Date(new Date().getTime() + 3600 * 1000).toUTCString()}`;
            document.cookie = `refresh_token=${tokenData.refresh}; path=/; secure; expires=${new Date(new Date().getTime() + 7 * 24 * 3600 * 1000).toUTCString()}`;

            window.location.href = '/home/';
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
