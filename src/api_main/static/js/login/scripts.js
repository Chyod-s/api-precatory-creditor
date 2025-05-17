document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.querySelector('#login-form');

  loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
      const query = new URLSearchParams({ username, password }).toString();

      const response = await fetch(`/api/usuarios?${query}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Usuário ou senha inválidos');
      }

      const data = await response.json();
      console.log('Login bem-sucedido:', data);

      await fetch('/auth/session', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user: data })
      });

      window.location.href = '/home';
    } catch (error) {
      alert(`Erro no login: ${error.message}`);
    }
  });
});
