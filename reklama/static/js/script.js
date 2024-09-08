// Sayt yuklanganida ishlash uchun
document.addEventListener('DOMContentLoaded', function() {
    console.log('Sahifa yuklandi!');

    // Menyu tugmalarini interaktiv qilish
    const menuItems = document.querySelectorAll('nav ul li');

    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            alert(`Siz ${item.textContent} tugmasini bosdingiz`);
        });
    });

    // Misol uchun, footer'ni yuqoriga surish
    const footer = document.querySelector('footer');
    if (footer) {
        footer.addEventListener('click', function() {
            console.log('Footer tugmasi bosildi!');
        });
    }

    // Ko'rinishdagi filterni ochish va yopish funksiyasi
    const toggleFilter = document.querySelector('.toggle-filter');
    const filter = document.getElementById('filter');

    if (toggleFilter && filter) {
        toggleFilter.addEventListener('click', function() {
            if (filter.style.display === 'none') {
                filter.style.display = 'block';
            } else {
                filter.style.display = 'none';
            }
        });
    }
});
