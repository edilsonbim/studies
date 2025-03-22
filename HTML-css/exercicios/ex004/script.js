document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const loginMessage = document.getElementById('loginMessage');

    // Validação simples (usuário e senha fictícios)
    if (username === "admin" && password === "1234") {
        loginMessage.textContent = "Login realizado com sucesso!";
        loginMessage.style.color = "green";
    } else {
        loginMessage.textContent = "Usuário ou senha incorretos.";
        loginMessage.style.color = "red";
    }
});