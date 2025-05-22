document.getElementById('certificate-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const msgEl = document.getElementById('message'); 
    const token = sessionStorage.getItem('auth_token');
    const credor_id = document.getElementById('op-credor').value;
    const foro = document.getElementById('tipo').value;

    const file = e.target.arquivo_url.files[0];

    const enviado_em = document.getElementById('enviado_em').value;

    const status = "PENDING";
    const origim = "MANUAL";

    const formData = new FormData();
    formData.append('credor_id', credor_id);
    formData.append('tipo', foro);
    formData.append('arquivo_url', file);
    formData.append('recebida_em', enviado_em);
    formData.append('status', status);
    formData.append('origem', origim);

    function logFormData(formData) {
    for (const [key, value] of formData.entries()) {
            console.log(`${key}:`, value);
        }
    }

    logFormData(formData);

    try {
        const res = await fetch('/api/certificates', {
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
                window.location.href = '/certidao';
            }, 1000);

        } else {
            msgEl.style.color = 'red';
            msgEl.textContent = responseData.message || 'Erro ao cadastrar precatorio.';
        }

    } catch (error) {
        msgEl.style.color = 'red';
        msgEl.textContent = 'Erro na conexão com o servidor.';
    }

})
