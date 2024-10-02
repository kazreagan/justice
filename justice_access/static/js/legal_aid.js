document.getElementById('search').addEventListener('input', function() {
    let filter = this.value.toLowerCase();
    let orgs = document.querySelectorAll('li');

    orgs.forEach(function(org) {
        if (org.textContent.toLowerCase().includes(filter)) {
            org.style.display = '';
        } else {
            org.style.display = 'none';
        }
    });
});


