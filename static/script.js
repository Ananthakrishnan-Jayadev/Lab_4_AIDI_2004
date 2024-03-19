 $(document).ready(function() {
  $('#fishForm').submit(function(event) {
    event.preventDefault();

    var formData = {
      weight: parseFloat($('#weight').val()),
      length1: parseFloat($('#length1').val()),
      length2: parseFloat($('#length2').val()),
      length3: parseFloat($('#length3').val()),
      height: parseFloat($('#height').val()),
      width: parseFloat($('#width').val())
    };

    $.ajax({
      url: '/predict',
      type: 'POST',
      contentType: 'application/json',  // Set content type to JSON
      data: JSON.stringify(formData),   // Convert form data to JSON string
      success: function(response) {
        // Redirect to the result page
        window.location.href = '/result?' + $.param(response);
      },
      error: function(error) {
        console.log(error);
        alert('An error occurred during prediction.');
      }
    });
  });
});

