document.getElementById('logout').addEventListener('click', (e) => {
    e.preventDefault();
    window.location.href = '/logout';
    sessionStorage.setItem('auth_token', null);
});