const images = document.querySelectorAll('.carousel-image');
let index = 0;

function nextImage() {
  images.forEach(image => image.classList.remove('active'));
  index = (index + 1) % images.length;
  images[index].classList.add('active');
}

// Configura o intervalo de tempo para alternar as imagens
setInterval(nextImage, 5000);
