document.getElementById('precatory-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const msgEl = document.getElementById('message'); 
    const token = sessionStorage.getItem('auth_token');
    const credor_id = document.getElementById('op-credor').value;
    const foro = document.getElementById('foro').value;
    const num_precatorio = e.target.numero_precatorio.value;
    const valor_nominal = e.target.valor_nominal.value;
    
    const enviado_em = document.getElementById('enviado_em').value;

    const formData = new FormData();
    formData.append('credor_id', credor_id);
    formData.append('foro', foro);
    formData.append('numero_precatorio', num_precatorio);
    formData.append('valor_nominal', valor_nominal);
    formData.append('data_publicacao', enviado_em);

    try {
        const res = await fetch('/api/precatory', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            credentials: 'include',
            body: formData
        });

        const responseData = await res.json();

        if (res.ok) {
            msgEl.style.color = 'green';
            msgEl.textContent = responseData.message;

            setTimeout(() => {
                window.location.href = '/precatorio';
            }, 1000);

        } else {
            msgEl.style.color = 'red';
            msgEl.textContent = responseData.message || 'Erro ao cadastrar precatorio.';
        }

    } catch (error) {
        msgEl.style.color = 'red';
        msgEl.textContent = 'Erro na conexão com o servidor.';
    }



});