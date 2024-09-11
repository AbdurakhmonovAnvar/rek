document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('post-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Formani standart tarzda yuborishni to'xtatadi

        // Form ma'lumotlarini olish
        const formData = new FormData(form);

        // Tokenni olish (bu erda tokenni cookie'dan olish usuli ko'rsatilgan)
        const token = getCookie('access_token'); // Cookie'dan token olish

        // Ajax request uchun ma'lumotlarni tayyorlash
        const requestData = {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Accept': 'application/json',
            },
            body: formData,
        };

        // Request yuborish
        fetch('/api/v1/adver_post/', requestData) // URL-manzilni to‘g‘ri yozing
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    // Ma'lumot muvaffaqiyatli yuborilganida bajariladigan kod
                    alert('Post successfully created!');
                    form.reset(); // Formani tozalash
                } else {
                    // Ma'lumot yuborishda xatolik yuzaga kelganda
                    alert('Error: ' + (data.message || 'Something went wrong.'));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while submitting the form.');
            });
    });

    // Cookie'dan token olish funksiyasi
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
});
