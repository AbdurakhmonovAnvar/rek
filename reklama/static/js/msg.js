// Cookie-dan tokenni olish uchun yordamchi funksiya
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// API endpointlarini haqiqiy URL bilan almashtiring
const fetchMessagesUrl = '/api/v1/message/';
const sendMessageUrl = '/api/v1/message_create/';
const deleteMessageUrl = (id) => `/api/v1/message/${id}/`; // Xabarni o'chirish uchun URL

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
                <div class="message-content">
                    <p><strong>User ${message.user}:</strong> ${message.message}</p>
                    <p><small>${message.created_at}</small></p>
                </div>
                <div class="message-actions">
                    <a><button class="update-button">Update</button></a>
                    <a><button class="delete-button" data-id="${message.id}">Delete</button></a>
                </div>
            `;
            messageList.appendChild(messageElement);

            // O'chirish tugmasi bosilganda
            messageElement.querySelector('.delete-button').addEventListener('click', function () {
                const messageId = this.getAttribute('data-id');
                deleteMessage(messageId);
            });
        });
    } catch (error) {
        console.error('Xabarlarni olishda xatolik:', error);
    }
}

// Xabarni o'chirish funksiyasi
async function deleteMessage(messageId) {
    const confirmDelete = confirm('Bu xabarni o‘chirishga ishonchingiz komilmi?');
    if (!confirmDelete) return;

    try {
        const token = getCookie('access_token'); // Tokenni cookie-dan oling
        const response = await fetch(deleteMessageUrl(messageId), {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${token}` // Tokenni headerda yuboring
            }
        });

        if (response.ok) {
            fetchMessages(); // O'chirilgandan keyin xabarlarni yangilash
        } else {
            console.error('Xabarni o‘chirishda xatolik:', response.statusText);
        }
    } catch (error) {
        console.error('Xabarni o‘chirishda xatolik:', error);
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
