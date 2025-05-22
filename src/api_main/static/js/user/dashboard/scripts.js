document.getElementById('credor-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const form = e.target;
    const msgEl = document.getElementById('message');
    const token = sessionStorage.getItem('auth_token');

    console.log("Token:", token);

    if (!token) {
        msgEl.style.color = 'red';
        msgEl.textContent = 'Token de autenticação não encontrado.';
        return;
    }

    const data = new FormData();
    data.append('nome', form.nome.value);
    data.append('cpf_cnpj', form.cpf_cnpj.value);
    data.append('email', form.email.value);
    data.append('telefone', form.telefone.value);

    const appendIfExists = (fieldName, fallback = '') => {
        const input = form.querySelector(`[name="${fieldName}"]`);
        data.append(fieldName, input ? input.value : fallback);
    };

    appendIfExists('numero_precatorio', 0);
    appendIfExists('valor_nominal', 0);
    appendIfExists('foro', 'TJSP');
    appendIfExists('data_publicacao', '2000-01-01');

    const obj = {};
    data.forEach((value, key) => {
    obj[key] = value;
    });
    console.log(obj);

    try {
        const res = await fetch('/api/creditors', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            credentials: 'include',
            body: data
        })

        const responseData = await res.json();

        if (res.ok) {
            msgEl.style.color = 'green';
            msgEl.textContent = responseData.message || 'Credor cadastrado com sucesso!';
            setTimeout(() => window.location.href = '/documentos', 1000);
        } else {
            msgEl.style.color = 'red';
            msgEl.textContent = responseData.message || 'Erro ao cadastrar o credor.';
        }
    } catch (error) {
        console.error('Erro na requisição:', error);
        msgEl.style.color = 'red';
        msgEl.textContent = 'Erro de conexão com o servidor.';
    }
});
