document.addEventListener('DOMContentLoaded', async () => {
    const navLog = document.getElementById('user-login');
    const navLogout = document.getElementById('user-logout');

    const logout = document.getElementById('logout');
    
    if (logout) {
        navLog.classList.remove('hidden');
        navLog.classList.add('block');

        navLogout.classList.remove('block');
        navLogout.classList.add('hidden');
    } else {
        navLog.classList.remove('block');
        navLog.classList.add('hidden'); 

        navLogout.classList.remove('hidden');
        navLogout.classList.add('block');

        navLogout.classList.add('h-4');
    }
});