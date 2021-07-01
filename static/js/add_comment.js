$( document ).ready(function () {
    let backendUrl = '/api/v1/comments/create/'
    let btn = $('#btn')
    let message = $('#exampleFormControlTextarea1')
    btn.click(function(e) {
      e.preventDefault()
      $.post(backendUrl, {message: message.val(), post: parseInt(post), csrfmiddlewaretoken: csrf},
      function(data) {
        message.val('');
        console.log(data);
        location.reload();  
      });
    })
  })