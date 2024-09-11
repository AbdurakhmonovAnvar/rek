document.addEventListener('DOMContentLoaded', function() {
    const logoutButton = document.getElementById('logout-button');

    if (logoutButton) {
        logoutButton.addEventListener('click', function() {
            // Tokenni cookie'dan o'chirish
            deleteCookie('access_token');

            // Logout so'rovini yuborish
            fetch('/api/v1/logout/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                },
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    // Logout muvaffaqiyatli amalga oshirilganida
                    alert('Successfully logged out.');
                    window.location.href = '/login/'; // Foydalanuvchini login sahifasiga yo‘naltirish
                } else {
                    // Logout vaqtida xatolik yuzaga kelganda
                    alert('Error: ' + (data.message || 'Logout failed.'));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while logging out.');
            });
        });
    }

    // Cookie'dan tokenni o'chirish funksiyasi
    function deleteCookie(name) {
        document.cookie = name + '=; Max-Age=-99999999;';
    }
});
