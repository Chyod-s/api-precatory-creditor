document.getElementById('personal-document-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const msgEl = document.getElementById('message'); 
    const token = sessionStorage.getItem('auth_token');

    const type = e.target.tipo.value;
    
    const file = e.target.arquivo_url.files[0];

    const day = new Date();
    const dia = String(day.getUTCDate()).padStart(2, '0');
    const mes = String(day.getUTCMonth() + 1).padStart(2, '0');
    const ano = day.getUTCFullYear();
    const dataFormatada = `${dia}/${mes}/${ano}`;
    
    const credor_id = document.getElementById('op-credor').value;
  
    const formData = new FormData();        
    formData.append('credor_id', credor_id);    
    formData.append('tipo', type);
    formData.append('arquivo_url', file); 
    formData.append('enviado_em', dataFormatada);
    
    try {
        const res = await fetch('/api/documents', {
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

            setTimeout(() => window.location.href = '/documentos', 1000);
        } else {
            msgEl.style.color = 'red';
            msgEl.textContent = responseData.message || 'Erro ao cadastrar documento.';
        }
    } catch (error) {
        msgEl.style.color = 'red';
        msgEl.textContent = 'Erro na conexão com o servidor.';
    }
});
