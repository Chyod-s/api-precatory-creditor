document.addEventListener('DOMContentLoaded', async () => {
    const select = document.getElementById('op-credor');
    const resultContainer = document.getElementById("result-container");
    const msgEl = document.getElementById('message');
    const token = sessionStorage.getItem('auth_token');
    const credor_id = document.getElementById('op-credor').value;

    console.log(credor_id);
    
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
        
        html += `<h3 class='text-1xl font-bold mb-2'>Documentos</h3>`;

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

        
        html += `<h3 class='text-xl font-bold mb-2'>Precatórios</h3>`;

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

        html += `<h3 class='text-xl font-bold mb-2'>Certificados</h3>`;

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
                console.log('Erro na conexão com o servidor.');
            }
        } 

    resultContainer.innerHTML = html || "<p class='text-gray-600'>Nenhum dado encontrado.</p>";

    }

    select.addEventListener('change', (e) => {
        fetchCredorData(e.target.value);
    });


    function waitForSelectValue(callback) {
    const interval = setInterval(() => {
        if (select.value) {
        clearInterval(interval);
        callback(select.value);
        }
    }, 10); 
    }

    waitForSelectValue(credor_id => {
        fetchCredorData(credor_id);
    });


});
