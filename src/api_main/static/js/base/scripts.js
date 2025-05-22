document.getElementById('logout')?.addEventListener('click', (e) => {
    e.preventDefault();
    sessionStorage.removeItem('auth_token'); 
    window.location.href = '/logout';
});

document.addEventListener('DOMContentLoaded', async () => {
    function parseJwt(token) {
        const base64Url = token.split('.')[1];
        const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        const jsonPayload = decodeURIComponent(atob(base64).split('').map(c =>
            '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
        ).join(''));
        return JSON.parse(jsonPayload);
    }

    const msgEl = document.getElementById('message');
    const selectEl = document.getElementById('op-credor');
    if (!msgEl || !selectEl) return; 

    const token = sessionStorage.getItem('auth_token');
    if (!token) {
        msgEl.style.color = 'red';
        msgEl.textContent = 'Token não encontrado.';
        return;
    }

    let sub_id = '';
    try {
        const payload = parseJwt(token);
        sub_id = payload.sub;
    } catch (e) {
        return;
    }

    try {
        const res = await fetch(`/api/users/${sub_id}/creditors`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            credentials: 'include'
        });

        const responseData = await res.json();
        
        if (Array.isArray(responseData)) {
            selectEl.innerHTML = responseData.map(doc => `
                <option value="${doc.id}">${doc.nome}</option>
            `).join('');
        } else if (responseData && responseData.nome) {
            selectEl.innerHTML = `<option value="${responseData.id}">${responseData.nome}</option>`;
        } else {
            selectEl.innerHTML = '<option>Sem dados</option>';
        }
    } catch (error) {
        msgEl.style.color = 'red';
        msgEl.textContent = 'Erro na conexão com o servidor.';
    }

});
