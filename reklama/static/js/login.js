document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('login-form').addEventListener('submit', async function (e) {
        e.preventDefault(); // Forma yuborilishini to'xtatish

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        console.log(username);

        try {
            const response = await fetch('/api/v1/get_token/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            });

            if (!response.ok) {
                throw new Error('Login failed! Status: ' + response.status);
            }

            const data = await response.json();
            console.log("Access Token:", data.access);
            console.log("Refresh Token:", data.refresh);

            // Tokenlarni cookie'ga saqlash
            document.cookie = `access_token=${data.access}; path=/; secure; expires=${new Date(new Date().getTime() + 3600 * 1000).toUTCString()}`;
            document.cookie = `refresh_token=${data.refresh}; path=/; secure; expires=${new Date(new Date().getTime() + 7 * 24 * 3600 * 1000).toUTCString()}`;
            window.location.href = '/home/';
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
