  //
  // // Initialize Firebase
  // var config = {
  //   apiKey: "AIzaSyAc6xANvMdWV2TTJA_Z0Bnb26JYxySKSS8",
  //   authDomain: "smart-spirometer.firebaseapp.com",
  //   databaseURL: "https://smart-spirometer.firebaseio.com",
  //   projectId: "smart-spirometer",
  //   storageBucket: "smart-spirometer.appspot.com",
  //   messagingSenderId: "846679117231"
  // };
  // firebase.initializeApp(config);
  //
  function get_data(page,count){
   $.ajax({
          type: "POST",
          url: "http://localhost:8080/get_data",
          data: {
              page: page,
              count: count,
          }
      }).done(function (data) {
          console.log('get returned data');
          console.log(data);
          // console.log(data_return.name);
          let messageDiv = document.getElementById("value");
          messageDiv.innerHTML = data;
          handle_response(data);
      });
  }

  function handle_response(data){
    let data_array=data.split("],[")
    console.log(data_array)
  }

  get_data('page_user',1)
