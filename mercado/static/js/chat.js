document.addEventListener('DOMContentLoaded', function() {
    const messageForm = document.getElementById('messageForm');
    const chatMessages = document.getElementById('chatMessages');
    const errorToast = new bootstrap.Toast(document.getElementById('errorToast'));

    function showError(message) {
        const toastBody = document.querySelector('#errorToast .toast-body');
        toastBody.textContent = message;
        errorToast.show();
    }

    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function createMessageElement(message) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${message.is_mine ? 'mine' : ''}`;
        messageDiv.dataset.messageId = message.id;

        messageDiv.innerHTML = `
            <div class="content">${message.text}</div>
            <small class="text-muted d-block mt-1">
                ${message.sender_username} • ${message.created_at}
            </small>
        `;

        return messageDiv;
    }

    if (messageForm) {
        messageForm.addEventListener('submit', async function(e) {
            e.preventDefault();

            const messageInput = this.querySelector('input[name="message"]');
            const message = messageInput.value.trim();

            if (!message) {
                showError('El mensaje no puede estar vacío');
                return;
            }

            const submitButton = this.querySelector('button[type="submit"]');
            submitButton.disabled = true;

            try {
                const response = await fetch(window.location.href, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    },
                    body: JSON.stringify({ message })
                });

                if (!response.ok) {
                    throw new Error(`Error ${response.status}: ${response.statusText}`);
                }

                const data = await response.json();
                
                if (data.status === 'success') {
                    const messageElement = createMessageElement({
                        id: data.message.id,
                        text: data.message.text,
                        sender_username: data.message.sender_username,
                        created_at: data.message.created_at,
                        is_mine: true
                    });

                    chatMessages.appendChild(messageElement);
                    scrollToBottom();
                    messageInput.value = '';
                } else {
                    showError(data.message || 'Error al enviar el mensaje');
                }
            } catch (error) {
                console.error('Error:', error);
                showError('Error al enviar el mensaje. Por favor, inténtalo de nuevo.');
            } finally {
                submitButton.disabled = false;
            }
        });
    }

    // Scroll inicial al fondo del chat
    scrollToBottom();
});