document.getElementById('back-link').addEventListener('click', (e) => {
    e.preventDefault();
    window.location.href = '/home';
});

document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();
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

        if (response.ok) {
            const result = await response.json();
            window.location.href = '/home';
        } else {
            const error = await response.json();
            document.getElementById('message').textContent = error.message || 'Erro ao cadastrar.';
        }
    } catch (err) {
        document.getElementById('message').textContent = 'Erro de conexão.';
    }
});
