
const daysElement = document.querySelector("[data-days]")
const hoursElement = document.querySelector("[data-hours]")
const minutesElement = document.querySelector("[data-minutes]")
const secondsElement = document.querySelector("[data-seconds]")

const render = (days, hours, minutes, seconds) => {;
    daysElement.innerHTML = String(days).padStart("2", 0);
    hoursElement.innerHTML = String(hours).padStart("2", 0);
    minutesElement.innerHTML = String(minutes).padStart("2", 0);
    secondsElement.innerHTML = String(seconds).padStart("2", 0);

};


const countdown = () => {
    const now = new Date();
    const nextYear = now.getFullYear() +1;
    const targetDate = new Date(nextYear, 0, 1);

    const timeLeft = targetDate - now;

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24))/ (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60))/(1000*60));
    const seconds = Math.floor((timeLeft % (1000 * 60))/1000);

    render(days, hours, minutes, seconds);
};

setInterval(countdown, 1000);

/* JS BLOG */

let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail 
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
  }
