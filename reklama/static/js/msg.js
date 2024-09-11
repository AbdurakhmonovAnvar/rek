// Cookie-dan tokenni olish uchun yordamchi funksiya
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// API endpointlarini haqiqiy URL bilan almashtiring
const fetchMessagesUrl = '/api/v1/message/';
const sendMessageUrl = '/api/v1/message_create/';

// Xabarlarni olish va ko'rsatish funksiyasi
async function fetchMessages() {
    try {
        const token = getCookie('access_token'); // Tokenni cookie-dan oling
        const response = await fetch(fetchMessagesUrl, {
            headers: {
                'Authorization': `Bearer ${token}` // Tokenni headerda yuboring
            }
        });
        const data = await response.json();
        const messageList = document.getElementById('message-list');
        messageList.innerHTML = ''; // Oldingi xabarlarni tozalash

        data.forEach(message => {
            const messageElement = document.createElement('div');
            messageElement.className = 'message';
            messageElement.innerHTML = `
                <p><strong>User ${message.user}:</strong> ${message.message}</p>
                <p><small>${message.created_at}</small></p>
            `;
            messageList.appendChild(messageElement);
        });
    } catch (error) {
        console.error('Xabarlarni olishda xatolik:', error);
    }
}

// Yangi xabar yuborish funksiyasi
async function sendMessage() {
    const messageInput = document.getElementById('message-input');
    const messageText = messageInput.value.trim();

    if (!messageText) {
        alert('Xabar matnini kiriting!');
        return;
    }

    try {
        const token = getCookie('access_token'); // Tokenni cookie-dan oling
        await fetch(sendMessageUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}` // Tokenni headerda yuboring
            },
            body: JSON.stringify({ message: messageText })
        });
        messageInput.value = ''; // Kirish maydonini tozalash
        fetchMessages(); // Xabarlar ro‘yxatini yangilash
    } catch (error) {
        console.error('Xabar yuborishda xatolik:', error);
    }
}

// Yuborish tugmasi uchun hodisa tinglovchisi
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('send-button').addEventListener('click', sendMessage);

    // Sahifa yuklanganda xabarlarni olish
    fetchMessages();
});
