document.querySelectorAll('.task input[type="checkbox"]').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
      const taskId = this.id; // Assuming the id is the task ID
      fetch(`/toggle/${taskId}/`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': '{{ csrf_token }}', // Use Django's CSRF token
          'Content-Type': 'application/json'
        }
      }).then(response => {
        if (response.ok) {
          location.reload(); // Reload the page to reflect changes
        } else {
          alert('An error occurred.');
        }
      });
    });
  });
document.querySelectorAll('.settings i').forEach(icon => {
  icon.addEventListener('click', function() {
    const menu = this.nextElementSibling;
    menu.classList.toggle('show');
  });
});

document.getElementById('ok1').addEventListener('change', function() {
  document.getElementById('ok').click();
});