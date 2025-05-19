document.addEventListener('DOMContentLoaded', () => {
  const token = sessionStorage.getItem('auth_token');
    console.log('Token:', token);
    
  if (token) {
    document.getElementById('logged-in-menu').classList.remove('hidden');
    document.getElementById('logged-out-menu').classList.add('hidden');
  } else {
    document.getElementById('logged-in-menu').classList.add('hidden');
    document.getElementById('logged-out-menu').classList.remove('hidden');
  }
});
