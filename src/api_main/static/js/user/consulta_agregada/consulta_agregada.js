    document.addEventListener('DOMContentLoaded', async () => {
    const select = document.getElementById('op-credor');
    const resultContainer = document.getElementById("result-container");
    const msgEl = document.getElementById('message');

    const token = sessionStorage.getItem('auth_token');

    async function fetchCredorData(credor_id) {
        let html = "";
        resultContainer.innerHTML = "<p class='text-gray-700'>Buscando dados...</p>";

        try {
        const response = await fetch(`/api/users/${credor_id}/summary`, {
            method: 'GET',
            headers: { 'Authorization': `Bearer ${token}` },
            credentials: 'include',
        });

        const json = await response.json();

        const data = json[0].data;
        
        if (data.creditors && data.creditors.length > 0) {
                for (const credor of data.creditors) {
                    html += `
                        <div class='mb-4'>
                            <p class='text-sm text-gray-800'>
                                <strong>Nome:</strong> ${credor.nome} |
                                <strong>CPF/CNPJ:</strong> ${credor.cpf_cnpj} |
                                <strong>Email:</strong> ${credor.email} |
                                <strong>Telefone:</strong> ${credor.telefone}
                            </p>
                        </div>
                    `;
                }
            }
        
        html += `<h3 class='text-xl font-semibold mb-2'>Documentos</h3>`;

        if (data.personal_documents && data.personal_documents.length > 0) {
            html += `<div class="flex flex-wrap gap-4">`;
            for (const doc of data.personal_documents) {
                html += `
                    <div class='mb-4'>
                        <ul class='list-disc pl-5 text-sm text-gray-800'>
                            <li><strong>Tipo:</strong> ${doc.tipo}</li>
                            <li><strong>Arquivo:</strong> ${doc.arquivo_url}</li>
                            <li><strong>Data:</strong> ${doc.enviado_em}</li>
                        </ul>
                    </div>
                `;}
                html += `</div>`;
            }

        
        html += `<h3 class='text-xl font-semibold mb-2'>Precatórios</h3>`;

        if (data.precatory && data.precatory.length > 0) {
            html += `<div class="flex flex-wrap gap-4">`;

            for (const doc of data.precatory    ) {
                html += `<div class='mb-4'>
                    <ul class='list-disc pl-5 text-sm text-gray-800'>
                        <li><strong>Numero:</strong> ${doc.numero_precatorio}</li>
                        <li><strong>Valor:</strong> ${doc.valor_nominal}</li>
                        <li><strong>Foro:</strong> ${doc.foro}</li>
                        <li><strong>Data:</strong> ${doc.data_publicacao}</li>
                    </ul>
                </div>`;
            }
            html += `</div>`;
        }

        html += `<h3 class='text-xl font-semibold mb-2'>Certificados</h3>`;

        if (data.certificates && data.certificates.length > 0) {
            html += `<div class="flex flex-wrap gap-4">`;
            for (const cert of data.certificates) {
                html += `
                    <div class='mb-4'>
                        <ul class='list-disc pl-5 text-sm text-gray-800'>
                            <li><strong>Tipo:</strong> ${cert.tipo}</li>
                            <li><strong>Origem:</strong> ${cert.origem}</li>
                            <li><strong>Status:</strong> ${cert.status}</li>
                            <li><strong>Data:</strong> ${cert.recebida_em}</li>
                            <li><strong>Arquivo:</strong> ${cert.arquivo_url} </li>
                        </ul>
                    </div>
                `;}
            html += `</div>`;
        }
 
        } catch (error) {
            if (msgEl) {
                msgEl.style.color = 'red';
                msgEl.textContent = 'Erro na conexão com o servidor.';
            }
        } 

    resultContainer.innerHTML = html || "<p class='text-gray-600'>Nenhum dado encontrado.</p>";

    }

    try {

        function parseJwt(token) {
            const base64Url = token.split('.')[1];
            const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
            const jsonPayload = decodeURIComponent(atob(base64).split('').map(c =>
                '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
            ).join(''));
            return JSON.parse(jsonPayload);
        }

        let sub_id = '';
        try {
            const payload = parseJwt(token);
            sub_id = payload.sub;
        } catch (e) {
            return;
        }

        const resCredores = await fetch(`/api/users/${sub_id}/creditors`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`
                },
                credentials: 'include'
            });


        const data = await resCredores.json();

        if (data.errors && data.errors.length > 0) {
                html += "<div class='text-red-600'><strong>Erros:</strong><ul>";
                data.errors.forEach(err => {
                    html += `<li>${err}</li>`;
                });
                html += "</ul></div>";
            }
        
        if (data.creditors && data.creditors.length > 0) {
                html += "<div><h3 class='text-xl font-semibold mb-2'>Credor</h3><ul class='list-disc pl-5'>";
                data.creditors.forEach(c => {
                    html += `<li>${c.nome} (${c.cpf_cnpj}) - ${c.email} / ${c.telefone}</li>`;
                });
                html += "</ul></div>";
            }


        data.forEach(c => {
        const opt = document.createElement('option');
        opt.value = c.id;
        opt.textContent = c.nome;
        select.appendChild(opt);
        });

        if (data.length > 0) {
        fetchCredorData(data[0].id);
        }

    } catch (err) {
        console.error("Erro ao carregar credores:", err);
    }

    select.addEventListener('change', (e) => {
        fetchCredorData(e.target.value);
    });

    });
