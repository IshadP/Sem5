document.getElementById('signupForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const user = { username, email, password };
    localStorage.setItem(email, JSON.stringify(user));
    alert('Sign up successful! You can now log in.');
    window.location.href = 'index.html';
});

document.getElementById('loginForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    const user = JSON.parse(localStorage.getItem(email));
    if (user && user.password === password) {
        alert('Login successful!');
        // Redirect or perform action on successful login
    } else {
        alert('Invalid credentials!');
    }
});

document.getElementById('resetForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const email = document.getElementById('resetEmail').value;

    const user = JSON.parse(localStorage.getItem(email));
    if (user) {
        alert('A password reset link has been sent to ' + email);
        // Simulate sending a reset link
    } else {
        alert('Email not found!');
    }
});
