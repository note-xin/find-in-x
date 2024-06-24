document.addEventListener('DOMContentLoaded', function() {
    const results = JSON.parse(localStorage.getItem('searchResults'));
    const resultsTableBody = document.querySelector('#resultsTable tbody');
    if (results) {
        results.forEach(result => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><a href="${result.link}">${result.title}</a></td>
                <td>${result.snippet}</td>
                <td>${result.datecreated}</td>
                <td>${result.datepublished}</td>
            `;
            resultsTableBody.appendChild(row);
        });
    } else {
        const row = document.createElement('tr');
        row.innerHTML = '<td colspan="4">No results found.</td>';
        resultsTableBody.appendChild(row);
    }

    document.getElementById('backButton').addEventListener('click', function() {
        window.location.href = '/';
    });
});
