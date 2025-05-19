
document.getElementById('logout').addEventListener('click', (e) => {
    e.preventDefault();
    window.location.href = '/logout';
    sessionStorage.setItem('auth_token', null);
});

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

    data.append('numero_precatorio', form.numero_precatorio.value || 0);
    data.append('valor_nominal', form.valor_nominal.value || 0);
    data.append('foro', form.foro.value || 'TJSP');
    data.append('data_publicacao', form.data_publicacao.value || '01/01/2000');
    
    const obj = {};
    data.forEach((value, key) => {
    obj[key] = value;
    });
    console.log(obj);

    try {
        const res = await fetch('/api/credores', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            credentials: 'include',
            body: data
        })

        const responseData = await res.json();

        console.log("Response data:", responseData);

        if (res.ok) {
            msgEl.style.color = 'green';
            msgEl.textContent = responseData.message || 'Credor cadastrado com sucesso!';
            setTimeout(() => window.location.href = '/dashboard', 1000);
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
