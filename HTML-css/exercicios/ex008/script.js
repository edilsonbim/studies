// Efeito de digitação no texto "Quem sou eu?"
const aboutMeText = document.querySelector('.about-me p');
const originalText = aboutMeText.textContent;
aboutMeText.textContent = '';

let i = 0;
function typeWriter() {
    if (i < originalText.length) {
        aboutMeText.textContent += originalText.charAt(i);
        i++;
        setTimeout(typeWriter, 50);
    }
}

typeWriter();

// Efeito de hover no header
document.querySelector('header').addEventListener('mouseover', function() {
    this.style.background = 'rgba(0, 39, 118, 0.7)';
});

document.querySelector('header').addEventListener('mouseout', function() {
    this.style.background = 'rgba(0, 0, 0, 0.7)';
});