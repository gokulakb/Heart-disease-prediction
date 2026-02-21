// Ensure all links work properly
document.addEventListener('DOMContentLoaded', function() {
    // Handle modal interactions
    var doctorModal = document.getElementById('doctorModal');
    if (doctorModal) {
        var modal = new bootstrap.Modal(doctorModal);
        
        // Example: You can add additional modal show/hide logic here
        doctorModal.addEventListener('shown.bs.modal', function () {
            console.log('Modal is fully shown');
        });
    }
    
    // Prevent default behavior for any disabled links
    document.querySelectorAll('a.disabled').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
        });
    });
    
    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});