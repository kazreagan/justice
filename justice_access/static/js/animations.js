// Entrance animation for images
document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.transition-image');
    const duration = 600; //animation duration
    const visibleTime = 2000; //visibility duration

    const animateImages = () => {
        images.forEach((image, index) => {
            //entrance animation
            setTimeout(() => {
                image.style.opacity = '1' // fade in
            }, index * duration); //stagger entrance by index

            //exit animation
            setTimeout(() => {
                image.style.opacity = '0' //fade out
            }, index * duration + visibleTime); //exit
        });

        //repeat animation
        setTimeout(animateImages, images.length * duration + visibleTime + duration); //loop through 
    };

    animateImages(); //start the loop
})