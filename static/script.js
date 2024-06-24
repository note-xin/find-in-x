document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const keyword = document.getElementById('keyword').value;
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ keyword: keyword })
    })
    .then(response => response.json())
    .then(data => {
        localStorage.setItem('searchResults', JSON.stringify(data));
        window.location.href = '/results';
    })
    .catch(error => console.error('Error:', error));
});
