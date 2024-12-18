document.addEventListener('DOMContentLoaded', function () {
    // Function to show the clicked image and hide others
    window.showImage = function (index) {
        const images = document.querySelectorAll('.visualization-image');
        images.forEach((img, i) => {
            img.classList.toggle('hidden', i !== parseInt(index));
        });
    };
});
