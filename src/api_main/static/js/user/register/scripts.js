document.getElementById('back-link').addEventListener('click', (e) => {
    e.preventDefault();
    window.location.href = '/home';
});

document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const msgEl = document.getElementById('message'); 
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const data = { user_name: username, password: password };

    try {
        const response = await fetch('/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const responseData = await response.json();

        if (response.ok) {
            msgEl.style.color = 'green';
            msgEl.textContent = responseData.message;
            
            setTimeout(() => {
                window.location.href = '/home'
            }, 1000);
        } else {
            const error = await response.json();
            document.getElementById('message').textContent = error.message || 'Erro ao cadastrar.';
        }
    } catch (err) {
        document.getElementById('message').textContent = 'Erro de conexão.';
    }
});
