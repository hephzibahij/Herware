// form.js
document.getElementById('join-us-button').addEventListener('click', function() {
  document.getElementById('join-us-form').style.display = 'block';
});

document.getElementById('join-us-form').addEventListener('submit', function(event) {
  event.preventDefault();
  console.log("Form submitted with data:", new FormData(document.getElementById('join-us-form')));
  document.getElementById('join-us-form').style.display = 'none';
});
